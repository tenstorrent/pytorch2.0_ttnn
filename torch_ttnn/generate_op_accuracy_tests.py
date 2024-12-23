import inspect
import lzma
import pickle
import torch.utils._pytree as pytree
import ttnn
import torch
import types

from collections import defaultdict
from pathlib import Path
from tests.utils import assert_with_pcc, comp_pcc, construct_pcc_assert_message

wrapper_funcs = set()


# Returns a list of inputs to the first graph of model
def generate_flat_args(gm, example_inputs):
    full_args = []
    # torch/_functorch/aot_autograd.py::aot_module_simplified
    params = {
        **dict(gm.named_parameters(remove_duplicate=False)),
        **dict(gm.named_buffers(remove_duplicate=False)),
    }
    params_flat, params_spec = pytree.tree_flatten(params)
    params_flat = list(params_flat)
    full_args.extend(params_flat)
    full_args.extend(example_inputs)

    return full_args


def get_opname(node):
    if hasattr(node.target, "__name__"):
        return node.target.__name__
    elif str(node.target).startswith("aten."):
        return str(node.target)
    elif isinstance(node.op, str):
        return node.target
    else:
        raise


# rename node names because some wrapper or built-in functions have the same name
def rename_nodes(graph, prefix):
    for node in graph.nodes:
        if node.op != "placeholder" and node.op != "output" and node.op != "get_attr":
            # simplify or put this in a new function
            opname = get_opname(node)
            if not opname.startswith("aten.") and not opname.startswith("ttnn."):
                node._rename(f"{prefix}_{node.name}")
    return graph


def format_dict(obj):
    to_kwargs = []
    # handle some cases str(torch.device) has no quotes
    for k, v in obj.items():
        if k == "device" and isinstance(v, torch.device):
            v = f'"{v}"'
        to_kwargs.append(f"{k} = {v}")
    return ", ".join(to_kwargs)


# collect wrapper functions if required
def node_to_python_code(node):
    # assume no placeholder and output?
    assert node.op not in ["placeholder", "output"]

    # handle get_attr nodes
    if node.op == "get_attr":
        # Embed get_attr constant into code
        tensor_data = getattr(node.graph.owning_module, node.target).data
        torch.set_printoptions(profile="full")
        statement = f"{node} = torch.{tensor_data}"
        torch.set_printoptions(profile="default")
        return statement

    node_args = ", ".join([str(arg) for arg in node.args])

    if node.target.__name__ == "getitem":
        return f"{node} = {node.args[0]}[{node.args[1]}]"

    # simplify or put this in a new function
    opname = str(node.target) if str(node.target).startswith("aten.") else node.target.__name__
    if (
        not opname.startswith("aten.")
        and not opname.startswith("ttnn.")
        and not isinstance(node.target, types.BuiltinFunctionType)
    ):
        lines = inspect.getsource(node.target)
        wrapper_funcs.add(lines)

    # find a better way to use registered custom builtins to replace TTNN constants
    statement = f"{node} = {opname}({node_args}, {format_dict(node.kwargs)})"
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


def users_have_getitem(node):
    for user in list(node.users.keys()):
        if user.op != "output" and user.op != "placeholder" and user.target.__name__ == "getitem":
            return user
    return None


# does this modify node in-place?
def rename_input_args_from_graph_break(output_nodes, node):
    # check for previous outputs
    if node.name == "clone":
        for out_arg in reversed(output_nodes[-1]):
            if out_arg.name.startswith("primals"):
                if out_arg.name in [a.name for a in output_nodes[-1]]:
                    node.replace_all_uses_with(out_arg, delete_user_cb=lambda node: node != out_arg)
                else:
                    node._rename(out_arg.name)
                break
    if node.name.startswith("tangent"):
        first_primal_idx = 0
        for i, out_arg in enumerate(output_nodes[-1]):
            if out_arg.name.startswith("primals"):
                first_primal_idx = i
                break
        tangent_node = output_nodes[-1][first_primal_idx - 1]
        if tangent_node.name in [a.name for a in output_nodes[-1]]:
            node.replace_all_uses_with(tangent_node, delete_user_cb=lambda node: node != tangent_node)
        else:
            node._rename(tangent_node.name)


def compute_key(node):
    if "tensor_meta" in node.meta:
        tensor_meta = node.meta["tensor_meta"]
    else:
        tensor_meta = node.meta["val"]
        # Workaround for layer_norm and other ops that has a list for "val"
        if isinstance(tensor_meta, tuple):
            tensor_meta = node.meta["val"][0]
    return str(node.meta["seq_nr"]) + node.meta["original_aten"]._name + str(tensor_meta)


def map_meta_to_aten_node(aten_graph):
    aten_name_to_node_map = defaultdict(list)
    for node in aten_graph.nodes:
        if node.op != "placeholder" and node.op != "output":
            aten_name_to_node_map[compute_key(node)] = node
    return aten_name_to_node_map


def map_aten_node_to_ttnn_node(ttnn_graph, output_nodes, aten_name_to_node_map):
    aten_to_ttnn_map = defaultdict(list)
    for node in ttnn_graph.nodes:
        if node.op == "placeholder":
            rename_input_args_from_graph_break(output_nodes, node)
            continue

        if node.op != "placeholder" and node.op != "output":
            # ignore to_torch
            if node.target == ttnn.to_torch:
                continue
            if "seq_nr" in node.meta:
                aten_node_name = compute_key(node)
                aten_node = aten_name_to_node_map[aten_node_name]
                aten_to_ttnn_map[aten_node].append(node)
                # also append gettiem if exists
    return aten_to_ttnn_map


# gather ttnn ops into a list and insert tuple in between
# this does not alter the graph, but prepare the list to translate to textual code
def process_ttnn_ops(ttnn_graph, aten_name_to_node_map, aten_to_ttnn_map):
    ttnn_all_nodes = []
    for node in ttnn_graph.nodes:
        if node.op == "output":
            continue
        if node.op == "placeholder":
            continue
        ttnn_all_nodes.append(node)
        # if ((from_node := node.meta.get("from_node", None)) is not None):
        if "seq_nr" in node.meta:
            aten_node_name = compute_key(node)
            aten_node = aten_name_to_node_map[aten_node_name]
            # this is the last ttnn node for this aten op, compare the output of this
            if node == aten_to_ttnn_map[aten_node][-1]:
                # this will be converted to test_accuracy(node1, node2) later
                # do not emit if users are getitem
                if not users_have_getitem(node):
                    if (getitem := users_have_getitem(aten_node)) is not None:
                        aten_node = getitem
                    ttnn_all_nodes.append((aten_node, node))
    return ttnn_all_nodes


def generate_op_accuracy_tests(model_name, aten_fx_graphs, ttnn_fx_graphs, all_inputs, *, verbose=False):
    assert len(aten_fx_graphs) == len(ttnn_fx_graphs)

    test_accuracy_graph_codes = []
    output_nodes = []
    for aten_graph, ttnn_graph in zip(aten_fx_graphs, ttnn_fx_graphs):
        ttnn_graph = rename_nodes(ttnn_graph, "ttnn_prefix")

        # map meta data to aten node
        # TODO: make sure key matches the correct group of aten ops
        aten_name_to_node_map = map_meta_to_aten_node(aten_graph)

        # gather all aten nodes and arg nodes
        aten_all_nodes = []
        arg_nodes = []
        for node in aten_graph.nodes:
            if node.op == "placeholder":
                rename_input_args_from_graph_break(output_nodes, node)
                arg_nodes.append(node)
                continue
            aten_all_nodes.append(node)

        # preprocess: map aten to ttnn ops. this is to know what is the last ttnn op in group to compare output
        aten_to_ttnn_map = map_aten_node_to_ttnn_node(ttnn_graph, output_nodes, aten_name_to_node_map)

        # interleave aten with ttnn code and insert test_accuracy code at the end of each section
        ttnn_all_nodes = process_ttnn_ops(ttnn_graph, aten_name_to_node_map, aten_to_ttnn_map)

        # finally convert interleaved nodes to python code for this graph
        arg_node_names = [node.name for node in arg_nodes]

        forward_signature = f"def forward({', '.join(arg_node_names)}):"
        # comment out signature if not the first graph
        graph_code = [forward_signature] if len(output_nodes) == 0 else ["   # " + forward_signature]
        graph_code.append("  device = ttnn.open_device(device_id=0, l1_small_size=16384)")
        for node in aten_all_nodes:
            if node.op == "output":
                output_nodes.append(node.args[0])
                graph_code.append(f"  # return {node.args[0]}")
                continue
            else:
                graph_code.append(f"  {node_to_python_code(node)}")
        for node in ttnn_all_nodes:
            if isinstance(node, tuple):
                graph_code.append(f"  test_accuracy({node[0]}, {node[1]})")
            else:
                graph_code.append(f"  {node_to_python_code(node)}")
        graph_code.append("  ttnn.close_device(device)")

        test_accuracy_graph_codes.append("\n".join(graph_code))

    # arrange full code
    import_code = [
        "import lzma",
        "import numpy as np",
        "import pickle",
        "import ttnn",
        "import torch",
        "from pathlib import Path",
        "aten = torch.ops.aten",
    ]

    # this needs to be done after the graph_code above because wrapper functions need to be resolved at that stage
    wrapper_code = list(wrapper_funcs)

    # test_accuracy helper code
    test_accuracy_code = """
def test_accuracy(expected, actual):
    if isinstance(actual, ttnn.Tensor):
        actual = ttnn.to_torch(actual)
    assert_with_pcc(expected, actual, pcc = 0.90)
"""

    # pcc functions
    pcc_funcs = [
        inspect.getsource(comp_pcc),
        inspect.getsource(construct_pcc_assert_message),
        inspect.getsource(assert_with_pcc),
    ]

    # main
    directory = Path("accuracy_tests")
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

    full_code = import_code + pcc_funcs + wrapper_code + [test_accuracy_code] + test_accuracy_graph_codes + [main_code]
    full_text = "\n".join(full_code)

    with open(directory / Path(f"{model_name}_code.py"), "w") as text_file:
        print(full_text, file=text_file)

    with lzma.open(directory / Path(f"{model_name}_inputs.pickle"), "wb") as f:
        pickle.dump(all_inputs, f)
