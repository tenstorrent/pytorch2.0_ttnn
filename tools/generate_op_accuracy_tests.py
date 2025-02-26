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
        if not is_operation(node):
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
                    # this will be converted to test_accuracy(node1, node2) later
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
    assert is_operation(node)

    # handle get_attr nodes
    if node.op == "get_attr":
        # Embed get_attr constant into code
        tensor_data = getattr(node.graph.owning_module, node.target).data
        torch.set_printoptions(profile="full")
        torch_prefix = "torch." if len(tensor_data.size()) > 0 else ""
        statement = f"{node} = {torch_prefix}{tensor_data}"
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


def _build_code_from_aten_ttnn_graphs(aten_graph, ttnn_graph, output_nodes):
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
            _rename_input_args_from_graph_break(output_nodes, node)
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
    the test_accuracy functions. 
    """
    ttnn_all_nodes = _process_ttnn_ops(ttnn_graph, aten_name_to_node_map, aten_to_ttnn_map)

    """
    Finally convert interleaved nodes to python code for this graph
    """
    arg_node_names = [node.name for node in arg_nodes]

    forward_signature = f"def forward({', '.join(arg_node_names)}):"
    # comment out signature if not the first graph
    graph_code = [forward_signature] if len(output_nodes) == 0 else ["   # " + forward_signature]
    graph_code.append("  device = ttnn.open_device(device_id=0, l1_small_size=16384)")
    
    op_list = ["tanh", "softmax"] 
    additional_test_nodes = {} 
    
    for node in aten_all_nodes: 
        if node.op == "output":
            output_nodes.append(node.args[0])
            graph_code.append(f"  # return {node.args[0]}")
            continue
        else:
            ind = [ind for ind, element in enumerate(op_list) if element in f"{node}"] 
            if len(ind) > 0: 
                node_name = f"{node}" if f"{node}"[0] != "_" else f"{node}"[1:] 
                additional_test_nodes[node_name] = node 
                
            graph_code.append(f"  {_node_to_python_code(node)}")

    for node in ttnn_all_nodes:
        if isinstance(node, tuple):
            graph_code.append(f"  test_accuracy({node[0]}, {node[1]})")
        else:
            graph_code.append(f"  {_node_to_python_code(node)}") 
            ind = [ind for ind, element in enumerate(op_list) if element in f"{node}"] 
            if len(ind) > 0: 
                node_name = "_".join(f"{node}".split("_")[1:]) 
                aten_node = additional_test_nodes[node_name] 
                graph_code.append(f"  test_accuracy({aten_node}, {node})") 
    
    graph_code.append("  ttnn.close_device(device)")

    return graph_code


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


def _generate_code(model_name, test_accuracy_graph_codes, all_inputs):
    """
    Generate standlone a python script along with an input file containing
    data for weights, biases, and inputs for a model run.

    Args:
        model_name (str): The name of the model used for filename purposes.
        test_accuracy_graph_codes (List[str]): List of lines of code.
        all_inputs (List): List of inputs including weights, biases, and dynamic data.

    Returns:
        None.
    """

    # List of modules
    import_code = [
        "import lzma",
        "import numpy as np",
        "import pickle",
        "import torch",
        "import ttnn",
        "from pathlib import Path",
    ]

    # List of aliases
    alias_code = [
        "aten = torch.ops.aten",
    ]

    # Definitions of wrapper functions
    wrapper_code = list(wrapper_funcs)

    # Statements that rename the wrapper functions to avoid conflicting names
    rename_wrapper_code = list(rename_wrappers)

    # pcc functions
    pcc_funcs = [
        inspect.getsource(comp_pcc),
        inspect.getsource(construct_pcc_assert_message),
        inspect.getsource(assert_with_pcc),
    ]

    # test_accuracy helper function definition
    test_accuracy_code = """
def test_accuracy(expected, actual):
    if isinstance(actual, ttnn.Tensor):
        actual = ttnn.to_torch(actual)
    assert_with_pcc(expected, actual, pcc = 0.90)
"""

    # main function definition
    directory = Path("tests/autogen_accuracy_tests")
    input_pkl_file = Path(f"{model_name}_inputs.pickle")
    full_input_pkl_path = directory / input_pkl_file
    full_input_pkl_path.parent.mkdir(parents=True, exist_ok=True)
    main_code = f"""
if __name__ == "__main__":
    filepath = Path(__file__).with_name("{input_pkl_file.name}")
    file = lzma.open(filepath, "rb")
    inputs = pickle.load(file)
    forward(*inputs)
"""

    # Assemble all of pieces of code into one script
    full_code = (
        import_code
        + alias_code
        + wrapper_code
        + rename_wrapper_code
        + pcc_funcs
        + [test_accuracy_code]
        + test_accuracy_graph_codes
        + [main_code]
    )
    full_text = "\n".join(full_code)

    code_full_path = directory / Path(f"{model_name}_code.py")
    with open(code_full_path, "w") as text_file:
        print(full_text, file=text_file)
        logging.info(f"Accuracy test code saved to {code_full_path}.")

    data_full_path = directory / Path(f"{model_name}_inputs.pickle")
    with lzma.open(data_full_path, "wb") as f:
        pickle.dump(all_inputs, f)
        logging.info(f"Accuracy data object saved to {data_full_path}.")


def generate_op_accuracy_tests(model_name, aten_fx_graphs, ttnn_fx_graphs, all_inputs):
    """
    Main entry to generate standalone python script with accuracy checks

    Args:
        model_name (str): The name of the model used for filename purposes.
        aten_fx_graphs (List[torch.fx.graph.Graph]): List of unmodified aten graphs.
        ttnn_fx_graphs (List[torch.fx.graph.Graph]): List of modified ttnn graphs.
        all_inputs (List): List of inputs including weights, biases, and dynamic data.
        verbose (boolean): Print out additional info.

    Returns:
        None.
    """

    assert len(aten_fx_graphs) == len(ttnn_fx_graphs)

    # Contains a list of each line of code
    test_accuracy_graph_codes = []
    # Tracks the output nodes for models with graph breakages
    output_nodes = []
    for aten_graph, ttnn_graph in zip(aten_fx_graphs, ttnn_fx_graphs):
        graph_code = _build_code_from_aten_ttnn_graphs(aten_graph, ttnn_graph, output_nodes)
        test_accuracy_graph_codes.append("\n".join(graph_code))

    _generate_code(model_name, test_accuracy_graph_codes, all_inputs)
