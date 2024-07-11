import torch
import torch_ttnn
import unittest
import ttnn
import tt_lib

from tests.utils import check_with_pcc


class TransposeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, dim0, dim1):
        return torch.transpose(x, dim0, dim1)

    # Constraint: Last dim of input should be even.
    # If not, this runtime error will be thrown:
    # RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:41: page_size % sizeof(uint32_t) == 0
    def input_shapes(self):
        return [(5, 3, 2), 0, 2]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)
        # For AutoFormat
        tt_lib.device.SetDefaultDevice(self.device)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_transpose(self):
        m = TransposeModule()
        input_shapes = m.input_shapes()
        input = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        dim0 = input_shapes[1]
        dim1 = input_shapes[2]
        result_before = m.forward(input, dim0, dim1)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(input, dim0, dim1)
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


if __name__ == "__main__":
    unittest.main()
