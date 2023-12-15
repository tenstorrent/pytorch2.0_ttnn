import torch.linalg
import torch.nn as nn
import torch
from torch.fx import symbolic_trace
import operator
from typing import List
import fx_graphviz

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    import mock_ttnn as ttnn

global_device: ttnn.Device = None


def replace_with_ttnn(node, func, device):
    """
    Replace a node with a new node that calls the given function with the same arguments.
    It will insert data movement and data conversion before and after the call.
    Replace:
        node
    With:
        from_torch => to_device => op-func => from_device => to_torch
    """
    graph: torch.fx.Graph = node.graph
    with graph.inserting_before(node):
        from_torch = tuple(graph.call_function(ttnn.from_torch, (i,)) for i in node.args)
        to_device = tuple(graph.call_function(ttnn.to_device, (i, device)) for i in from_torch)
        ttnn_op = graph.call_function(func, to_device)
        from_device = graph.call_function(ttnn.from_device, (ttnn_op,))
        to_torch = graph.call_function(ttnn.to_torch, (from_device,))
        node.replace_all_uses_with(to_torch)
        graph.erase_node(node)

def eliminate_redundant_data_movement_conversion(node, func, pre_func, check_device = False):
    """
    Eliminate redundant pattern of paired data movement, such as from_device => to_device.
    """
    changed = False
    available_func_list = [ttnn.from_device, ttnn.to_device, ttnn.from_torch, ttnn.to_torch]
    if func not in available_func_list or pre_func not in available_func_list:
        return changed
    if len(node.users) == 0:
        return changed
    if node.op == 'call_function' and node.target == func:
        pre_node = node.args[0]
        if type(pre_node) == torch.fx.node.Node and \
            pre_node.op == 'call_function' and pre_node.target == pre_func:
            if not check_device or node.args[1] == pre_node.args[1]:
                node.replace_all_uses_with(pre_node.args[0])
                changed = True
    return changed

def eliminate_redundant_data_movement_conversion_pass(gm: torch.fx.GraphModule):
    changed = False
    for node in gm.graph.nodes:
        changed |= eliminate_redundant_data_movement_conversion(node, ttnn.to_device, ttnn.from_device, check_device=True)
        changed |= eliminate_redundant_data_movement_conversion(node, ttnn.from_device, ttnn.to_device, check_device=True)
        changed |= eliminate_redundant_data_movement_conversion(node, ttnn.to_torch, ttnn.from_torch)
        changed |= eliminate_redundant_data_movement_conversion(node, ttnn.from_torch, ttnn.to_torch)
    if changed:
        gm.graph.eliminate_dead_code()
        gm.recompile()
    return changed

class WrapperDevice():
    def __repr__(self):
        return f"global_device"

def rewrite_tt_op_pass(gm: torch.fx.GraphModule):
    #device = ttnn.DeviceWrapper(device_id)
    device = WrapperDevice()
    graph: torch.fx.Graph = gm.graph
    for node in gm.graph.nodes:
        if node.op == 'call_function' and node.target == torch.ops.aten.add.Tensor:
            replace_with_ttnn(node, ttnn.add, device)
        elif node.op == 'call_function' and node.target == torch.ops.aten.mm.default:
            replace_with_ttnn(node, ttnn.matmul, device)
        elif node.op == 'call_function' and node.target == torch.ops.aten.mul.Tensor:
            replace_with_ttnn(node, ttnn.matmul, device)


def set_device(device):
    global global_device
    global_device = device


def graphviz_pass(gm: torch.fx.GraphModule, filename: str):
    fx_graphviz.to_svg(gm.graph, filename)


def aten_backend(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], options={}) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """
    
    graphviz_pass(gm, "00-before")
    torch.fx.graph._register_custom_builtin('global_device', 'from . import global_device', global_device)

    # Rewrite with ttnn ops, will insert redundant data movement
    rewrite_tt_op_pass(gm)
    graphviz_pass(gm, "01-rewrite")
    # After rewrite, remove redundant data movement
    while True:
        if not eliminate_redundant_data_movement_conversion_pass(gm):
            break
    graphviz_pass(gm, "02-eliminate")

    gm.graph.print_tabular()
    gm.recompile()
    print(gm.code)
    return gm

from torch._dynamo.backends.common import aot_autograd
backend = aot_autograd(fw_compiler=aten_backend)
