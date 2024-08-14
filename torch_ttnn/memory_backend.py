import torch.linalg
import torch
from typing import List
import torch._dynamo
from functorch.compile import make_boxed_func
import ttnn
import pickle
from pathlib import Path
import os
from torch_ttnn.mem_utils import *

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True


# The option for torch_ttnn.backend
class TorchTtnnOption:
    def __init__(self, device: ttnn.Device, gen_graphviz=False, metrics_path=""):
        self.device = device
        self.gen_graphviz = gen_graphviz
        self._out_fx_graphs = list()
        self._memory_manager = list()

        if metrics_path:
            p = Path(f"metrics/{metrics_path}")
            os.makedirs(p, exist_ok=True)
        self.metrics_path = metrics_path
        self._metrics = dict()


def register_ttnn_objects(option: TorchTtnnOption):
    """
    torch.fx builds a source object as a string, calls builtin compile(), and finally
    calls builtin exec() with a dictionary of globals that contains the strings (keys)
    that will be replaced by the ttnn objects (values) during evaluation.
    """
    torch.fx.graph._register_custom_builtin("ttnn_Specified_Device", "", option.device)

    torch.fx.graph._register_custom_builtin(
        "ttnn_ROW_MAJOR_LAYOUT", "", ttnn.ROW_MAJOR_LAYOUT
    )
    torch.fx.graph._register_custom_builtin("ttnn_TILE_LAYOUT", "", ttnn.TILE_LAYOUT)

    torch.fx.graph._register_custom_builtin("ttnn_uint32", "", ttnn.uint32)
    torch.fx.graph._register_custom_builtin("ttnn_bfloat16", "", ttnn.bfloat16)

    torch.fx.graph._register_custom_builtin(
        "ttnn_DRAM_MEMORY_CONFIG",
        "",
        ttnn.DRAM_MEMORY_CONFIG,
    )
    torch.fx.graph._register_custom_builtin(
        "ttnn_L1_MEMORY_CONFIG",
        "",
        ttnn.L1_MEMORY_CONFIG,
    )


# The backend for torch.compile that converts a graph to use ttnn.
# The "option" parameter is a dict that contains one key "torch_ttnn_option".
# The value of "torch_ttnn_option" is a TorchTtnnOption object.
# See document for detail.
def aten_backend(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], options: dict
) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """

    # Clone ops used for input aliasing workaround are no longer needed at this point
    from .handle_input_aliasing import remove_clones_for_input_aliasing

    gm = remove_clones_for_input_aliasing(gm)

    option: TorchTtnnOption = options["torch_ttnn_option"]

    # Helper function to count the number of aten ops in the graph currently
    def count_aten_ops():
        aten_ops = [
            str(node.target)
            for node in list(gm.graph.nodes)
            if node.op in ["call_function", "call_method"]
            and isinstance(node.target, torch._ops.OpOverload)
            and "aten" in str(node.target)
        ]
        return len(aten_ops)

    # Save the number of aten ops before compilation
    if option.metrics_path:
        option._metrics["torch_ops_before"] = count_aten_ops()

    # Register ttnn objects as graph globals
    register_ttnn_objects(option)

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from torch.fx.passes.dialect.common.cse_pass import CSEPass
    from torch_ttnn.passes.lowering.to_tt_pass import ToTtPass
    from torch_ttnn.passes.lowering.add_data_move_pass import AddDataMovePass
    from torch_ttnn.passes.graphviz_pass import GraphvizPass
    from torch_ttnn.passes.lowering.eliminate_data_move_pass import (
        EliminateDataMovePass,
    )
    from torch_ttnn.passes.lowering.permute_reshape_tuple import PermuteReshapeTuple
    from torch_ttnn.passes.memory_pass import MemoryPass
    passes = [
        ToTtPass(),
        AddDataMovePass(),
        EliminateDataMovePass(),
        CSEPass(),
        PermuteReshapeTuple(),
        MemoryPass(),
    ]

    # Add graphviz pass interleavly if needed
    if option.gen_graphviz:
        graphviz_filenames = [
            "00.origin",
            "01.to-tt",
            "02.add-data-move",
            "03.elimate-data-move",
            "04.cse",
            "05.permute-reshape-tuple",
            "06.memory-pass",
        ]
        assert len(graphviz_filenames) == len(passes) + 1
        for idx in range(len(graphviz_filenames)):
            passes.insert(idx * 2, GraphvizPass(graphviz_filenames[idx]))

    pm = PassManager(passes=passes)
    gm, modified = pm(gm)

    gm.graph.lint()
    gm.recompile()

    # Get the memory manager object for memory analysis
    for p in passes:
        if isinstance(p, MemoryPass):
            option._memory_manager = p.memory_manager
            mm = p.memory_manager

    # See if SRAM overflows and eviction is required
    while check_sram_overflow(mm) is True:
    # if check_sram_overflow(mm) is True:
        guilty_op, tensors_to_evict = which_tensors_to_evict(mm)

        # Run a eviction pass to remove tensors from device
        # This pass only evicts tensors for a single ttnn op which overflows the SRAM
        # Multiple overflows require multiple run of this pass
        from torch_ttnn.passes.eviction_pass import EvictionPass
        passes = [
            EvictionPass(mm, guilty_op, tensors_to_evict),
            GraphvizPass("eviction-pass"),
            MemoryPass(),
        ]
        pm = PassManager(passes=passes)
        gm, modified = pm(gm)

        gm.graph.lint()
        gm.recompile()

        # Get the memory manager object for memory analysis
        for p in passes:
            if isinstance(p, MemoryPass):
                option._memory_manager = p.memory_manager
                mm = p.memory_manager

    if option.metrics_path:
        # Save the number of aten ops after compilation
        option._metrics["torch_ops_remain"] = count_aten_ops()
        # Save the number of to/from_device ops in current graph
        to_from_device_ops = [
            node.target.__name__
            for node in list(gm.graph.nodes)
            if node.op in ["call_function", "call_method"]
            and (
                "ttnn.to" in node.target.__name__ or "ttnn.from" in node.target.__name__
            )
        ]
        option._metrics["to_from_device_ops"] = len(to_from_device_ops)
        # Save the data as pickle files
        p = Path(f"metrics/{option.metrics_path}")
        pickle_out_path = p / "compiled-op_metrics.pickle"
        with open(pickle_out_path, "wb") as f:
            pickle.dump(option._metrics, f)

    option._out_fx_graphs.append(gm.graph)
    return make_boxed_func(gm)


from torch._dynamo.backends.common import aot_autograd
from functools import partial


from .handle_input_aliasing import insert_clones_for_input_aliasing


# The wrapper of aot_autograd that takes a TorchTtnnOption as options.
def memory_backend(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], **kwargs
) -> torch.fx.GraphModule:
    if options := kwargs.get("options"):
        options = {"torch_ttnn_option": options}
    else:
        raise RuntimeError("TorchTtnnOption missing")

    gm = insert_clones_for_input_aliasing(gm)
    return aot_autograd(fw_compiler=partial(aten_backend, options=options))(
        gm, example_inputs
    )
