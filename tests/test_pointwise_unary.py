
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

    def _test_impl(self, from_op, to_op, init_shift):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x):
                return from_op(x)

            def input_shapes(self):
                return [(4, 4)]

        m = Module()
        input_shapes = m.input_shapes()
        inputs = [
            torch.rand(shape, dtype=torch.bfloat16) + init_shift
            for shape in input_shapes
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == to_op)
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

    def test_abs(self):
        self._test_impl(torch.abs, ttnn.abs, 0)

    def test_acos(self):
        self._test_impl(torch.acos, ttnn.acos, 0)

    def test_acosh(self):
        self._test_impl(torch.acosh, ttnn.acosh, 1)

    def test_asin(self):
        self._test_impl(torch.asin, ttnn.asin, 0)

    def test_asinh(self):
        self._test_impl(torch.asinh, ttnn.asinh, 0)

    def test_atan(self):
        self._test_impl(torch.atan, ttnn.atan, 0)

    def test_atanh(self):
        self._test_impl(torch.atanh, ttnn.atanh, 0)

    def test_clone(self):
        self._test_impl(torch.clone, torch_ttnn.target_wrappers.clone, 0)

    def test_cos(self):
        self._test_impl(torch.cos, ttnn.cos, 0)

    def test_cosh(self):
        self._test_impl(torch.cosh, ttnn.cosh, 0)

    def test_erf(self):
        self._test_impl(torch.erf, ttnn.erf, 0)

    def test_exp(self):
        self._test_impl(torch.exp, ttnn.exp, 0)

    def test_expm1(self):
        self._test_impl(torch.expm1, ttnn.expm1, 1)

    def test_gelu(self):
        self._test_impl(torch.nn.functional.gelu, ttnn.gelu, 0)

    def test_hardtanh(self):
        self._test_impl(torch.nn.functional.hardtanh, ttnn.hardtanh, 0)

    def test_isinf(self):
        self._test_impl(torch.isinf, ttnn.isinf, 0)

    def test_isnan(self):
        self._test_impl(torch.isnan, ttnn.isnan, 0)

    def test_leaky_relu(self):
        self._test_impl(torch.nn.functional.leaky_relu, ttnn.leaky_relu, 0)

    def test_log(self):
        self._test_impl(torch.log, ttnn.log, 0)

    def test_log10(self):
        self._test_impl(torch.log10, ttnn.log10, 0)

    def test_log1p(self):
        self._test_impl(torch.log1p, ttnn.log1p, 0)

    def test_log2(self):
        self._test_impl(torch.log2, ttnn.log2, 0)

    def test_logical_not(self):
        self._test_impl(torch.logical_not, ttnn.logical_not, 0)

    def test_neg(self):
        self._test_impl(torch.neg, ttnn.neg, 0)

    def test_reciprocal(self):
        self._test_impl(torch.reciprocal, ttnn.reciprocal, 0)

    def test_relu(self):
        self._test_impl(torch.relu, ttnn.relu, 0)

    def test_rsqrt(self):
        self._test_impl(torch.rsqrt, ttnn.rsqrt, 0)

    def test_sigmoid(self):
        self._test_impl(torch.sigmoid, ttnn.sigmoid, 0)

    def test_sign(self):
        self._test_impl(torch.sign, ttnn.sign, 0)

    def test_sin(self):
        self._test_impl(torch.sin, ttnn.sin, 0)

    def test_sinh(self):
        self._test_impl(torch.sinh, ttnn.sinh, 0)

    def test_silu(self):
        self._test_impl(torch.nn.functional.silu, ttnn.silu, 0)

    def test_sqrt(self):
        self._test_impl(torch.sqrt, ttnn.sqrt, 0)

    def test_tan(self):
        self._test_impl(torch.tan, ttnn.tan, 0)

    def test_tanh(self):
        self._test_impl(torch.tanh, ttnn.tanh, 0)
