import torch.linalg
import torch
import ttnn
import torch._dynamo
<<<<<<< HEAD
from typing import List, Optional, Union, Mapping, Any
=======
from functorch.compile import make_boxed_func
import ttnn
import pickle
from pathlib import Path
import os
import torch_ttnn.metrics as metrics
>>>>>>> upstream/main

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True

<<<<<<< HEAD
=======

# The option for torch_ttnn.backend
class TorchTtnnOption:
    def __init__(self, device: ttnn.Device, gen_graphviz=False, metrics_path=""):
        self.device = device
        self.gen_graphviz = gen_graphviz
        self._out_fx_graphs = list()

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
>>>>>>> upstream/main

# The option for torch_ttnn.backend
class TenstorrentBackendOption:
    def __init__(self, device: ttnn.Device, tracer_option = None):
        self.device = device
        self.gen_graphviz = False
        self._out_fx_graphs = list()
        self.tracer_option = tracer_option

# The backend for torch.compile that converts a graph to use ttnn.
# The "option" parameter is a TorchTtnnOption object
# See document for detail.
def aten_backend(
    gm: torch.fx.GraphModule,
    example_inputs: List[torch.Tensor],
    options: TenstorrentBackendOption = None,
) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """

<<<<<<< HEAD
    option: TenstorrentBackendOption = options
    torch.fx.graph._register_custom_builtin("ttnn_Specified_Device", "", option.device)
    torch.fx.graph._register_custom_builtin("ttnn_TILE_LAYOUT", "", ttnn.TILE_LAYOUT)
    torch.fx.graph._register_custom_builtin(
        "ttnn_ROW_MAJOR_LAYOUT", "", ttnn.ROW_MAJOR_LAYOUT
    )

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from torch.fx.passes.dialect.common.cse_pass import CSEPass
    from .passes.to_tt_pass import ToTtPass
    from .passes.add_coreops_pass import AddDataMovePass
    from .passes.graphviz_pass import GraphvizPass
    from .passes.eliminate_coreops_pass import EliminateCoreopsPass
    from .passes.permute_reshape_tuple import PermuteReshapeTuple
=======
    # Clone ops used for input aliasing workaround are no longer needed at this point
    from .handle_input_aliasing import remove_clones_for_input_aliasing

    gm = remove_clones_for_input_aliasing(gm)

    option: TorchTtnnOption = options["torch_ttnn_option"]

    # Save the number of aten ops before compilation
    if option.metrics_path:
        original_schema_list = metrics.collect_schema_from_nodes(gm.graph.nodes)
        metrics.save_pickle(
            original_schema_list, option.metrics_path, "original-schema_list"
        )

    # Register ttnn objects as graph globals
    register_ttnn_objects(option)

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from torch_ttnn.passes.lowering.to_tt_pass import ToTtPass
    from torch_ttnn.passes.lowering.add_data_move_pass import AddDataMovePass
    from torch_ttnn.passes.graphviz_pass import GraphvizPass
    from torch_ttnn.passes.lowering.eliminate_data_move_pass import (
        EliminateDataMovePass,
    )
    from torch_ttnn.passes.lowering.permute_reshape_tuple import PermuteReshapeTuple
>>>>>>> upstream/main

    passes = [
        ToTtPass(),
        AddDataMovePass(),
<<<<<<< HEAD
        EliminateCoreopsPass(),
        CSEPass(),
=======
        EliminateDataMovePass(),
>>>>>>> upstream/main
        PermuteReshapeTuple(),
    ]

    # Add graphviz pass interleavly if needed
    if option.gen_graphviz:
<<<<<<< HEAD
        passes_with_graphviz = [GraphvizPass("00.origin")]
        for idx in range(len(passes)):
            passes_with_graphviz.append(passes[idx])
            passes_with_graphviz.append(
                GraphvizPass(f"{idx + 1:02d}.{passes[idx].__class__.__name__}")
            )
        passes = passes_with_graphviz
=======
        graphviz_filenames = [
            "00.origin",
            "01.to-tt",
            "02.add-data-move",
            "03.elimate-data-move",
            "04.permute-reshape-tuple",
        ]
        assert len(graphviz_filenames) == len(passes) + 1
        for idx in range(len(graphviz_filenames)):
            p = Path(f"metrics/{option.metrics_path}/{graphviz_filenames[idx]}")
            passes.insert(idx * 2, GraphvizPass(p))
>>>>>>> upstream/main

    pm = PassManager(passes=passes)
    gm, modified = pm(gm)

    gm.graph.lint()
    gm.recompile()

    if option.metrics_path:
        compiled_schema_list = metrics.collect_schema_from_nodes(gm.graph.nodes)
        metrics.save_pickle(
            compiled_schema_list, option.metrics_path, "compiled-schema_list"
        )

    option._out_fx_graphs.append(gm.graph)
    return make_boxed_func(gm)


from torch._dynamo.backends.common import aot_autograd
from functools import partial

<<<<<<< HEAD
# The backend for torch.compile that converts a graph to use ttnn.
# The "option" parameter is a TorchTtnnOption object
# See document for detail.
# This function is a wrapper of aten_backend, and is used by torch.compile.
# This function is also registered as a backend for torch.compile.
def ttnn_backend(
    gm: torch.fx.GraphModule,
    example_inputs: List[torch.Tensor],
    options: TenstorrentBackendOption = None,
) -> torch.fx.GraphModule:
    tracer_option = options.tracer_option
    if tracer_option is not None:
        from ..tracer import Tracer
        out_prefix = f"fw_{tracer_option['model_name']}"
        out_folder = tracer_option["out_folder"]
        trace_orig = tracer_option["trace_orig"] if "trace_orig" in tracer_option else True
        trace_modi = tracer_option["trace_modi"] if "trace_modi" in tracer_option else False
        fw_compiler = Tracer(partial(aten_backend, options=options), out_prefix, out_folder, trace_orig, trace_modi)
        return aot_autograd(fw_compiler=fw_compiler)(
            gm, example_inputs
        )
    else:
        return aot_autograd(fw_compiler=partial(aten_backend, options=options))(
            gm, example_inputs
        )
=======

from .handle_input_aliasing import insert_clones_for_input_aliasing


# The wrapper of aot_autograd that takes a TorchTtnnOption as options.
def backend(
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
>>>>>>> upstream/main
