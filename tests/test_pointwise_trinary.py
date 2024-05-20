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

    def _test_addcop_impl(self, source_op, target_op, with_value):
        class AddcmulModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            if with_value:

                def forward(self, x, y, z):
                    return source_op(x, y, z, value=1.0)

            else:

                def forward(self, x, y, z):
                    return source_op(x, y, z)

            def input_types(self):
                return [
                    ((4, 4), torch.float16),
                    ((4, 4), torch.float16),
                    ((4, 4), torch.float16),
                ]

        m = AddcmulModule()
        input_types = m.input_types()
        inputs = [torch.randint(1, 3, type[0]).type(type[1]) for type in input_types]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[3].target, ttnn.from_torch)
        self.assertEqual(nodes[4].target, ttnn.to_layout)
        self.assertEqual(nodes[5].target, ttnn.to_device)
        self.assertEqual(nodes[6].target, ttnn.from_torch)
        self.assertEqual(nodes[7].target, ttnn.to_layout)
        self.assertEqual(nodes[8].target, ttnn.to_device)
        self.assertEqual(nodes[9].target, ttnn.from_torch)
        self.assertEqual(nodes[10].target, ttnn.to_layout)
        self.assertEqual(nodes[11].target, ttnn.to_device)
        self.assertEqual(nodes[12].target, target_op)
        self.assertEqual(nodes[13].target, ttnn.from_device)
        self.assertEqual(nodes[14].target, ttnn.to_layout)
        self.assertEqual(nodes[15].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16), result_after.to(torch.bfloat16)
            )
        )

    def test_addcmul(self):
        self._test_addcop_impl(
            source_op=torch.addcmul, target_op=ttnn.addcmul, with_value=False
        )

    def test_addcmul_with_value(self):
        self._test_addcop_impl(
            source_op=torch.addcmul, target_op=ttnn.addcmul, with_value=True
        )

    def test_addcdiv(self):
        self._test_addcop_impl(
            source_op=torch.addcdiv, target_op=ttnn.addcdiv, with_value=False
        )

    def test_addcdiv_with_value(self):
        self._test_addcop_impl(
            source_op=torch.addcdiv, target_op=ttnn.addcdiv, with_value=True
        )

    def test_where(self):
        class WhereModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, x, y, z):
                return torch.where(x, y, z)

            def input_types(self):
                return [
                    ((4, 4), torch.bool),
                    ((4, 4), torch.float16),
                    ((4, 4), torch.float16),
                ]

        m = WhereModule()
        input_types = m.input_types()
        inputs = [torch.randint(1, 3, type[0]).type(type[1]) for type in input_types]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs)
        self.assertEqual(1, len(option._out_fx_graphs))
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertEqual(nodes[3].target, "to")
        self.assertEqual(nodes[4].target, ttnn.from_torch)
        self.assertEqual(nodes[5].target, ttnn.to_layout)
        self.assertEqual(nodes[6].target, ttnn.to_device)
        self.assertEqual(nodes[7].target, ttnn.from_torch)
        self.assertEqual(nodes[8].target, ttnn.to_layout)
        self.assertEqual(nodes[9].target, ttnn.to_device)
        self.assertEqual(nodes[10].target, ttnn.from_torch)
        self.assertEqual(nodes[11].target, ttnn.to_layout)
        self.assertEqual(nodes[12].target, ttnn.to_device)
        self.assertEqual(nodes[13].target, ttnn.where)
        self.assertEqual(nodes[14].target, ttnn.from_device)
        self.assertEqual(nodes[15].target, ttnn.to_layout)
        self.assertEqual(nodes[16].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(
            torch.allclose(
                result_before.to(torch.bfloat16), result_after.to(torch.bfloat16)
            )
        )
