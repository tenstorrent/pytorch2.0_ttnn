# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import inspect
import itertools
import logging
import lzma
import pickle
import torch.utils._pytree as pytree
import ttnn
import torch
import types

from collections import defaultdict
from pathlib import Path
from tests.utils import assert_with_pcc, comp_pcc, construct_pcc_assert_message
from torch.fx.node import Node, map_arg
from torch_ttnn.utils import (
    get_opname,
    users_have_getitem,
    is_operation,
    get_node_name,
    get_output_nodes,
    get_input_nodes,
)
from typing import NamedTuple

wrapper_funcs = set()
wrapper_alias = set()

export_code_options = [
    "accuracy",  # Test accuracy between Aten and corresponding TTNN ops
    "profiling",  # Generate tracy-compatible code for profiling purposes
]


def _get_indent(tabs=1, tabstop=4):
    """
    Get indentation in spaces given the number of tabs

    Args:
        tabs (int): Number of tabs
        tabstop (int): Number of spaces per tab

    Returns:
        str: Reformatted string with indentation
    """
    spaces = " " * tabstop
    return spaces * tabs


"""
The first clone of an argument maps to the last primal of the previous output.
Use _get_first_clone_node(arg_list) to get the first clone node in the argument list.
Then match that with the last primal in the outputs using _match_last_primal_with_clone_node

Example:
def forward_1(...):
    ...
    return [out1, out2, out3, primals_1, primals_2, primals_3, out4, out5]

def forward_2(..., clone):
    %clone = placeholder(clone)  <==>  same as primals_3, replace uses of clone with primals_3
"""


def _get_first_clone_node(node_list):
    """
    Get first node starting with "clone" from the node_list.
    node_list can be a list of strings or list of fx.Nodes
    """
    for node in node_list:
        if get_node_name(node).startswith("clone"):
            return node
    return None


def _match_last_primal_with_clone_node(outputs, node):
    """
    Match a clone node with the last output primal.
    """
    if get_node_name(node).startswith("clone"):
        for out_arg in reversed(outputs):
            if get_node_name(out_arg).startswith("primals"):
                return out_arg
    return None


def _rename_arguments_and_tangents(arg_node_names, tangents):
    """
    Returns a tuple of modified argument node names and assignment of tangents to the correct output
    See comment below for more details.

    Args:
        arg_node_names (List[str]): List of argument names for the current forward function
        tangents (List[TangentsInfo]): List of TangentsInfo objects

    Returns:
        (List[str], List[str]):
            List of strings for renamed arguments in the format of {arg_name}_{chunk_idx}_{graph_idx}
            List of strings for assignment of tangents to the corresponding output, i.e. tangents = output
    """

    """
    Potential tangents are a consecutive list of nodes before the first primal.

    Given the following forward call:
    mul_1, ge, sigmoid, exp, div, cat, mm_2, primals_4, primals_7, primals_8, ... = forward_0_0(...)

    Potential tangents = [mul_1, ge, sigmoid, exp, div, cat, mm_2] (len = 7)
                  mask = [True, False, True, True, True, True, True] (len = 7)
       output tangents = [mul_1, sigmoid, exp, div, cat, mm_2] (len = 6)

    Upcoming function with tangents passed as arguments:
    ... = forward_1_1(primals_4, primals_7, primals_8, ..., tangents_1, tangents_2, tangents_3, tangents_4, tangents_5, tangents_6)

    Match the most recent set of output tangents with input tangents.

    tangents_1 = mul_1
    tangents_2 = sigmoid
    tangents_3 = exp
    tangents_4 = div
    tangents_5 = cat
    tangents_6 = mm_2

    For output lists that have tangents, rename the other outputs from the same list, i.e. primals_4, primals_7, primals_8, ... since
    they will be passed together to the same forward function. Use the chunk_idx and graph_idx from TangentsInfo to append the correct suffix.

    The correct tangents originated from 0_0 forward graph. Append to other outputs:
    ... = forward_1_1(primals_4_0_0, primals_7_0_0, primals_8_0_0, ..., tangents_1, tangents_2, tangents_3, tangents_4, tangents_5, tangents_6)

    Note: These outputs are renamed separately in _rename_outputs. This function only renames the argument list.

    """

    input_tangents = []
    renamed_tangents = []
    for arg in arg_node_names:
        if get_node_name(arg).startswith("tangents"):
            input_tangents.append(arg)
    # map backwards, from the most recent tangents list
    new_args = []
    # first clone if it exists
    first_clone = _get_first_clone_node(arg_node_names)

    for tan_info in reversed(tangents):
        if len(tan_info.tangents) == len(input_tangents):
            suffix = f"{tan_info.chunk_idx}_{tan_info.graph_idx}"
            for arg in arg_node_names:
                if not arg.startswith("tangents") and arg != first_clone:
                    new_args.append(f"{arg}_{suffix}")
                else:
                    new_args.append(arg)
            for a, b in zip(input_tangents, tan_info.tangents):
                renamed_tangents.append(f"{a} = {b}_{suffix}")
            break
    if not new_args:
        new_args = arg_node_names

    return new_args, renamed_tangents


def _rename_outputs(output_nodes, chunk_idx, graph_idx):
    """
    Rename outputs that have tangents

    Outputs that are labeled as tangents will be reused later, but not necessarily the graph directly
    after. In addition, the remaining outputs from the same list will be passed together. Outputs
    also tend to have the same names, so to prevent overwrite, we rename them according to the
    chunk_idx and graph_idx of the graph from which they originate.

    Args:
        output_nodes (List[torch.fx.Node]): List of output nodes for one forward graph
        chunk_idx (int): chunk index of the corresponding forward graph
        graph_idx (int): for each chunk, the graph index of the forward graph

    Returns:
        List[str]: Renamed outputs, in the form of {output_name}_{chunk_idx}_{graph_idx}
    """
    rename_all_outputs = False
    out_node_names = []
    # Find if a tangent exists first
    for outp in output_nodes:
        if outp is not None and (tan := outp.meta.get("tangents", None)) is not None and tan:
            rename_all_outputs = True
            break

    # Then rename outputs accordingly
    for outp in output_nodes:
        outp_name = get_node_name(outp)
        if rename_all_outputs:
            out_node_names.append(f"{outp_name}_{chunk_idx}_{graph_idx}")
        else:
            out_node_names.append(outp_name if outp_name else "_")

    return out_node_names


def _compute_key(node):
    """
    Return string that is unique to the aten op in order to map to the lowered set
    of ttnn ops correctly.
    """
    if "tensor_meta" in node.meta:
        tensor_meta = node.meta["tensor_meta"]
    elif "val" in node.meta:
        tensor_meta = node.meta["val"]
        # Workaround for ttnn.layer_norm
        if node.target == ttnn.layer_norm:
            tensor_meta = node.meta["val"][0]
    else:
        tensor_meta = ""
    return str(node.meta["seq_nr"]) + node.meta["original_aten"]._name + str(tensor_meta)


def _map_aten_to_ttnn_ops(ttnn_graph, aten_name_to_node_map, clone_nodes):
    """
    Map all aten ops to ttnn ops. This is in a 1 aten op to many ttnn ops
    mapping. This is done by comparing the metadata in the aten op to the
    that of the ttnn op. Some intermediate nodes that have different meta-
    data will be skipped. This is fine because we only care about the very
    last node of the set of ttnn ops.
    """
    aten_to_ttnn_map = defaultdict(list)
    # Get first clone node if found
    first_clone = _get_first_clone_node(get_input_nodes(ttnn_graph))

    for node in ttnn_graph.nodes:
        if node.op == "placeholder":
            # Handle special case for the first clone node
            if node == first_clone and first_clone in clone_nodes:
                node.replace_all_uses_with(
                    clone_nodes[first_clone], delete_user_cb=lambda node: node != clone_nodes[first_clone]
                )
            continue

        if node.op != "output":
            # ignore to_torch
            if node.target == ttnn.to_torch:
                continue
            if "seq_nr" in node.meta:
                aten_node_name = _compute_key(node)
                # If a key is not in the map, then ignore. This is usually an intermediate
                # node from a decomposition, and we do not not compare this.
                if aten_node := aten_name_to_node_map[aten_node_name]:
                    aten_to_ttnn_map[aten_node].append(node)

    return aten_to_ttnn_map


def _process_ttnn_ops(ttnn_graph, aten_name_to_node_map, aten_to_ttnn_map):
    """
    Organize ttnn ops into a sequential list while inserting tuples in between.
    These tuples should contain a pair, (output of aten node, output of ttnn node).
    These outputs will be compared against each other during the accuracy test.
    """
    ttnn_all_nodes = []
    for node in ttnn_graph.nodes:
        if node.op == "placeholder":
            continue

        ttnn_all_nodes.append(node)

        # check the node pair to compare against each other
        if "seq_nr" in node.meta:
            aten_node_name = _compute_key(node)
            # If a key is not in the map, then ignore. This is usually an intermediate
            # node from a decomposition, and we do not not compare this.
            if aten_node := aten_name_to_node_map[aten_node_name]:
                # this is the last ttnn node for this aten op, compare the output of this
                if node == aten_to_ttnn_map[aten_node][-1]:
                    # this will be converted to check_accuracy(node1, node2) later
                    # do not emit if users are getitem
                    if not users_have_getitem(node):
                        if (getitem := users_have_getitem(aten_node)) is not None:
                            aten_node = getitem
                        ttnn_all_nodes.append((aten_node, node))
    return ttnn_all_nodes


def _format_dict(obj):
    """
    Format a dictionary to string with {"keys" = "values"}
    """
    to_kwargs = []
    # handle some cases where str(torch.device) has no quotes
    for k, v in obj.items():
        if (k == "device" and isinstance(v, torch.device)) or isinstance(v, str):
            v = f'"{v}"'
        to_kwargs.append(f"{k} = {v}")
    return ", ".join(to_kwargs)


def _node_to_python_code(node):
    """
    Convert a node to a function call statement.
    """
    # assume no placeholder
    assert node.op != "placeholder"

    if node.op == "output":
        return f"return {node.args[0]}"

    # handle get_attr nodes
    if node.op == "get_attr":
        # Embed get_attr constant into code
        tensor_data = getattr(node.graph.owning_module, node.target).data
        # printoptions needed to display entirety of large tensor
        torch.set_printoptions(profile="full")
        tensor_str = (
            f"torch.{str(tensor_data)}"
            if isinstance(tensor_data, torch.Tensor)
            else f"torch.tensor({str(tensor_data)})"
        )
        torch.set_printoptions(profile="default")
        statement = f"{node} = {tensor_str}"
        return statement

    # handle getitem nodes
    if node.target.__name__ == "getitem":
        return f"{node} = {node.args[0]}[{node.args[1]}]"

    # handle wrapper functions
    opname = get_opname(node)
    if (
        not opname.startswith("aten.")
        and not opname.startswith("ttnn.")
        and not isinstance(node.target, types.BuiltinFunctionType)
    ):
        lines = inspect.getsource(node.target)
        wrapper_funcs.add(lines)
        # remove target_wrapper prefix to match function name
        wrapper_alias.add(opname.replace("target_wrapper_", ""))

    # function to process special args
    def process_arg(arg):
        # some args can be string literals, add quotes to them
        if isinstance(arg, str):
            return f'"{arg}"'
        else:
            return arg

    # find a better way to use registered custom builtins to replace TTNN constants
    node_args = ", ".join([str(process_arg(arg)) for arg in node.args])
    statement = f"{node} = {opname}({node_args}, {_format_dict(node.kwargs)})"
    replace_map = {
        "ttnn_Specified_Device": "device",
        "ttnn_TILE_LAYOUT": "ttnn.TILE_LAYOUT",
        "ttnn_ROW_MAJOR_LAYOUT": "ttnn.ROW_MAJOR_LAYOUT",
        "ttnn_L1_MEMORY_CONFIG": "ttnn.L1_MEMORY_CONFIG",
        "ttnn_DRAM_MEMORY_CONFIG": "ttnn.DRAM_MEMORY_CONFIG",
        "ttnn_uint32": "ttnn.uint32",
        "ttnn_bfloat16": "ttnn.bfloat16",
    }

    for k, v in replace_map.items():
        statement = statement.replace(k, v)
    return statement


def _build_code_from_aten_ttnn_graphs(
    aten_graph, ttnn_graph, output_nodes, torch_ttnn_option, chunk_idx, graph_idx, clone_nodes
):
    """
    Given a pair of aten and ttnn graphs, build a list of lines of code.

    Args:
        aten_graph (torch.fx.graph.Graph): Unmodified aten graph
        ttnn_graph (torch.fx.graph.Graph): Modified ttnn graph.
        output_nodes (List[tuple(torch.fx.Node])):
            List of output tuple of nodes used to track graph breakage.
            The final code will be one fused function.
        torch_ttnn_option (TorchTtnnOption): options containing various useful attributes
        chunk_idx (int): Index to the top level list of aten/ttnn graphs
        graph_idx (int): Index to the sublist of graphs

    Returns:
        List[str]: List of lines of code
    """

    """
    Rename nodes with names that do not change after graph transformation.
    Aten and ttnn nodes were renamed automatically during lowering. Nodes from
    getitem and wrappers do not.
    """
    for node in ttnn_graph.nodes:
        if is_operation(node) and node.op != "get_attr":
            opname = get_opname(node)
            if not opname.startswith("aten.") and not opname.startswith("ttnn."):
                node._rename(f"ttnn_prefix_{node.name}")

    """
    Gather together all the aten nodes and argument (placeholder) nodes into one list.
    Rename some input arguments to match names due to graph breakage. 
    """
    aten_all_nodes = []
    arg_nodes = []
    for node in aten_graph.nodes:
        if node.op == "placeholder":
            arg_nodes.append(node)
            continue
        aten_all_nodes.append(node)

    """
    Maps selected metadata from `compute_key` to the aten node
    """
    aten_name_to_node_map = defaultdict(list)
    for node in aten_graph.nodes:
        if is_operation(node):
            aten_name_to_node_map[_compute_key(node)] = node

    """
    Now map all aten ops to ttnn ops.
    """
    aten_to_ttnn_map = _map_aten_to_ttnn_ops(ttnn_graph, aten_name_to_node_map, clone_nodes)

    """
    Gather all ttnn ops into one list. Use `aten_to_ttnn_map` to determine where to insert
    the check_accuracy functions. 
    """
    ttnn_all_nodes = _process_ttnn_ops(ttnn_graph, aten_name_to_node_map, aten_to_ttnn_map)

    """
    Finally convert interleaved nodes to python code for this graph
    """
    arg_node_names = [node.name for node in arg_nodes]
    arg_node_names.append("device")

    forward_func_name = f"forward_{chunk_idx}_{graph_idx}"
    forward_signature = f"def {forward_func_name}({', '.join(arg_node_names)}):"
    # comment out signature if not the first graph
    graph_code = [forward_signature]

    # Assume export_code parent function has checked for validity
    option = torch_ttnn_option.export_code
    # Only emit original aten nodes for the accuracy option
    if option == "accuracy":
        for node in aten_all_nodes:
            if node.op == "output":
                aten_out_list = node.args[0]
                output_nodes.append(aten_out_list)
                # comment out aten return for referencing purposes
                graph_code.append(_get_indent(1) + f"# return {aten_out_list}")
                graph_code.append(_get_indent(1) + f"aten_outputs = {aten_out_list}")
                continue
            else:
                graph_code.append(_get_indent(1) + f"{_node_to_python_code(node)}")

    for i, node in enumerate(ttnn_all_nodes):
        if option == "profiling" and i % 500 == 0:
            graph_code.append(_get_indent(1) + f"ttnn.DumpDeviceProfiler(device)")

        if isinstance(node, tuple):
            if option == "accuracy":
                graph_code.append(_get_indent(1) + f"check_accuracy({node[0]}, {node[1]})")
        else:
            # Print the accuracy of the outputs for this forward function
            if node.op == "output" and option == "accuracy":
                graph_code.append(_get_indent(1) + f"ttnn_outputs = {node.args[0]}")
                graph_code.append(
                    _get_indent(1)
                    + "accuracy = np.mean([comp_pcc_wrapper(a, t) for a, t in zip(aten_outputs, ttnn_outputs)])"
                )
                graph_code.append(_get_indent(1) + f'print(f"{forward_func_name} accuracy: {{accuracy}}")')

            graph_code.append(_get_indent(1) + f"{_node_to_python_code(node)}")

    return graph_code


def _reformat_inputs(all_inputs):
    """
    Some inputs are in special formats (e.g. SymInts) that need to be reformatted to hold
    static values. Otherwise, the data cannot be exported.

    Args:
        all_inputs (List[List[]]): Lists of lists

    Returns:
        Reformatted list of inputs
    """

    for inputs in all_inputs:
        for i, inpt in enumerate(inputs):
            if isinstance(inpt, torch.SymInt):
                assert inpt.node.has_hint()
                inputs[i] = torch.tensor(inpt.node.hint)

    return all_inputs


def generate_flat_args(gm, example_inputs):
    """
    Combines weights, biases, and dynamic inputs into a list. This should be
    called during lowering when the GraphModule (gm) has been lowered to aten.

    Args:
        gm (torch.fx.GraphModule): aten GraphModule
        example_inputs (List[]): Dynamic inputs for the aten GraphModule

    Returns:
        Combined list of all the input data
    """
    full_args = []
    # based off torch/_functorch/aot_autograd.py::aot_module_simplified
    params = {
        **dict(gm.named_parameters(remove_duplicate=False)),
        **dict(gm.named_buffers(remove_duplicate=False)),
    }
    params_flat, params_spec = pytree.tree_flatten(params)
    params_flat = list(params_flat)
    full_args.extend(params_flat)
    full_args.extend(example_inputs)

    return full_args


def _save_to_disk(model_name, forward_codes, call_forwards_in_main, all_inputs, torch_ttnn_option):
    """
    Generate standlone a python script along with an input file containing
    data for weights, biases, and inputs for a model run.

    Args:
        model_name (str): The name of the model used for filename purposes.
        forward_codes (List[str]): List of lines of code.
        call_forwards_in_main (List[str]): List of lines of code.
        all_inputs (List[List]): List of list of inputs including weights, biases, and dynamic data.
        torch_ttnn_option (TorchTtnnOption): options containing various useful attributes

    Returns:
        None.
    """

    # Assume export_code parent function has checked for validity
    option = torch_ttnn_option.export_code
    check_accuracy_graph_codes = [elem for sublist in forward_codes for elem in sublist]

    # List of modules
    import_code = [
        "import lzma",
        "import numpy as np",
        "import pickle",
        "import torch",
        "import ttnn",
        "from pathlib import Path",
        "from typing import Dict",
    ]
    import_code += (
        ["from ttnn import TensorToMesh, MeshToTensor, MeshDevice"] if torch_ttnn_option.data_parallel else []
    )
    import_code += (
        [
            "from tracy import Profiler",
            "from tracy import signpost",
        ]
        if option == "profiling"
        else []
    )

    # List of aliases and globals
    alias_code = [
        "aten = torch.ops.aten",
        'inf = float("inf")',
    ]

    # Handle additional requirements for run_once
    if torch_ttnn_option.load_params_once:
        alias_code.append("run_once_count = 0")
        alias_code.append("run_once_ans = tuple()")
        from torch_ttnn.passes.lowering.target_wrappers import conv, move_to_host

        wrapper_funcs.add(inspect.getsource(conv))
        wrapper_funcs.add(inspect.getsource(move_to_host))

    # Definitions of wrapper functions
    wrapper_code = []
    for func in wrapper_funcs:
        func_lines = func.split("\n")
        # Remove decorators
        for i, line in enumerate(func_lines):
            if line.lstrip().startswith("def "):
                break
            if line.lstrip().startswith("@"):
                func_lines[i] = ""
        wrapper_code.append("\n".join(func_lines))

    # Additional alias for wrapper functions to avoid aten naming conflicts
    wrapper_alias_code = []
    for fn in wrapper_alias:
        assign = f"target_wrapper_{fn} = {fn}"
        wrapper_alias_code.append(assign)

    # pcc functions
    pcc_funcs = (
        [
            inspect.getsource(comp_pcc),
            inspect.getsource(construct_pcc_assert_message),
            inspect.getsource(assert_with_pcc),
        ]
        if option == "accuracy"
        else []
    )

    # Lazy import to avoid circular imports
    from tests import conftest as tests_conftest

    get_dispatch_core_type = tests_conftest.get_dispatch_core_type
    get_dispatch_core_axis = tests_conftest.get_dispatch_core_axis
    get_dispatch_core_config = tests_conftest.get_dispatch_core_config

    device_funcs = [
        inspect.getsource(get_dispatch_core_type),
        inspect.getsource(get_dispatch_core_axis),
        inspect.getsource(get_dispatch_core_config),
    ]

    # check_accuracy helper function definition
    check_accuracy_code = (
        """
def check_accuracy(expected, actual):
    if expected is None and actual is None:
        return
    if isinstance(actual, ttnn.Tensor):
        actual = ttnn.to_torch(actual)
    assert_with_pcc(expected, actual, pcc = 0.90)

def comp_pcc_wrapper(expected, actual):
    if expected is None and actual is None:
        return 1.0
    assert isinstance(expected, torch.Tensor)
    assert isinstance(actual, torch.Tensor)
    _, pcc = comp_pcc(expected, actual)
    return pcc
"""
        if option == "accuracy"
        else ""
    )

    # main function definition

    # process each line of the forward calls with appropriate indentation
    def format_forward_calls(call_forwards_in_main, indents=""):
        forward_calls_joined = [indents + line for line in call_forwards_in_main]
        forward_calls_joined = "\n".join(forward_calls_joined)
        return forward_calls_joined

    total_num_iterations = torch_ttnn_option.total_num_iterations
    if option == "profiling":
        forward_calls_joined = f"""
    profiler = Profiler()
    for i in range({total_num_iterations}):
        if i == 0 or i == {total_num_iterations - 1}:
            # We want to profile the first and the last one,
            # so we measure without cache and with cache
            profiler.enable()
        signpost(header=f"Run number {{i}}")
{format_forward_calls(call_forwards_in_main, _get_indent(2))}
        signpost(header="Run result post proc")
        profiler.disable()
"""
    else:
        forward_calls_joined = format_forward_calls(call_forwards_in_main, _get_indent(1))

    # TODO: Find a more dynamic way to copy device initialization from conftest.py
    if torch_ttnn_option.data_parallel:
        # Support mesh device
        open_device = [
            "device = ttnn.open_mesh_device(ttnn.MeshShape(1, 2), dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size)"
        ]
        close_device = "ttnn.close_mesh_device(device)"
    else:
        open_device = [
            "device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size)",
            "ttnn.SetDefaultDevice(device)",
        ]
        close_device = "ttnn.close_device(device)"
    open_device = "\n".join(f"{_get_indent(1)}{i}" for i in open_device)
    close_device = _get_indent(1) + close_device

    directory = Path("tests/export_code") / Path(option)
    input_pkl_file = Path(f"{model_name}_inputs.pickle")
    full_input_pkl_path = directory / input_pkl_file
    full_input_pkl_path.parent.mkdir(parents=True, exist_ok=True)
    main_code = f"""
if __name__ == "__main__":
    filepath = Path(__file__).with_name("{input_pkl_file.name}")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    l1_small_size = 16384
    dispatch_core_config = get_dispatch_core_config()
{open_device}
    device.enable_program_cache()
{forward_calls_joined}
    ttnn.synchronize_device(device)
{close_device}
"""

    # Assemble all of pieces of code into one script
    full_code = (
        import_code
        + alias_code
        + wrapper_code
        + wrapper_alias_code
        + pcc_funcs
        + device_funcs
        + [check_accuracy_code]
        + check_accuracy_graph_codes
        + [main_code]
    )
    full_text = "\n".join(full_code)

    code_full_path = directory / Path(f"{model_name}_code.py")
    with open(code_full_path, "w") as text_file:
        print(full_text, file=text_file)
        logging.info(f"{option} test code saved to {code_full_path}.")

    all_inputs = _reformat_inputs(all_inputs)
    data_full_path = directory / Path(f"{model_name}_inputs.pickle")
    with lzma.open(data_full_path, "wb") as f:
        pickle.dump(all_inputs, f)
        logging.info(f"{option} data object saved to {data_full_path}.")


def _assemble_forward_functions(
    aten_fx_graphs, ttnn_fx_graphs, inputs, torch_ttnn_option, chunk_idx, tangents_info, clone_nodes
):
    """
    Take all the graphs and assemble into a list of

    Args:
        aten_fx_graphs (List[torch.fx.graph.Graph]): List of unmodified aten graphs.
        ttnn_fx_graphs (List[torch.fx.graph.Graph]): List of modified ttnn graphs.
        inputs (List[]): List of inputs including weights, biases, and dynamic data.
        verbose (boolean): Print out additional info.
        torch_ttnn_option (TorchTtnnOption): object containing other useful attributes
        chunk_idx: index of the top level list of aten/ttnn graphs

    Returns:
        (List[str], List[str]): List of forward definitions, list of forward call in main
    """

    # Assume export_code parent function has checked for validity
    option = torch_ttnn_option.export_code

    call_forwards_in_main = []

    # Map input arg names of first forward graph to inputs.
    def get_names_of_args(graph):
        arg_nodes = []
        for node in graph.nodes:
            if node.op == "placeholder":
                arg_nodes.append(node)
        arg_node_names = [node.name for node in arg_nodes]
        return arg_node_names

    def get_names_of_outputs(graph):
        out_nodes = get_output_nodes(graph)
        out_node_names = [node.name if node is not None else "_" for node in out_nodes]
        return out_node_names

    for graph_idx, aten_graph in enumerate(aten_fx_graphs):
        call_forwards_in_main.append(f"# start: chunk_idx: {chunk_idx} graph_idx: {graph_idx}")

        # Process arguments
        arg_node_names = get_names_of_args(aten_graph)

        if graph_idx == 0:
            assert len(arg_node_names) == len(inputs)
            # Map indices
            for i, arg in enumerate(arg_node_names):
                call_forwards_in_main.append(f"{arg} = inputs[{chunk_idx}][{i}]")
        else:
            # In some cases where there are graph breakages, outputs of the previous graphs
            # can become inputs for subsequent graphs. Some are given new names based on
            # some pattern. The following renames some of these nodes.
            # Find the first clone if available
            first_clone = _get_first_clone_node(get_input_nodes(aten_graph))
            if first_clone in clone_nodes:
                call_forwards_in_main.append(f"{first_clone} = {clone_nodes[first_clone]}")

        # process tangents separately
        arg_node_names, renamed_tangents = _rename_arguments_and_tangents(arg_node_names, tangents_info)
        for i in renamed_tangents:
            call_forwards_in_main.append(i)

        # append device to the end of arg list
        arg_node_names.append("device")
        # Call the forward function
        out_node_names = _rename_outputs(get_output_nodes(aten_graph), chunk_idx, graph_idx)
        out_nodes_string = f"{', '.join(out_node_names)} = " if out_node_names else ""
        call_forwards_in_main.append(f"{out_nodes_string}forward_{chunk_idx}_{graph_idx}({', '.join(arg_node_names)})")

    assert len(aten_fx_graphs) == len(ttnn_fx_graphs)

    # Contains a list of each forward graph
    forward_code = []
    # Tracks the output nodes for models with graph breakages
    output_nodes = []
    for graph_idx, (aten_graph, ttnn_graph) in enumerate(zip(aten_fx_graphs, ttnn_fx_graphs)):
        graph_code = _build_code_from_aten_ttnn_graphs(
            aten_graph, ttnn_graph, output_nodes, torch_ttnn_option, chunk_idx, graph_idx, clone_nodes
        )
        if option == "profiling":
            # Insert last one before return
            graph_code.insert(-1, _get_indent(1) + f"ttnn.DumpDeviceProfiler(device)")
        forward_code.append(graph_code)

    return forward_code, call_forwards_in_main


class TangentsInfo(NamedTuple):
    # Organize the list of tangents and from which graph they originated
    chunk_idx: int
    graph_idx: int
    tangents: list


def _collect_tangents(aten_fx_graphs):
    """
    Collects lists of tangents into a TangentsInfo object.

    Args:
        aten_fx_graphs: List of aten graphs
    Returns:
        List[TangentsInfo]: List TangentsInfo objects
    """
    tangents_info = []

    for chunk_idx, aten_fx_graphs_chunk in enumerate(aten_fx_graphs):
        for graph_idx, aten_graph in enumerate(aten_fx_graphs_chunk):
            # For every output in each graph, locate the nodes marked as tangents.
            # Save them in the respective order along with graph id information.
            outputs = get_output_nodes(aten_graph)
            tangents_list = []
            # If there are no primal nodes, there are also no tangents. We can prepend nodes in advance.
            # Retrieve the "tangents" metadata value and save the nodes that have True.
            # The chunk_idx and graph_idx are also saved because we need the origin of this forward function.
            # These tangents and other outputs from the same list should be used together in future forward functions.
            first_primal_idx = 0
            for i, outp in enumerate(outputs):
                if get_node_name(outp).startswith("primals"):
                    first_primal_idx = i
                    break

            tangents_list = []
            if first_primal_idx > 0:
                for outp in reversed(outputs[0:first_primal_idx]):
                    if outp is not None and (tan := outp.meta.get("tangents", None)) is not None:
                        if tan:
                            tangents_list.append(get_node_name(outp))
                    else:
                        break
                tangents_list.reverse()
                tangents_info.append(TangentsInfo(chunk_idx, graph_idx, tangents_list))

    return tangents_info


def _collect_matching_primals_from_clones(aten_fx_graphs):
    """
    Collect all last primals from outputs and match them with clone nodes if applicable.
    """
    flatten_list = list(itertools.chain.from_iterable(aten_fx_graphs))

    primals = [None] * len(flatten_list)
    clones = [None] * len(flatten_list)
    for idx, aten_graph in enumerate(flatten_list):
        # get last primal from outputs
        outputs = get_output_nodes(aten_graph)
        for outp in reversed(outputs):
            if outp is not None and outp.name.startswith("primal"):
                primals[idx] = outp
                break

        # get first clone in inputs
        inputs = get_input_nodes(aten_graph)
        for inp in inputs:
            if inp.name.startswith("clone"):
                clones[idx] = inp
                break

    primals_from_clones = {}
    # for each clone, search backwards from the same position
    # i.e. match the clone with the previous primal
    for idx, clone in enumerate(clones):
        if clone is not None:
            for primal in reversed(primals[0:idx]):
                if primal is not None:
                    primals_from_clones[clone] = primal
                    break

    return primals_from_clones


def export_code(torch_ttnn_option):
    """
    Main entry to generate standalone python script with accuracy checks

    Args:
        torch_ttnn_option (TorchTtnnOption): object that holds model_name, aten_fx_graphs, ttnn_fx_graphs, all_inputs, and export_code options
    Returns:
        None.
    """

    # This will not do anything if export_code is not set to something valid
    option = torch_ttnn_option.export_code
    if option is None:
        return
    else:
        assert option in export_code_options

    model_name = torch_ttnn_option.metrics_path  # str: Use the same name for metrics
    aten_fx_graphs = torch_ttnn_option._aten_fx_graphs  # List[List[torch.fx.graph.Graph]]
    ttnn_fx_graphs = torch_ttnn_option._ttnn_fx_graphs  # List[List[torch.fx.graph.Graph]]
    all_inputs = torch_ttnn_option._all_inputs  # List[List]

    # Flatten the nested lists above to lists of definitions and calls
    # Top level contains one input list per group(list) of forward functions

    # list of forward definitions
    forward_code_list = []
    # list of calls to forward functions inside main()
    call_forwards_in_main_list = []

    assert len(aten_fx_graphs) == len(all_inputs)
    tangents_info = _collect_tangents(aten_fx_graphs)
    clone_nodes = _collect_matching_primals_from_clones(aten_fx_graphs)
    for chunk_idx, (aten_fx_graphs_chunk, ttnn_fx_graphs_chunk, inputs) in enumerate(
        zip(aten_fx_graphs, ttnn_fx_graphs, all_inputs)
    ):
        forward_code, call_forwards_in_main = _assemble_forward_functions(
            aten_fx_graphs_chunk, ttnn_fx_graphs_chunk, inputs, torch_ttnn_option, chunk_idx, tangents_info, clone_nodes
        )
        forward_code_list.extend(forward_code)
        call_forwards_in_main_list.extend(call_forwards_in_main)

    _save_to_disk(model_name, forward_code_list, call_forwards_in_main_list, all_inputs, torch_ttnn_option)
