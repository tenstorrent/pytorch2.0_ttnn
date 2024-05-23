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

    class GroupNormModule(torch.nn.Module):
        def __init__(self):
            super().__init__()
        def forward(self, x, num_groups, **kwargs):
            return torch.group_norm(x, num_groups, **kwargs)
        def input_shape(self):
            return (20, 6, 10, 10)
        def weight_shape(self):
            return (6)
        def bias_shape(self):
            return (6)

    def _test_group_norm(self, weight=False, bias=False):
        m = self.GroupNormModule()
        input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
        kwargs = {"num_groups": 3}
        if weight:
            kwargs["weight"] = torch.rand(m.weight_shape(), dtype=torch.bfloat16)
        if bias:
            kwargs["bias"] = torch.rand(m.bias_shape(), dtype=torch.bfloat16)
        result_before = m.forward(input, **kwargs)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(input, **kwargs)
        option._out_fx_graphs[0].print_tabular()

        nodes = list(option._out_fx_graphs[0].nodes)
        return result_before, result_after, nodes

    def test_group_norm(self):
        result_before, result_after, nodes = self._test_group_norm()
        # Check the graph has be rewritten and contain ttnn ops
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.group_norm)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_group_norm_weight(self):
        result_before, result_after, nodes = self._test_group_norm(True)
        # Check the graph has be rewritten and contain ttnn ops
        self.assertTrue(nodes[2].target == ttnn.from_torch)
        self.assertTrue(nodes[3].target == ttnn.to_layout)
        self.assertTrue(nodes[4].target == ttnn.to_device)
        self.assertTrue(nodes[5].target == ttnn.from_torch)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_device)
        self.assertTrue(nodes[8].target == ttnn.group_norm)
        self.assertTrue(nodes[9].target == ttnn.from_device)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_group_norm_weight_bias(self):
        result_before, result_after, nodes = self._test_group_norm(True, True)
        # Check the graph has be rewritten and contain ttnn ops
        self.assertTrue(nodes[3].target == ttnn.from_torch)
        self.assertTrue(nodes[4].target == ttnn.to_layout)
        self.assertTrue(nodes[5].target == ttnn.to_device)
        self.assertTrue(nodes[6].target == ttnn.from_torch)
        self.assertTrue(nodes[7].target == ttnn.to_layout)
        self.assertTrue(nodes[8].target == ttnn.to_device)
        self.assertTrue(nodes[9].target == ttnn.from_torch)
        self.assertTrue(nodes[10].target == ttnn.to_layout)
        self.assertTrue(nodes[11].target == ttnn.to_device)
        self.assertTrue(nodes[12].target == ttnn.group_norm)
        self.assertTrue(nodes[13].target == ttnn.from_device)
        self.assertTrue(nodes[14].target == ttnn.to_layout)
        self.assertTrue(nodes[15].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def test_group_norm_many_times(self):
        m = self.GroupNormModule()
        input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
        weight = torch.rand(m.weight_shape(), dtype=torch.bfloat16)
        bias = torch.rand(m.bias_shape(), dtype=torch.bfloat16)
        num_groups = 3
        result_before1 = m.forward(input, num_groups)
        result_before2 = m.forward(input, num_groups, bias = bias)
        result_before3 = m.forward(input, num_groups, weight = weight, bias = bias)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after1 = m.forward(input, num_groups)
        result_after2 = m.forward(input, num_groups, bias = bias)
        result_after3 = m.forward(input, num_groups, weight = weight, bias = bias)

        self.assertTrue(torch.allclose(result_before1, result_after1))
        self.assertTrue(torch.allclose(result_before2, result_after2))
        self.assertTrue(torch.allclose(result_before3, result_after3))


    class LayerNormModule(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, normalized_shape, weight=None, bias=None, eps=1e-05):
            return torch.layer_norm(x, normalized_shape, weight, bias, eps)

        def input_shape(self):
            return (20, 5, 10, 10)

    def test_layer_norm(self):
        m = self.LayerNormModule()
        input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
        normalized_shape = [5, 10, 10]
        result_before = m.forward(input, normalized_shape)
        option = torch_ttnn.TenstorrentBackendOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(input, normalized_shape)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        self.assertTrue(nodes[1].target == ttnn.from_torch)
        self.assertTrue(nodes[2].target == ttnn.to_layout)
        self.assertTrue(nodes[3].target == ttnn.to_device)
        self.assertTrue(nodes[4].target == ttnn.layer_norm)
        self.assertTrue(nodes[5].target == ttnn.from_device)
        self.assertTrue(nodes[6].target == ttnn.to_layout)
        self.assertTrue(nodes[7].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))
