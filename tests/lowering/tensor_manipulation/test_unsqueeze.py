import torch
import torch_ttnn
import unittest
import ttnn
import tt_lib

# RuntimeError: TT_THROW @ ../ttnn/cpp/ttnn/operations/core.hpp:81: tt::exception
# info: Unable to reshape a tensor in TILE_LAYOUT to non-tile height and width!
# Please convert the input tensor to ROW_MAJOR_LAYOUT first.


class Unsqueeze1Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.unsqueeze(x, y)

    def input_shapes(self):
        return [(5, 2, 4, 3), 1]


class Unsqueeze2Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.unsqueeze(x, y)

    def input_shapes(self):
        return [(5, 2, 4), 1]


class Unsqueeze3Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.unsqueeze(x, y)

    def input_shapes(self):
        return [(5, 2, 4, 3), -2]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)
        # For AutoFormat
        tt_lib.device.SetDefaultDevice(self.device)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_unsqueeze1(self):
        mod = Unsqueeze1Module()
        input_shapes = mod.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        dim = input_shapes[1]
        inputs = [tensor, dim]
        result_before = mod.forward(*inputs)

        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
        # Throwing error in to_tt_pass.py not sure exactly where
        result_after = ttnn_mod.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.reshape)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    # 4D reshapes are done on device
    def test_unsqueeze2(self):
        mod = Unsqueeze2Module()
        input_shapes = mod.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        dim = input_shapes[1]
        inputs = [tensor, dim]
        result_before = mod.forward(*inputs)

        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
        # Throwing error in to_tt_pass.py not sure exactly where
        result_after = ttnn_mod.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[4].target == ttnn.reshape)
        self.assertTrue(nodes[4].args[0].target == ttnn.to_device)
        self.assertTrue(nodes[4].args[0].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[4].args[0].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_unsqueeze3(self):
        mod = Unsqueeze3Module()
        input_shapes = mod.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        dim = input_shapes[1]
        inputs = [tensor, dim]
        result_before = mod.forward(*inputs)

        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
        # Throwing error in to_tt_pass.py not sure exactly where
        result_after = ttnn_mod.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()
        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[3].target == ttnn.reshape)
        self.assertTrue(nodes[3].args[0].target == ttnn.to_layout)
        self.assertTrue(nodes[3].args[0].args[0].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))


if __name__ == "__main__":
    unittest.main()
