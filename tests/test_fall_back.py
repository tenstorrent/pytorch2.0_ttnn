import torch
import torch_ttnn
import unittest
import ttnn

from tests.utils import check_with_pcc


class MixModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        z = torch.div(x, y)
        z = torch.add(z, z)
        z = torch.matmul(z, z)
        z = torch.div(z, z)
        z = torch.div(z, z)
        return z

    def input_shapes(self):
        return [(4, 4), (4, 4)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_fall_back(self):
        m = MixModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        target = [node.target for node in nodes]
        self.assertEqual(target.count(ttnn.reciprocal), 3)
        self.assertEqual(target.count(ttnn.mul), 3)
        self.assertEqual(target.count(ttnn.add), 1)
        self.assertEqual(target.count(ttnn.matmul), 1)

        nodes = list(option._out_fx_graphs[-1].nodes)
        reciprocal_idx = [i for i, n in enumerate(target) if n == ttnn.reciprocal]
        multiply_idx = [i for i, n in enumerate(target) if n == ttnn.multiply]
        self.assertTrue(len(reciprocal_idx) == len(multiply_idx))
        for ri, mi in zip(reciprocal_idx, multiply_idx):
            self.assertTrue(ri < mi)
        add_idx = target.index(ttnn.add)
        self.assertTrue(add_idx > multiply_idx[0])
        self.assertTrue(add_idx < multiply_idx[1])
        self.assertTrue(add_idx < multiply_idx[2])
        matmul_idx = target.index(ttnn.matmul)
        self.assertTrue(matmul_idx > multiply_idx[0])
        self.assertTrue(matmul_idx > add_idx)
        self.assertTrue(matmul_idx < multiply_idx[1])
        self.assertTrue(matmul_idx < multiply_idx[2])

        # Check inference result
        self.assertTrue(check_with_pcc(result_before, result_after))
