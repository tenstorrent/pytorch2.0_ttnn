
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


    def test_add(self):
        class AddModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.add(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = AddModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.add)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_atan2(self):
        class Atan2Module(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.atan2(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = Atan2Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.atan2)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_eq(self):
        class EqModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.eq(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = EqModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.eq)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_gt(self):
        class GtModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.gt(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = GtModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.gt)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_logical_and(self):
        class Logical_andModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.logical_and(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = Logical_andModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.logical_and)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_logical_or(self):
        class Logical_orModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.logical_or(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = Logical_orModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.logical_or)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_logical_xor(self):
        class Logical_xorModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.logical_xor(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = Logical_xorModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.logical_xor)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_lt(self):
        class LtModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.lt(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = LtModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.lt)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_maximum(self):
        class MaximumModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.maximum(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = MaximumModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.maximum)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_minimum(self):
        class MinimumModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.minimum(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = MinimumModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.minimum)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_mul(self):
        class MulModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.mul(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = MulModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.mul)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_ne(self):
        class NeModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.ne(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = NeModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.ne)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_pow(self):
        class PowModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.pow(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = PowModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.pow)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_sub(self):
        class SubModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.sub(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = SubModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.sub)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))

    def test_xlogy(self):
        class XlogyModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x, y): return torch.xlogy(x, y)
            def input_shapes(self): return [(4, 4), (4, 4)]

        m = XlogyModule()
        input_shapes = m.input_shapes()
        inputs = [
            torch.randint(0, 3, shape).type(torch.bfloat16) for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.xlogy)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before.to(torch.bfloat16), result_after.to(torch.bfloat16), rtol=0.2))
