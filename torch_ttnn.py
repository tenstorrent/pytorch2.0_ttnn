import torch.linalg
import ttnn
import torch.nn as nn
import torch
from torch.fx import symbolic_trace
import operator
from typing import List

torch.fx.graph._register_custom_builtin('Device', 'from ttnn import Device', ttnn.Device)

device_id: int = 0

def linear(i, weight, bias):
    return ttnn.add(ttnn.matmul(i, weight), bias)


def replace_with_ttnn(node, func, device):
    """
    Replace a node with a new node that calls the given function with the same arguments.
    """
    graph: torch.fx.Graph = node.graph
    with graph.inserting_before(node):
        from_torch = tuple(graph.call_function(ttnn.from_torch, (i,)) for i in node.args)
        to_device = tuple(graph.call_function(ttnn.to_device, (i, device)) for i in from_torch)
        ttnn_op = graph.call_function(func, to_device)
        from_device = graph.call_function(ttnn.from_device, (ttnn_op, device))
        to_torch = graph.call_function(ttnn.to_torch, (from_device,))
        node.replace_all_uses_with(to_torch)
        graph.erase_node(node)

def eliminate_paired_data_movement(node, func, pre_func, check_device = False):
    """
    Eliminate redudent pattern of paired data movement, such as from_device => to_device.
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

def eliminate_paired_data_movement_pass(gm: torch.fx.GraphModule):
    changed = False
    for node in gm.graph.nodes:
        changed |= eliminate_paired_data_movement(node, ttnn.to_device, ttnn.from_device, check_device=True)
        changed |= eliminate_paired_data_movement(node, ttnn.from_device, ttnn.to_device, check_device=True)
        changed |= eliminate_paired_data_movement(node, ttnn.to_torch, ttnn.from_torch)
        changed |= eliminate_paired_data_movement(node, ttnn.from_torch, ttnn.to_torch)
    if changed:
        gm.graph.eliminate_dead_code()
        gm.recompile()
    return changed

def aten_backend(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], options={}) -> torch.fx.GraphModule:
    """
    The backend for torch.compile that converts a graph to use ttnn.
    The graph is wrapped in torch._dynamo.backends.common.aot_autograd, which
    trace into low level ATen ops not only high level torch ops.
    """
    device = ttnn.Device(device_id)
    graph: torch.fx.Graph = gm.graph
    for node in gm.graph.nodes:
        if node.op == 'call_function' and node.target == torch.ops.aten.add.Tensor:
            replace_with_ttnn(node, ttnn.add, device)
        elif node.op == 'call_function' and node.target == torch.ops.aten.mul.Tensor:
            replace_with_ttnn(node, ttnn.matmul, device)

    gm.recompile()

    while True:
        if not eliminate_paired_data_movement_pass(gm):
            break

    gm.graph.print_tabular()
    return gm

from torch._dynamo.backends.common import aot_autograd
backend = aot_autograd(fw_compiler=aten_backend)
