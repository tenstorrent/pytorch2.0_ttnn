import torch
import torch_ttnn
import ttnn
import unittest


class SoftmaxModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, axis):
        return torch.softmax(x, axis)

    def input_shapes(self):
        return [(1, 1, 64, 32)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_softmax(self):
        m = SoftmaxModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
        axis = -1
        result_before = m.forward(*inputs, axis)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(*inputs, axis)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.softmax)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))


if __name__ == "__main__":
    unittest.main()
