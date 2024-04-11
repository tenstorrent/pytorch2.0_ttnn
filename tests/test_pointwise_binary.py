
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

    def _test_impl(self, torch_op, ttnn_op, op1_is_tensor=True, op2_is_tensor=True):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch_op(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if op1_is_tensor else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if op2_is_tensor else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if op1_is_tensor:
            acc_idx += 1
        if op2_is_tensor:
            acc_idx += 1
        i1_idx = acc_idx
        if op1_is_tensor:
            acc_idx += 3
        i2_idx = acc_idx
        if op2_is_tensor:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if op2_is_tensor:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn_op)
        self.assertEqual(nodes[o_idx + 0].target, ttnn.from_device)
        self.assertEqual(nodes[o_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[o_idx + 2].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16),
                result_after.to(torch.bfloat16),
                rtol=0.2,
            )
        )

    def test_add(self):
        self._test_impl(torch.add, ttnn.add, True, True)

    def test_atan2(self):
        self._test_impl(torch.atan2, ttnn.atan2, True, True)

    def test_eq(self):
        self._test_impl(torch.eq, ttnn.eq, True, True)

    def test_gt(self):
        self._test_impl(torch.gt, ttnn.gt, True, True)

    def test_logical_and(self):
        self._test_impl(torch.logical_and, ttnn.logical_and, True, True)

    def test_logical_or(self):
        self._test_impl(torch.logical_or, ttnn.logical_or, True, True)

    def test_logical_xor(self):
        self._test_impl(torch.logical_xor, ttnn.logical_xor, True, True)

    def test_lt(self):
        self._test_impl(torch.lt, ttnn.lt, True, True)

    def test_maximum(self):
        self._test_impl(torch.maximum, ttnn.maximum, True, True)

    def test_minimum(self):
        self._test_impl(torch.minimum, ttnn.minimum, True, True)

    def test_mul(self):
        self._test_impl(torch.mul, ttnn.mul, True, True)

    def test_ne(self):
        self._test_impl(torch.ne, ttnn.ne, True, True)

    def test_pow(self):
        self._test_impl(torch.pow, ttnn.pow, True, True)

    def test_pow_t_s(self):
        self._test_impl(torch.pow, ttnn.pow, True, False)

    def test_sub(self):
        self._test_impl(torch.sub, ttnn.sub, True, True)

    def test_xlogy(self):
        self._test_impl(torch.xlogy, ttnn.xlogy, True, True)
