import torch
import torch_ttnn
import unittest
from torch_ttnn import ttnn
import tt_lib


class MulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.mul(x, y)

    def input_shapes(self):
        return [(4, 4), (4, 4)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)
        # For AutoFormat
        tt_lib.device.SetDefaultDevice(self.device)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_mul(self):
        m = MulModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(1, 5, shape).type(torch.float32) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[10].target == ttnn.mul)
        self.assertTrue(nodes[10].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[10].args[0].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[10].args[0].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[10].args[1].target == ttnn.to_device)
        self.assertTrue(nodes[10].args[1].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[10].args[1].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[11].target == ttnn.from_device)
        self.assertTrue(nodes[12].target == ttnn.to_layout)
        self.assertTrue(nodes[13].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after))

    def test_mul_scalar(self):
        m = MulModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(1, 5, input_shapes[0]).type(torch.float32),
            torch.randint(1, 5, (1,)).type(torch.float32).item(),
        ]
        print(inputs)
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[5].target == ttnn.mul)
        self.assertTrue(nodes[5].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[5].args[0].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[5].args[0].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.from_device)
        self.assertTrue(nodes[7].target == ttnn.to_layout)
        self.assertTrue(nodes[8].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after))


if __name__ == "__main__":
    unittest.main()
