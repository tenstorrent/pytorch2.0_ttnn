import torch
import torch_ttnn
import unittest
from torch_ttnn import ttnn
from torch.fx.passes.dialect.common.cse_pass import CSEPass


class AddModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x

    def input_shapes(self):
        return [(4, 4)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open(0)

    def tearDown(self):
        # Close the device
        ttnn.close(self.device)

    def test_add(self):
        m = AddModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option.out_fx_graph.print_tabular()
        
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option.out_fx_graph.nodes)
        self.assertTrue(nodes[3].target == ttnn.add)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))
