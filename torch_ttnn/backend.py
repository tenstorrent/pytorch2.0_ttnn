# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
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
import tools.export_code as export_code
import torch_ttnn.metrics as metrics
from torch_ttnn import mem_utils
import copy
from torch_ttnn.utils import get_add_custom_object_in_graph

torch._dynamo.config.suppress_errors = False
torch._dynamo.config.verbose = True


# The option for torch_ttnn.backend
class TorchTtnnOption:
    def __init__(
        self,
        device: ttnn.Device,
        gen_graphviz=False,
        run_mem_analysis=False,
        run_eviction_opt=False,
        verbose=True,
        metrics_path="",
        tracer_option=None,
        bypass_compile=False,
        use_less_ttnn_op_types=True,
        export_code=None,
        total_num_iterations=1,
        data_parallel=False,
    ):
        self.device = device
        self.gen_graphviz = gen_graphviz
        self._out_fx_graphs = list()
        self.memory_manager = None
        self.run_mem_analysis = run_mem_analysis
        self.run_eviction_opt = run_eviction_opt
        self.verbose = verbose
        self.tracer_option = tracer_option
        self.total_num_iterations = total_num_iterations
        self.data_parallel = data_parallel

        self.metrics_path = metrics_path
        self.bypass_compile = bypass_compile
        self.use_less_ttnn_op_types = use_less_ttnn_op_types
        self.original_schema_list = list()
        self.compiled_schema_list = list()

        # Used for generate standalone python script
        self.export_code = export_code
        self._aten_fx_graphs = list()
        self._all_inputs = list()
        self._ttnn_fx_graphs = list()

        # Used for multi-device
        self._n_parameters = None
        self._n_buffers = None
        self._n_arguments = None

    def reset_containers(self):
        self._out_fx_graphs = list()
        self.original_schema_list = list()
        self._ttnn_fx_graphs = list()


def register_ttnn_objects(option: TorchTtnnOption):
    """
    torch.fx builds a source object as a string, calls builtin compile(), and finally
    calls builtin exec() with a dictionary of globals that contains the strings (keys)
    that will be replaced by the ttnn objects (values) during evaluation.
    """
    get_add_custom_object_in_graph("ttnn_Specified_Device", option.device)

    get_add_custom_object_in_graph("ttnn_ROW_MAJOR_LAYOUT", ttnn.ROW_MAJOR_LAYOUT)
    get_add_custom_object_in_graph("ttnn_TILE_LAYOUT", ttnn.TILE_LAYOUT)

    get_add_custom_object_in_graph("ttnn_uint32", ttnn.uint32)
    get_add_custom_object_in_graph("ttnn_int32", ttnn.int32)
    get_add_custom_object_in_graph("ttnn_bfloat16", ttnn.bfloat16)

    get_add_custom_object_in_graph("ttnn_DRAM_MEMORY_CONFIG", ttnn.DRAM_MEMORY_CONFIG)
    get_add_custom_object_in_graph("ttnn_L1_MEMORY_CONFIG", ttnn.L1_MEMORY_CONFIG)


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

    # Save aten graph if requested
    if options.export_code:
        # Will this hamper memory usage?
        graph_copy = copy.deepcopy(gm.graph)
        graph_copy.owning_module = gm
        option._aten_fx_graphs[-1].append(graph_copy)

    # Save the number of aten ops before compilation
    if option.metrics_path:
        # do constant folding for consistency of input varation
        from torch.fx.passes.infra.pass_manager import PassManager
        from torch_ttnn.passes.constant_folding_pass import ConstantFoldingPass

        pm_fold = PassManager(passes=[ConstantFoldingPass()])
        gm_fold, modified = pm_fold(gm)
        option.original_schema_list.extend(metrics.collect_input_variations_from_list_nodes(gm_fold.graph.nodes))

    # Do not continue with compilation if bypass
    if option.bypass_compile:
        option._out_fx_graphs.append(gm.graph)
        return make_boxed_func(gm)

    # Register ttnn objects as graph globals
    register_ttnn_objects(option)

    # Run analysis passes to help with ttnn ops
    from torch.fx.passes.infra.pass_manager import PassManager
    from torch_ttnn.passes.analysis.input_analysis_pass import InputAnalysisPass
    from torch_ttnn.passes.analysis.multi_device_shard_analysis_pass import MultiDeviceShardAnalysisPass

    # Rewrite with ttnn ops, will insert redundant data movement
    from torch.fx.passes.dialect.common.cse_pass import CSEPass
    from torch_ttnn.passes.multi_device_pass import MultiDevicePass
    from torch_ttnn.passes.constant_folding_pass import ConstantFoldingPass
    from torch_ttnn.passes.lowering.to_tt_pass import ToTtPass
    from torch_ttnn.passes.fusion_pass import FusionPass
    from torch_ttnn.passes.lowering.add_data_move_pass import AddDataMovePass
    from torch_ttnn.passes.lowering.eliminate_coreops_pass import EliminateCoreopsPass
    from torch_ttnn.passes.graphviz_pass import GraphvizPass
    from torch_ttnn.passes.lowering.permute_reshape_tuple import PermuteReshapeTuple
    from torch_ttnn.passes.memory_pass import MemoryPass

    passes = [
        InputAnalysisPass(option._n_parameters, option._n_buffers, option._n_arguments),
        MultiDeviceShardAnalysisPass(option.device),
        ConstantFoldingPass(),
        MultiDevicePass(option.device, example_inputs),
        ToTtPass(option.device, option.use_less_ttnn_op_types),
        AddDataMovePass(option.device),
        EliminateCoreopsPass(),
        CSEPass(),
        PermuteReshapeTuple(),
        FusionPass(),
    ]

    mem_pass = MemoryPass(option.verbose)
    if option.run_mem_analysis:
        passes.append(mem_pass)

    # Add graphviz pass interleavly if needed
    if option.gen_graphviz:
        passes_with_graphviz = [GraphvizPass(f"metrics/{option.metrics_path}/00.origin")]
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

    # Get the memory manager object for memory analysis
    if option.run_mem_analysis:
        option.memory_manager = mem_pass.mm

    # Run eviction opt pass if enabled
    if option.run_eviction_opt == True:
        assert option.run_mem_analysis == True, "Eviction pass depends on memory analysis pass!"
        from torch_ttnn.passes.eviction_pass import EvictionPass

        nth_eviction = 1
        max_evictions_limit = option.memory_manager.max_evictions_required()

        # See if SRAM overflows and eviction is required
        while mem_utils.check_sram_overflow(option.memory_manager) is True:
            if nth_eviction > max_evictions_limit:
                assert False, "Max evictions done, still model doesn't fit in memory!"

            guilty_op, tensors_to_evict = mem_utils.which_tensors_to_evict(option.memory_manager)
            # This indicates splitting is required
            if tensors_to_evict == -1:
                break
            # Run a eviction pass to remove tensors from device
            # This pass only evicts tensors for a single ttnn op which overflows the SRAM
            # Multiple overflows require multiple run of this pass

            mem_pass = MemoryPass(option.verbose)
            passes = [
                EvictionPass(option.memory_manager, guilty_op, tensors_to_evict),
                GraphvizPass(f"eviction-pass-{nth_eviction}"),
                mem_pass,
            ]
            pm = PassManager(passes=passes)
            gm, modified = pm(gm)

            gm.graph.lint()
            gm.recompile()

            # Get the memory manager object for memory analysis
            option.memory_manager = mem_pass.mm
            nth_eviction += 1

    if option.metrics_path:
        option.compiled_schema_list.extend(metrics.collect_input_variations_from_list_nodes(gm.graph.nodes))

    option._out_fx_graphs.append(gm.graph)
    if options.export_code:
        option._ttnn_fx_graphs[-1].append(gm.graph)

    for node in gm.graph.nodes:
        if node.op == "placeholder":
            print(f"{node.name}: {node.meta}")

    for number, line in enumerate(gm.code.splitlines()):
        print(f"{number + 1}: {line}")

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
    if options.export_code:
        import tools.export_code as export_code

        # Some models have multiple forward functions with separate inputs for each.
        # Within these forward functions, there can be graph breakages which are
        # also represented by separate forward functions, but these do not have their
        # own separate inputs. Therefore, we organize the list of aten/ttnn graphs
        # with sublists where the top level list corresponds to the respective list of inputs.
        options._aten_fx_graphs.append(list())
        options._ttnn_fx_graphs.append(list())
        options._all_inputs.append(export_code.generate_flat_args(gm, example_inputs))

    # Analysis of params, buffers, and args
    options._n_parameters = len(list(gm.parameters()))
    options._n_buffers = len(list(gm.buffers()))
    options._n_arguments = len(example_inputs)

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
