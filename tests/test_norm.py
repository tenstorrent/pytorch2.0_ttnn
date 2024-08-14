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
        def num_groups(self):
            return 3
        def input_shape(self):
            return (20, 6, 10, 10)
        def weight_shape(self):
            return (6)
        def bias_shape(self):
            return (6)

    class LayerNormModule(torch.nn.Module):
        def __init__(self):
            super().__init__()
        def forward(self, x, normalized_shape, **kwargs):
            return torch.layer_norm(x, normalized_shape, **kwargs)
        def normalized_shape(self):
            return (5, 10, 10)
        def input_shape(self):
            return (20, 5, 10, 10)
        def weight_shape(self):
            return (5, 10, 10)
        def bias_shape(self):
            return (5, 10, 10)

    def _test_norm(self, norm_type, weight=False, bias=False):
        if norm_type == "group":
            m = self.GroupNormModule()
            kwargs = {"num_groups": m.num_groups()}
        elif norm_type == "layer":
            m = self.LayerNormModule()
            kwargs = {"normalized_shape": m.normalized_shape()}
        input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
        if weight:
            kwargs["weight"] = torch.rand(m.weight_shape(), dtype=torch.bfloat16)
        if bias:
            kwargs["bias"] = torch.rand(m.bias_shape(), dtype=torch.bfloat16)
        result_before = m.forward(input, **kwargs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after = m.forward(input, **kwargs)
        option._out_fx_graphs[0].print_tabular()

        nodes = list(option._out_fx_graphs[0].nodes)
        # Check the graph has be rewritten and contain ttnn ops
        if weight == False and bias == False:
            self.assertTrue(nodes[1].target == ttnn.from_torch)
            self.assertTrue(nodes[2].target == ttnn.to_layout)
            self.assertTrue(nodes[3].target == ttnn.to_device)
            if norm_type == "group":
                self.assertTrue(nodes[4].target == ttnn.group_norm)
            elif norm_type == "layer":
                self.assertTrue(nodes[4].target == ttnn.layer_norm)
            self.assertTrue(nodes[5].target == ttnn.from_device)
            self.assertTrue(nodes[6].target == ttnn.to_layout)
            self.assertTrue(nodes[7].target == ttnn.to_torch)
        elif weight == True and bias == False:
            self.assertTrue(nodes[2].target == ttnn.from_torch)
            self.assertTrue(nodes[3].target == ttnn.to_layout)
            self.assertTrue(nodes[4].target == ttnn.to_device)
            self.assertTrue(nodes[5].target == ttnn.from_torch)
            self.assertTrue(nodes[6].target == ttnn.to_layout)
            self.assertTrue(nodes[7].target == ttnn.to_device)
            if norm_type == "group":
                self.assertTrue(nodes[8].target == ttnn.group_norm)
            elif norm_type == "layer":
                self.assertTrue(nodes[8].target == ttnn.layer_norm)
            self.assertTrue(nodes[9].target == ttnn.from_device)
            self.assertTrue(nodes[10].target == ttnn.to_layout)
            self.assertTrue(nodes[11].target == ttnn.to_torch)
        elif weight == True and bias == True:
            self.assertTrue(nodes[3].target == ttnn.from_torch)
            self.assertTrue(nodes[4].target == ttnn.to_layout)
            self.assertTrue(nodes[5].target == ttnn.to_device)
            self.assertTrue(nodes[6].target == ttnn.from_torch)
            self.assertTrue(nodes[7].target == ttnn.to_layout)
            self.assertTrue(nodes[8].target == ttnn.to_device)
            self.assertTrue(nodes[9].target == ttnn.from_torch)
            self.assertTrue(nodes[10].target == ttnn.to_layout)
            self.assertTrue(nodes[11].target == ttnn.to_device)
            if norm_type == "group":
                self.assertTrue(nodes[12].target == ttnn.group_norm)
            elif norm_type == "layer":
                self.assertTrue(nodes[12].target == ttnn.layer_norm)
            self.assertTrue(nodes[13].target == ttnn.from_device)
            self.assertTrue(nodes[14].target == ttnn.to_layout)
            self.assertTrue(nodes[15].target == ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))

    def _test_norm_many_times(self, norm_type):
        if norm_type == "group":
            m = self.GroupNormModule()
            kwargs = {"num_groups": m.num_groups()}
        elif norm_type == "layer":
            m = self.LayerNormModule()
            kwargs = {"normalized_shape": m.normalized_shape()}
        input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
        weight = torch.rand(m.weight_shape(), dtype=torch.bfloat16)
        bias = torch.rand(m.bias_shape(), dtype=torch.bfloat16)
        result_before1 = m.forward(input, **kwargs)
        result_before2 = m.forward(input, **kwargs, bias = bias)
        result_before3 = m.forward(input, **kwargs, weight = weight, bias = bias)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend="ttnn", options=option)
        result_after1 = m.forward(input, **kwargs)
        result_after2 = m.forward(input, **kwargs, bias = bias)
        result_after3 = m.forward(input, **kwargs, weight = weight, bias = bias)

        self.assertTrue(torch.allclose(result_before1, result_after1))
        self.assertTrue(torch.allclose(result_before2, result_after2))
        self.assertTrue(torch.allclose(result_before3, result_after3))

    def test_group_norm(self):
        self._test_norm("group")

    def test_group_norm_weight(self):
        self._test_norm("group", True)

    def test_group_norm_weight_bias(self):
        self._test_norm("group", True, True)

    def test_group_norm_many_times(self):
        self._test_norm_many_times("group")

    def test_layer_norm(self):
        self._test_norm("layer")

    def test_layer_norm_weight(self):
        self._test_norm("layer", True)

    def test_layer_norm_weight_bias(self):
        self._test_norm("layer", True, True)

    def test_layer_norm_many_times(self):
        self._test_norm_many_times("layer")

