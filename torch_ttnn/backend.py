import torch.linalg
import torch
import torch._dynamo
from typing import List, Optional, Union, Mapping, Any
from functorch.compile import make_boxed_func
import ttnn
import pickle
from pathlib import Path
import os
from torch_ttnn.handle_input_aliasing import insert_clones_for_input_aliasing
import torch_ttnn.metrics as metrics

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True


# The option for torch_ttnn.backend
class TorchTtnnOption:
    def __init__(
        self,
        device: ttnn.Device,
        gen_graphviz=False,
        metrics_path="",
        tracer_option=None,
        bypass=False,
    ):
        self.device = device
        self.gen_graphviz = gen_graphviz
        self._out_fx_graphs = list()
        self.tracer_option = tracer_option

        if metrics_path:
            p = Path(f"metrics/{metrics_path}")
            os.makedirs(p, exist_ok=True)
        self.metrics_path = metrics_path
        self.bypass = bypass
        self.original_schema_list = list()
        self.compiled_schema_list = list()


def register_ttnn_objects(option: TorchTtnnOption):
    """
    torch.fx builds a source object as a string, calls builtin compile(), and finally
    calls builtin exec() with a dictionary of globals that contains the strings (keys)
    that will be replaced by the ttnn objects (values) during evaluation.
    """
    torch.fx.graph._register_custom_builtin("ttnn_Specified_Device", "", option.device)

    torch.fx.graph._register_custom_builtin("ttnn_ROW_MAJOR_LAYOUT", "", ttnn.ROW_MAJOR_LAYOUT)
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
# The "option" parameter is a TorchTtnnOption object
# See document for detail.
def aten_backend(
    gm: torch.fx.GraphModule,
    example_inputs: List[torch.Tensor],
    options: TorchTtnnOption,
) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """

    option: TorchTtnnOption = options

    # Clone ops used for input aliasing workaround are no longer needed at this point
    from .handle_input_aliasing import remove_clones_for_input_aliasing

    gm = remove_clones_for_input_aliasing(gm)
    # Save the number of aten ops before compilation
    if option.metrics_path:
        option.original_schema_list.extend(metrics.collect_schema_from_nodes(gm.graph.nodes))

    # Do not continue with compilation if bypass
    if option.bypass:
        option._out_fx_graphs.append(gm.graph)
        return make_boxed_func(gm)

    # Register ttnn objects as graph globals
    register_ttnn_objects(option)

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.infra.pass_manager import PassManager
    from torch.fx.passes.dialect.common.cse_pass import CSEPass
    from torch_ttnn.passes.lowering.to_tt_pass import ToTtPass
    from torch_ttnn.passes.lowering.add_data_move_pass import AddDataMovePass
    from torch_ttnn.passes.lowering.eliminate_coreops_pass import EliminateCoreopsPass
    from torch_ttnn.passes.graphviz_pass import GraphvizPass
    from torch_ttnn.passes.lowering.permute_reshape_tuple import PermuteReshapeTuple

    passes = [
        ToTtPass(),
        AddDataMovePass(),
        EliminateCoreopsPass(),
        CSEPass(),
        PermuteReshapeTuple(),
    ]

    # Add graphviz pass interleavly if needed
    if option.gen_graphviz:
        passes_with_graphviz = [GraphvizPass("00.origin")]
        for idx in range(len(passes)):
            passes_with_graphviz.append(passes[idx])
            passes_with_graphviz.append(
                GraphvizPass(f"metrics/{option.metrics_path}/{idx + 1:02d}.{passes[idx].__class__.__name__}")
            )
        passes = passes_with_graphviz

    pm = PassManager(passes=passes)
    gm, modified = pm(gm)

    gm.graph.lint()
    gm.recompile()

    if option.metrics_path:
        option.compiled_schema_list.extend(metrics.collect_schema_from_nodes(gm.graph.nodes))

    option._out_fx_graphs.append(gm.graph)
    return make_boxed_func(gm)


from torch._dynamo.backends.common import aot_autograd
from functools import partial


# The backend for torch.compile that converts a graph to use ttnn.
# The "option" parameter is a TorchTtnnOption object
# See document for detail.
# This function is a wrapper of aten_backend, and is used by torch.compile.
# This function is also registered as a backend for torch.compile.
def ttnn_backend(
    gm: torch.fx.GraphModule,
    example_inputs: List[torch.Tensor],
    options: TorchTtnnOption = None,
) -> torch.fx.GraphModule:
    tracer_option = options.tracer_option
    if tracer_option is not None:
        from ..tracer import Tracer

        out_prefix = f"fw_{tracer_option['model_name']}"
        out_folder = tracer_option["out_folder"]
        trace_orig = tracer_option["trace_orig"] if "trace_orig" in tracer_option else True
        trace_modi = tracer_option["trace_modi"] if "trace_modi" in tracer_option else False
        fw_compiler = Tracer(
            partial(aten_backend, options=options),
            out_prefix,
            out_folder,
            trace_orig,
            trace_modi,
        )
        return aot_autograd(fw_compiler=fw_compiler)(gm, example_inputs)
    else:
        gm = insert_clones_for_input_aliasing(gm)
        return aot_autograd(fw_compiler=partial(aten_backend, options=options))(gm, example_inputs)
