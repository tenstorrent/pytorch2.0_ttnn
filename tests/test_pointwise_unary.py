
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


    def test_abs(self):
        class AbsModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.abs(x)
            def input_shapes(self): return [(4, 4)]

        m = AbsModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.abs)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_acos(self):
        class AcosModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.acos(x)
            def input_shapes(self): return [(4, 4)]

        m = AcosModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.acos)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_acosh(self):
        class AcoshModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.acosh(x)
            def input_shapes(self): return [(4, 4)]

        m = AcoshModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) + 1 for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.acosh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_asin(self):
        class AsinModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.asin(x)
            def input_shapes(self): return [(4, 4)]

        m = AsinModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.asin)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_asinh(self):
        class AsinhModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.asinh(x)
            def input_shapes(self): return [(4, 4)]

        m = AsinhModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.asinh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_atan(self):
        class AtanModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.atan(x)
            def input_shapes(self): return [(4, 4)]

        m = AtanModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.atan)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_atanh(self):
        class AtanhModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.atanh(x)
            def input_shapes(self): return [(4, 4)]

        m = AtanhModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.atanh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_clone(self):
        class CloneModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.clone(x)
            def input_shapes(self): return [(4, 4)]

        m = CloneModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.clone)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_cos(self):
        class CosModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.cos(x)
            def input_shapes(self): return [(4, 4)]

        m = CosModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.cos)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_cosh(self):
        class CoshModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.cosh(x)
            def input_shapes(self): return [(4, 4)]

        m = CoshModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.cosh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_erf(self):
        class ErfModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.erf(x)
            def input_shapes(self): return [(4, 4)]

        m = ErfModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.erf)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_exp(self):
        class ExpModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.exp(x)
            def input_shapes(self): return [(4, 4)]

        m = ExpModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.exp)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_expm1(self):
        class Expm1Module(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.expm1(x)
            def input_shapes(self): return [(4, 4)]

        m = Expm1Module()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.expm1)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_gelu(self):
        class GeluModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.nn.functional.gelu(x)
            def input_shapes(self): return [(4, 4)]

        m = GeluModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.gelu)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_hardtanh(self):
        class HardtanhModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.nn.functional.hardtanh(x)
            def input_shapes(self): return [(4, 4)]

        m = HardtanhModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.hardtanh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_isinf(self):
        class IsinfModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.isinf(x)
            def input_shapes(self): return [(4, 4)]

        m = IsinfModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.isinf)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_isnan(self):
        class IsnanModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.isnan(x)
            def input_shapes(self): return [(4, 4)]

        m = IsnanModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.isnan)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_leaky_relu(self):
        class Leaky_reluModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.nn.functional.leaky_relu(x)
            def input_shapes(self): return [(4, 4)]

        m = Leaky_reluModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.leaky_relu)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_log(self):
        class LogModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.log(x)
            def input_shapes(self): return [(4, 4)]

        m = LogModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.log)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_log10(self):
        class Log10Module(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.log10(x)
            def input_shapes(self): return [(4, 4)]

        m = Log10Module()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.log10)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_log1p(self):
        class Log1pModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.log1p(x)
            def input_shapes(self): return [(4, 4)]

        m = Log1pModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.log1p)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_log2(self):
        class Log2Module(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.log2(x)
            def input_shapes(self): return [(4, 4)]

        m = Log2Module()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.log2)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_logical_not(self):
        class Logical_notModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.logical_not(x)
            def input_shapes(self): return [(4, 4)]

        m = Logical_notModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.logical_not)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_neg(self):
        class NegModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.neg(x)
            def input_shapes(self): return [(4, 4)]

        m = NegModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.neg)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_reciprocal(self):
        class ReciprocalModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.reciprocal(x)
            def input_shapes(self): return [(4, 4)]

        m = ReciprocalModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.reciprocal)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_relu(self):
        class ReluModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.relu(x)
            def input_shapes(self): return [(4, 4)]

        m = ReluModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.relu)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_rsqrt(self):
        class RsqrtModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.rsqrt(x)
            def input_shapes(self): return [(4, 4)]

        m = RsqrtModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.rsqrt)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_sigmoid(self):
        class SigmoidModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.sigmoid(x)
            def input_shapes(self): return [(4, 4)]

        m = SigmoidModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.sigmoid)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_sign(self):
        class SignModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.sign(x)
            def input_shapes(self): return [(4, 4)]

        m = SignModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.sign)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_sin(self):
        class SinModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.sin(x)
            def input_shapes(self): return [(4, 4)]

        m = SinModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.sin)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_sinh(self):
        class SinhModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.sinh(x)
            def input_shapes(self): return [(4, 4)]

        m = SinhModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.sinh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_sqrt(self):
        class SqrtModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.sqrt(x)
            def input_shapes(self): return [(4, 4)]

        m = SqrtModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.sqrt)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_tan(self):
        class TanModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.tan(x)
            def input_shapes(self): return [(4, 4)]

        m = TanModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.tan)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_tanh(self):
        class TanhModule(torch.nn.Module):
            def __init__(self): super().__init__()
            def forward(self, x): return torch.tanh(x)
            def input_shapes(self): return [(4, 4)]

        m = TanhModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.tanh)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.from_device)
        self.assertTrue(nodes[5].target == ttnn.to_layout)
        self.assertTrue(nodes[6].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))
