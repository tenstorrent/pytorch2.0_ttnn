import torch
import torch_ttnn
import unittest
from torch_ttnn import ttnn


class AddModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return x + y

    def input_shapes(self):
        return [(4, 4), (4, 4)]


class MatmulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.matmul(x, y)

    def input_shapes(self):
        return [(3, 4), (4, 5)]


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
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        # TODO(yoco) Check the graph has be rewritten and contain ttnn ops
        result_after = m.forward(*inputs)
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_matmul(self):
        m = MatmulModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        # TODO(yoco) Check the graph has be rewritten and contain ttnn ops
        result_after = m.forward(*inputs)
        self.assertTrue(torch.allclose(result_before, result_after))


if __name__ == "__main__":
    unittest.main()
