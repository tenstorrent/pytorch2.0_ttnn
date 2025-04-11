# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import inspect
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
from torch_ttnn.utils import get_opname, users_have_getitem, is_operation

wrapper_funcs = set()
rename_wrappers = set()

export_code_options = [
    "accuracy",  # Test accuracy between Aten and corresponding TTNN ops
    "profiling",  # Generate tracy-compatible code for profiling purposes
]


def _rename_input_args_from_graph_break(output_nodes, node):
    """
    When graph breaks occur, usually due to control flow, PyTorch keeps the names
    of the nodes consistent between graphs. For example, in the following example,
    add_1 was not an output, but treated still treated as an input to the follow-up
    graph.
    def forward_1(arg0, arg1, arg2):
        %add_1 = aten.add(...)
        %add_2 = aten.add(...)
        return [add_2]
    def forward_2(arg0, arg1, arg2, add_1):
        ...

    However, some nodes that are outputs are renamed despite being the same. This function
    attempts to rename them back so that graphs can be fused into one. This is where
    output_nodes will be used to keep track of these nodes.
    """

    """
    For nodes named "clone", this is the same as the last primal in the tuple of outputs
    from the previous graph.
    Example:
    def forward_1(...):
        ...
        return [out1, out2, out3, primals_1, primals_2, primals_3, out4, out5]

    def forward_2(..., clone):
        %clone = placeholder(clone)  <==>  same as primals_3, replace uses of clone with primals_3

    """
    if node.name == "clone":
        for out_arg in reversed(output_nodes[-1]):
            if out_arg.name.startswith("primals"):
                node.replace_all_uses_with(out_arg, delete_user_cb=lambda node: node != out_arg)
                break

    """
    For nodes that start with "tangents", this is the same as the node before the first primal
    from the outputs.
    Example:
    def forward_1(...):
        ...
        return [out1, out2, out3, primals_1, primals_2, primals_3, out4, out5]

    def forward_2(..., tangents_1):
        %tangents_1 = placeholder(tangents_1)  <==>  same as out3, replace uses of tangents_1 with out3
    """
    if node.name.startswith("tangents"):
        first_primal_idx = 0
        for i, out_arg in enumerate(output_nodes[-1]):
            if out_arg.name.startswith("primals"):
                first_primal_idx = i
                break
        tangent_node = output_nodes[-1][first_primal_idx - 1]
        node.replace_all_uses_with(tangent_node, delete_user_cb=lambda node: node != tangent_node)


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


def _map_aten_to_ttnn_ops(ttnn_graph, aten_name_to_node_map, output_nodes):
    """
    Map all aten ops to ttnn ops. This is in a 1 aten op to many ttnn ops
    mapping. This is done by comparing the metadata in the aten op to the
    that of the ttnn op. Some intermediate nodes that have different meta-
    data will be skipped. This is fine because we only care about the very
    last node of the set of ttnn ops.
    """
    aten_to_ttnn_map = defaultdict(list)
    for node in ttnn_graph.nodes:
        if node.op == "placeholder":
            _rename_input_args_from_graph_break(output_nodes, node)
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
        # if not is_operation(node):
        #     continue

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
        if k == "device" and isinstance(v, torch.device):
            v = f'"{v}"'
        to_kwargs.append(f"{k} = {v}")
    return ", ".join(to_kwargs)


def _node_to_python_code(node):
    """
    Convert a node to a function call statement.
    """
    # assume no placeholder and output
    assert node.op != "placeholder"
    # assert is_operation(node)

    if node.op == "output":
        return f"return {node.args[0]}"

    # handle get_attr nodes
    if node.op == "get_attr":
        # Embed get_attr constant into code
        tensor_data = getattr(node.graph.owning_module, node.target).data
        torch.set_printoptions(profile="full")
        tensor_str = f"torch.{tensor_data}" if isinstance(tensor_data, torch.Tensor) else f"torch.tensor({tensor_data})"
        statement = f"{node} = {tensor_str}"
        torch.set_printoptions(profile="default")
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
        # rename functions to avoid naming conflict
        func_name = node.target.__name__
        rename_func = f"""
ref = globals()["{func_name}"]
globals()["{func_name}_wrapper"] = ref
del globals()["{func_name}"]
"""
        rename_wrappers.add(rename_func)
        opname += "_wrapper"

    # find a better way to use registered custom builtins to replace TTNN constants
    node_args = ", ".join([str(arg) for arg in node.args])
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


def _build_code_from_aten_ttnn_graphs(aten_graph, ttnn_graph, output_nodes, torch_ttnn_option, chunk_idx, graph_idx):
    """
    Given a pair of aten and ttnn graphs, build a list of lines of code.

    Args:
        aten_graph (torch.fx.graph.Graph): Unmodified aten graph
        ttnn_graph (torch.fx.graph.Graph): Modified ttnn graph.
        output_nodes (List[tuple(torch.fx.Node])):
            List of output tuple of nodes used to track graph breakage.
            The final code will be one fused function.

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
            # _rename_input_args_from_graph_break(output_nodes, node)
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
    aten_to_ttnn_map = _map_aten_to_ttnn_ops(ttnn_graph, aten_name_to_node_map, output_nodes)

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

    # Only emit original aten nodes for accuracy
    option = torch_ttnn_option.export_code
    if option == "accuracy":
        for node in aten_all_nodes:
            if node.op == "output":
                aten_out_list = node.args[0]
                output_nodes.append(aten_out_list)
                # comment out aten return for referencing purposes
                graph_code.append(f"    # return {aten_out_list}")
                graph_code.append(f"    aten_outputs = {aten_out_list}")
                continue
            else:
                graph_code.append(f"    {_node_to_python_code(node)}")

    for i, node in enumerate(ttnn_all_nodes):
        if option == "profiling" and i % 500 == 0:
            graph_code.append(f"    ttnn.DumpDeviceProfiler(device)")

        if isinstance(node, tuple):
            if option == "accuracy":
                graph_code.append(f"    check_accuracy({node[0]}, {node[1]})")
        else:
            # Print the accuracy of the outputs for this forward function
            if node.op == "output" and option == "accuracy":
                graph_code.append(f"    ttnn_outputs = {node.args[0]}")
                graph_code.append(
                    "    accuracy = np.mean([comp_pcc_wrapper(a, t) for a, t in zip(aten_outputs, ttnn_outputs)])"
                )
                graph_code.append(f'    print(f"{forward_func_name} accuracy: {{accuracy}}")')

            graph_code.append(f"    {_node_to_python_code(node)}")

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


# rename to forward_definitions and forward_calls maybe?
def _generate_code(model_name, forward_codes, call_forwards_in_main, all_inputs, torch_ttnn_option):
    """
    Generate standlone a python script along with an input file containing
    data for weights, biases, and inputs for a model run.

    Args:
        model_name (str): The name of the model used for filename purposes.
        check_accuracy_graph_codes (List[str]): List of lines of code.
        all_inputs (List[List]): List of list of inputs including weights, biases, and dynamic data.

    Returns:
        None.
    """

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
    ]
    import_code += (
        [
            "from tracy import Profiler",
            "from tracy import signpost",
        ]
        if option == "profiling"
        else []
    )

    # List of aliases
    alias_code = [
        "aten = torch.ops.aten",
    ]

    # Definitions of wrapper functions
    wrapper_code = list(wrapper_funcs)

    # Statements that rename the wrapper functions to avoid conflicting names
    rename_wrapper_code = list(rename_wrappers)

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

    # check_accuracy helper function definition
    check_accuracy_code = (
        """
def check_accuracy(expected, actual):
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

    def format_forward_calls(call_forwards_in_main, leading_spaces=""):
        forward_calls_joined = [leading_spaces + line for line in call_forwards_in_main]
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
{format_forward_calls(call_forwards_in_main, "        ")}
        signpost(header="Run result post proc")
        profiler.disable()
"""
    else:
        forward_calls_joined = format_forward_calls(call_forwards_in_main, "    ")

    directory = Path("tests/export_code") / Path(option)
    input_pkl_file = Path(f"{model_name}_inputs.pickle")
    full_input_pkl_path = directory / input_pkl_file
    full_input_pkl_path.parent.mkdir(parents=True, exist_ok=True)
    main_code = f"""
if __name__ == "__main__":
    filepath = Path(__file__).with_name("{input_pkl_file.name}")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    device = ttnn.open_device(device_id=0, l1_small_size=16384)
    # ttnn.enable_program_cache(device)
{forward_calls_joined}
    ttnn.close_device(device)
"""

    # Assemble all of pieces of code into one script
    full_code = (
        import_code
        + alias_code
        + wrapper_code
        + rename_wrapper_code
        + pcc_funcs
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


def _export_code(model_name, aten_fx_graphs, ttnn_fx_graphs, inputs, torch_ttnn_option, chunk_idx):
    """
    Main entry to generate standalone python script with accuracy checks

    Args:
        model_name (str): The name of the model used for filename purposes.
        aten_fx_graphs (List[torch.fx.graph.Graph]): List of unmodified aten graphs.
        ttnn_fx_graphs (List[torch.fx.graph.Graph]): List of modified ttnn graphs.
        all_inputs (List[List]): List of list of inputs including weights, biases, and dynamic data.
        verbose (boolean): Print out additional info.

    Returns:
        None.
    """
    option = torch_ttnn_option.export_code
    if option is not None:
        assert option in export_code_options

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
        out_nodes = []
        for node in graph.nodes:
            if node.op == "output":
                out_nodes.extend(node.args[0])
        out_node_names = [node.name if node is not None else "_" for node in out_nodes]
        return out_node_names

    for graph_idx, aten_graph in enumerate(aten_fx_graphs):
        arg_node_names = get_names_of_args(aten_graph)

        if graph_idx == 0:
            assert len(arg_node_names) == len(inputs)
            # Map indices
            for i, arg in enumerate(arg_node_names):
                call_forwards_in_main.append(f"{arg} = inputs[{chunk_idx}][{i}]")
        else:
            prev_out_node_names = get_names_of_outputs(aten_fx_graphs[graph_idx - 1])

            for arg in arg_node_names:
                if arg == "clone":
                    for out_arg in reversed(prev_out_node_names):
                        if out_arg.startswith("primals"):
                            call_forwards_in_main.append(f"{arg} = {out_arg}")
                            break
                if arg.startswith("tangents"):
                    first_primal_idx = 0
                    for i, out_arg in enumerate(prev_out_node_names):
                        if out_arg.startswith("primals"):
                            first_primal_idx = i
                            break
                    tangent_node = prev_out_node_names[first_primal_idx - 1]
                    call_forwards_in_main.append(f"{arg} = {tangent_node}")

        # append device to the end of arg list
        arg_node_names.append("device")
        # Then lastly call the forward function
        out_node_names = get_names_of_outputs(aten_graph)
        out_nodes_string = f"{', '.join(out_node_names)} = " if out_node_names else ""
        call_forwards_in_main.append(f"{out_nodes_string}forward_{chunk_idx}_{graph_idx}({', '.join(arg_node_names)})")

    assert len(aten_fx_graphs) == len(ttnn_fx_graphs)

    # Contains a list of each forward graph
    forward_code = []
    # Tracks the output nodes for models with graph breakages
    output_nodes = []
    for graph_idx, (aten_graph, ttnn_graph) in enumerate(zip(aten_fx_graphs, ttnn_fx_graphs)):
        graph_code = _build_code_from_aten_ttnn_graphs(
            aten_graph, ttnn_graph, output_nodes, torch_ttnn_option, chunk_idx, graph_idx
        )
        if option == "profiling":
            # Insert last one before return
            graph_code.insert(-1, "  ttnn.DumpDeviceProfiler(device)")
        forward_code.append(graph_code)

    return forward_code, call_forwards_in_main


def export_code(model_name, torch_ttnn_option):
    """
    Main entry to generate standalone python script with accuracy checks

    Args:
        model_name (str): The name of the model used for filename purposes.
        torch_ttnn_option (TorchTtnnOption): object that holds aten_fx_graphs, ttnn_fx_graphs, all_inputs, and export_code options
    Returns:
        None.
    """

    aten_fx_graphs = torch_ttnn_option._aten_fx_graphs  # List[torch.fx.graph.Graph]
    ttnn_fx_graphs = torch_ttnn_option._ttnn_fx_graphs  # List[torch.fx.graph.Graph]
    all_inputs = torch_ttnn_option._all_inputs  # List[List]

    # list of forward definitions
    forward_code_list = []
    # list of calls to forward functions inside main()
    call_forwards_in_main_list = []
    assert len(aten_fx_graphs) == len(all_inputs)
    for chunk_idx, (aten_fx_graphs_chunk, ttnn_fx_graphs_chunk, inputs) in enumerate(
        zip(aten_fx_graphs, ttnn_fx_graphs, all_inputs)
    ):
        forward_code, call_forwards_in_main = _export_code(
            model_name, aten_fx_graphs_chunk, ttnn_fx_graphs_chunk, inputs, torch_ttnn_option, chunk_idx
        )
        forward_code_list.extend(forward_code)
        call_forwards_in_main_list.extend(call_forwards_in_main)

    _generate_code(model_name, forward_code_list, call_forwards_in_main_list, all_inputs, torch_ttnn_option)
