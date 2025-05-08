import torch
import ttnn
from torch.fx import Graph


class LoadWeightsGraph:
    def __init__(self):
        empty_graph = Graph()
        empty_module = torch.nn.Module()
        self.load_weights_graph = torch.fx.GraphModule(empty_module, empty_graph, class_name="load_weights")
        self.inputs = []
        self.outputs = []

    def add_input(self, args, kwargs):
        inp = self.load_weights_graph.graph.placeholder(args[0].target)
        self.inputs.append(inp)
        from_torch = self.load_weights_graph.graph.call_function(ttnn.from_torch, (inp,), kwargs)
        self.outputs.append(from_torch)

    def create_output(self):
        output = self.load_weights_graph.graph.output(self.outputs)
        return output
