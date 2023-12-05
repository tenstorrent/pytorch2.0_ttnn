import torch.linalg
import torch._C._nn
import ttnn
import torch.nn as nn
import torch
from torch.fx import symbolic_trace
import operator


def linear(i, weight, bias):
    return ttnn.add(ttnn.matmul(i, weight), bias)


class NestedTracer(torch.fx.Tracer):
    def is_leaf_module(self, m: torch.nn.Module, qualname: str):
        if isinstance(m, nn.Linear):
            return False
        return super().is_leaf_module(m, qualname)


def transform_ttnn(module : nn.Module) -> nn.Module:
    graph : torch.fx.Graph = NestedTracer().trace(module)
    symbolic_traced : torch.fx.GraphModule = torch.fx.GraphModule(module, graph)
    for node in graph.nodes:
        if node.op == 'call_function' and node.target == operator.add:
            node.target = ttnn.add
        elif node.op == 'call_function' and node.target == torch._C._nn.linear:
            node.target = linear
            
    result_module = torch.fx.GraphModule(module, graph)
    return result_module