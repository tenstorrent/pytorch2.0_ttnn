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
        class ReshapeModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, new_shape):
                return torch.reshape(x, new_shape)

            def input_shapes(self):
                return [(32, 64)]

        m = ReshapeModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        new_shape = (64, 32)
        result_before = m.forward(*inputs, new_shape)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, new_shape)

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
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, order)

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[1].target, ttnn.from_torch)
        self.assertEqual(nodes[2].target, ttnn.to_layout)
        self.assertEqual(nodes[3].target, ttnn.to_device)
        self.assertEqual(nodes[4].target, ttnn.permute)
        self.assertEqual(nodes[5].target, ttnn.from_device)
        self.assertEqual(nodes[6].target, ttnn.to_layout)
        self.assertEqual(nodes[7].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_t(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return x.t()

            def input_shapes(self):
                return [(32, 16)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[1].target, ttnn.from_torch)
        self.assertEqual(nodes[2].target, ttnn.to_layout)
        self.assertEqual(nodes[3].target, ttnn.to_device)
        self.assertEqual(nodes[4].target, ttnn.permute)
        self.assertEqual(nodes[4].args[1], (1, 0))
        self.assertEqual(nodes[5].target, ttnn.from_device)
        self.assertEqual(nodes[6].target, ttnn.to_layout)
        self.assertEqual(nodes[7].target, ttnn.to_torch)
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
        sizes = (2, 2)
        result_before = m.forward(*inputs, sizes)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, sizes)

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[1].target, ttnn.from_torch)
        self.assertEqual(nodes[2].target, ttnn.to_layout)
        self.assertEqual(nodes[3].target, ttnn.to_device)
        self.assertEqual(nodes[4].target, torch_ttnn.target_wrappers.repeat)
        self.assertEqual(nodes[5].target, ttnn.from_device)
        self.assertEqual(nodes[6].target, ttnn.to_layout)
        self.assertEqual(nodes[7].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def _test_concat_impl(self, dim):
        class RepeatModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x1, x2, dim):
                return torch.cat([x1, x2], dim)

            def input_shapes(self):
                return [(4, 2), (4, 2)]

        m = RepeatModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs, dim)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, dim)

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[2].target, ttnn.from_torch)
        self.assertEqual(nodes[3].target, ttnn.to_layout)
        self.assertEqual(nodes[4].target, ttnn.to_device)
        self.assertEqual(nodes[5].target, ttnn.from_torch)
        self.assertEqual(nodes[6].target, ttnn.to_layout)
        self.assertEqual(nodes[7].target, ttnn.to_device)
        self.assertEqual(nodes[8].target, ttnn.concat)
        self.assertEqual(nodes[9].target, ttnn.from_device)
        self.assertEqual(nodes[10].target, ttnn.to_layout)
        self.assertEqual(nodes[11].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_concat_0(self):
        self._test_concat_impl(0)

    def test_concat_1(self):
        self._test_concat_impl(1)

    def test_split(self):
        class RepeatModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, size, dim):
                return torch.split(x, size, dim)

            def input_shapes(self):
                return [(5, 2)]

        m = RepeatModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs, 2, 0)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, 2, 0)

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[1 + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[1 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[1 + 2].target, ttnn.to_device)
        self.assertEqual(nodes[4].target, ttnn.split)
        self.assertEqual(nodes[5 + 0].target.__name__, "getitem")
        self.assertEqual(nodes[5 + 1].target.__name__, "getitem")
        self.assertEqual(nodes[5 + 2].target.__name__, "getitem")
        self.assertEqual(nodes[8 + 0].target, ttnn.from_device)
        self.assertEqual(nodes[8 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[8 + 2].target, ttnn.to_torch)
        self.assertEqual(nodes[11 + 0].target, ttnn.from_device)
        self.assertEqual(nodes[11 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[11 + 2].target, ttnn.to_torch)
        self.assertEqual(nodes[14 + 0].target, ttnn.from_device)
        self.assertEqual(nodes[14 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[14 + 2].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before[0], result_after[0]))
        self.assertTrue(torch.allclose(result_before[1], result_after[1]))
        self.assertTrue(torch.allclose(result_before[2], result_after[2]))