
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
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.abs(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.abs)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_acos(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.acos(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.acos)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_acosh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.acosh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 1
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.acosh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_asin(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.asin(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.asin)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_asinh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.asinh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.asinh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_atan(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.atan(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.atan)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_atanh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.atanh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.atanh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_clone(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.clone(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == torch_ttnn.target_wrappers.clone)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_cos(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.cos(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.cos)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_cosh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.cosh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.cosh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_erf(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.erf(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.erf)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_exp(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.exp(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.exp)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_expm1(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.expm1(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 1
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.expm1)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_gelu(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.nn.functional.gelu(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.gelu)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_hardtanh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.nn.functional.hardtanh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.hardtanh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_isinf(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.isinf(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.isinf)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_isnan(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.isnan(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.isnan)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_leaky_relu(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.nn.functional.leaky_relu(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.leaky_relu)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_log(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.log(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.log)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_log10(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.log10(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.log10)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_log1p(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.log1p(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.log1p)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_log2(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.log2(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.log2)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_logical_not(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.logical_not(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.logical_not)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_neg(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.neg(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.neg)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_reciprocal(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.reciprocal(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.reciprocal)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_relu(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.relu(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.relu)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_rsqrt(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.rsqrt(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.rsqrt)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_sigmoid(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.sigmoid(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.sigmoid)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_sign(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.sign(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.sign)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_sin(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.sin(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.sin)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_sinh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.sinh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.sinh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_silu(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.nn.functional.silu(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.silu)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_sqrt(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.sqrt(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.sqrt)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_tan(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.tan(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.tan)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_tanh(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return torch.tanh(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + 0
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.tanh)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )
