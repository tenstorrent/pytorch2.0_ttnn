import torch
import torch_ttnn
import ttnn
import unittest


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_matmul(self):
        class MatmulModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.matmul(x, y)

            def input_shapes(self):
                return [(32, 32), (32, 32)]

        m = MatmulModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[6].target, ttnn.matmul)
        self.assertEqual(nodes[6].args[0].target, ttnn.to_device)
        self.assertEqual(nodes[6].args[0].args[0].target, ttnn.from_torch)
        self.assertEqual(nodes[7].target, ttnn.from_device)
        self.assertEqual(nodes[8].target, ttnn.to_layout)
        self.assertEqual(nodes[9].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_linear(self):
        class LinearModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y, z):
                return torch.nn.functional.linear(x, y, z)

            def input_shapes(self):
                return [(32, 32), (32, 32), (32, 32)]

        m = LinearModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[9].target, ttnn.linear)
        self.assertEqual(nodes[9].args[0].target, ttnn.to_device)
        self.assertEqual(nodes[9].args[0].args[0].target, ttnn.from_torch)
        self.assertEqual(nodes[10].target, ttnn.from_device)
        self.assertEqual(nodes[11].target, ttnn.to_layout)
        self.assertEqual(nodes[12].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))
