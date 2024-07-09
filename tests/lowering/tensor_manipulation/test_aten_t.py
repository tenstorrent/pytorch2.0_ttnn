import torch
import torch_ttnn
import unittest
import ttnn
import tt_lib

from torch_ttnn.utils import check_with_pcc


class AtenTModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.t(x)

    def input_shapes(self):
        return [(1, 32)]


class AtenT0DModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.t(x)

    def input_shapes(self):
        return 5


class AtenT1DModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.t(x)

    def input_shapes(self):
        return [(5)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)
        # For AutoFormat
        tt_lib.device.SetDefaultDevice(self.device)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_aten_t(self):
        m = AtenTModule()
        input_shapes = m.input_shapes()
        input = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        result_before = m.forward(input)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(input)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)

        self.assertTrue(nodes[4].target == ttnn.permute)
        self.assertTrue(nodes[4].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[4].args[0].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[4].args[0].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(check_with_pcc(result_before, result_after))

    def test_aten_t_0d(self):
        m = AtenT0DModule()
        input_shapes = m.input_shapes()
        input = torch.rand(input_shapes, dtype=torch.bfloat16)
        result_before = m.forward(input)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(input)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)

        self.assertTrue(nodes[1].target == torch.ops.aten.t.default)
        self.assertTrue(nodes[1].args[0].target == "arg0_1")
        self.assertTrue(nodes[1].args[0].op == "placeholder")
        self.assertTrue(nodes[2].target == "output")
        self.assertTrue(nodes[2].op == "output")
        self.assertTrue(check_with_pcc(result_before, result_after))

    def test_aten_t_1d(self):
        m = AtenT1DModule()
        input_shapes = m.input_shapes()
        input = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        result_before = m.forward(input)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(input)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)

        self.assertTrue(nodes[1].target == torch.ops.aten.t.default)
        self.assertTrue(nodes[1].args[0].target == "arg0_1")
        self.assertTrue(nodes[1].args[0].op == "placeholder")
        self.assertTrue(nodes[2].target == "output")
        self.assertTrue(nodes[2].op == "output")
        self.assertTrue(check_with_pcc(result_before, result_after))


if __name__ == "__main__":
    unittest.main()
