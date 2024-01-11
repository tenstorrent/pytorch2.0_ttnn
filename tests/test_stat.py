import os
import shutil
import torch
import torch_stat
import unittest
import json
from torch.fx.passes.dialect.common.cse_pass import CSEPass

class ConvModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels = 3,
                                    out_channels = 5,
                                    kernel_size = (3, 4),
                                    stride = (1, 2),
                                    padding = (2, 1),
                                    padding_mode = "zeros",
                                    dilation = (1, 3),
                                    groups = 1,
                                    bias = True)
    def forward(self, x):
        return self.conv(x)
    def input_shapes(self):
        return [(1, 3, 32, 32)]

class TestModules(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.out_path = os.path.join(os.getcwd(), ".test_stat")

    def setUp(self):
        shutil.rmtree(self.out_path, ignore_errors = True)

    def tearDown(self):
        shutil.rmtree(self.out_path, ignore_errors = True)

    def test_conv(self):
        m = ConvModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape) for shape in input_shapes]
        option = torch_stat.TorchStatOption(model_name = "conv",
                                            out = self.out_path,
                                            gen_graphviz=True)
        m = torch.compile(m, backend=torch_stat.backend(option))
        _ = m.forward(*inputs)
        fw_result_json_path = os.path.join(self.out_path, "raw", "fw_conv.json")
        fw_graphviz_path = os.path.join(self.out_path, "graphviz", "fw_conv.dot.svg")
        self.assertTrue(os.path.isfile(fw_result_json_path))
        self.assertTrue(os.path.isfile(fw_graphviz_path))

    def test_conv_backward(self):
        m = ConvModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, requires_grad=True) for shape in input_shapes]
        option = torch_stat.TorchStatOption(model_name = "conv_backward",
                                            out = self.out_path,
                                            gen_graphviz=True)
        m = torch.compile(m, backend=torch_stat.backend(option, backward = True))
        result = m.forward(*inputs)
        result.sum().backward()
        bw_result_json_path = os.path.join(self.out_path, "raw", "bw_conv_backward.json")
        bw_graphviz_path = os.path.join(self.out_path, "graphviz", "bw_conv_backward.dot.svg")
        self.assertTrue(os.path.isfile(bw_result_json_path))
        self.assertTrue(os.path.isfile(bw_graphviz_path))
