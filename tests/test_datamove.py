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

    def test_reshape(self):
        class SoftmaxModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, new_shape):
                return torch.reshape(x, new_shape)

            def input_shapes(self):
                return [(32, 64)]

        m = SoftmaxModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        new_shape = (64, 32)
        result_before = m.forward(*inputs, new_shape)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, new_shape)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.reshape)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    # NOTE(yoco) This test failed because currently
    # the ttnn.permute does nothing. Seems like the ttnn.permute
    # is not implemented yet.
    def test_permute(self):
        class PermuteModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, order):
                return torch.permute(x, order)

            def input_shapes(self):
                return [(4, 4)]

        m = PermuteModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        order = (1, 0)
        result_before = m.forward(*inputs, order)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, order)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.permute)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_repeat(self):
        class RepeatModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, sizes):
                return x.repeat(sizes)

            def input_shapes(self):
                return [(4, 4)]

        m = RepeatModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        sizes = ttnn.Shape(2, 2)
        result_before = m.forward(*inputs, sizes)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, sizes)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.repeat)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))
