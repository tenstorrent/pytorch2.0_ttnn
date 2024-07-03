
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
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.add(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.add)
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


    def test_atan2(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.atan2(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.atan2)
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


    def test_eq(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.eq(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.eq)
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


    def test_gt(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.gt(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.gt)
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


    def test_logical_and(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.logical_and(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.logical_and)
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


    def test_logical_or(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.logical_or(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.logical_or)
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


    def test_logical_xor(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.logical_xor(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.logical_xor)
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


    def test_lt(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.lt(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.lt)
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


    def test_maximum(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.maximum(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.maximum)
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


    def test_minimum(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.minimum(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.minimum)
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


    def test_mul(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.mul(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.mul)
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


    def test_ne(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.ne(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.ne)
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


    def test_pow(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.pow(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.pow)
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


    def test_pow_t_s(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.pow(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if False else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if False:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if False:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if False:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.pow)
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


    def test_sub(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.sub(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.sub)
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


    def test_xlogy(self):
        class Module(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y):
                return torch.xlogy(x, y)

        m = Module()
        inputs = [
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
            torch.randint(0, 3, (4, 4)).type(torch.bfloat16) if True else 2.0,
        ]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        # option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        acc_idx = 0
        if True:
            acc_idx += 1
        if True:
            acc_idx += 1
        i1_idx = acc_idx
        if True:
            acc_idx += 3
        i2_idx = acc_idx
        if True:
            acc_idx += 3
        op_idx = acc_idx
        o_idx = acc_idx + 1

        self.assertEqual(nodes[i1_idx + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[i1_idx + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[i1_idx + 2].target, ttnn.to_device)
        if True:
            self.assertEqual(nodes[i2_idx + 0].target, ttnn.from_torch)
            self.assertEqual(nodes[i2_idx + 1].target, ttnn.to_layout)
            self.assertEqual(nodes[i2_idx + 2].target, ttnn.to_device)
        self.assertEqual(nodes[op_idx].target, ttnn.xlogy)
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

