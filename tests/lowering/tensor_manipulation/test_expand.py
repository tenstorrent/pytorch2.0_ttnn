import torch
import torch_ttnn
import unittest
import ttnn
import tt_lib
from torch_ttnn.utils import (
    TtnnRowMajorLayout,
    TtnnTileLayout,
)


class ExpandModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        return x.expand(new_shape)

    def input_shapes(self):
        return [(1, 4), (4, 4)]


class ExpandAfterOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        a = torch.clone(x)
        return a.expand(new_shape)

    def input_shapes(self):
        return [(1, 4), (4, 4)]


class ExpandBeforeOpModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        ex = x.expand(new_shape)
        return torch.add(ex, ex)

    def input_shapes(self):
        return [(1, 4), (4, 4)]


class ExpandBetweenOpsModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, new_shape):
        a = torch.clone(x)
        ex = a.expand(new_shape)
        return torch.add(ex, ex)

    def input_shapes(self):
        return [(1, 4), (4, 4)]


class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)
        # For AutoFormat
        tt_lib.device.SetDefaultDevice(self.device)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_expand(self):
        m = ExpandModule()
        input_shapes = m.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        new_shape = input_shapes[1]
        inputs = [tensor, new_shape]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        target = [node.target for node in nodes]
        self.assertTrue(target.count(ttnn.repeat) == 1)
        self.assertTrue(nodes[target.index(ttnn.repeat)].args[1].target == ttnn.Shape)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_expand_after_op(self):
        m = ExpandAfterOpModule()
        input_shapes = m.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        new_shape = input_shapes[1]
        inputs = [tensor, new_shape]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        target = [node.target for node in nodes]
        self.assertTrue(target.count(ttnn.repeat) == 1)
        repeat_node = nodes[target.index(ttnn.repeat)]
        self.assertTrue(repeat_node.args[0].target == ttnn.to_layout)
        self.assertTrue(repeat_node.args[0].args[0].target == ttnn.clone)
        self.assertTrue(type(repeat_node.args[0].args[1]) is type(TtnnRowMajorLayout()))
        self.assertTrue(repeat_node.args[1].target == ttnn.Shape)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_expand_before_op(self):
        m = ExpandBeforeOpModule()
        input_shapes = m.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        new_shape = input_shapes[1]
        inputs = [tensor, new_shape]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        target = [node.target for node in nodes]
        self.assertTrue(target.count(ttnn.repeat) == 1)
        self.assertTrue(nodes[target.index(ttnn.repeat)].args[1].target == ttnn.Shape)
        # to_layout that follows ttnn.repeat
        to_layout_idx = target.index(ttnn.to_layout, target.index(ttnn.repeat))
        to_layout_node = nodes[to_layout_idx]
        self.assertTrue(to_layout_node.args[0].target == ttnn.repeat)
        self.assertTrue(type(to_layout_node.args[1]) is type(TtnnTileLayout()))
        self.assertTrue(target.count(ttnn.add) == 1)
        self.assertTrue(to_layout_idx < target.index(ttnn.add))

        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))

    def test_expand_between_ops(self):
        m = ExpandBetweenOpsModule()
        input_shapes = m.input_shapes()
        tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
        new_shape = input_shapes[1]
        inputs = [tensor, new_shape]
        result_before = m.forward(*inputs)
        option = torch_ttnn.TorchTtnnOption(device=self.device)
        option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        result_after = m.forward(*inputs)
        option._out_fx_graphs[0].print_tabular()

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        target = [node.target for node in nodes]
        self.assertTrue(target.count(ttnn.repeat) == 1)
        repeat_node = nodes[target.index(ttnn.repeat)]
        self.assertTrue(repeat_node.args[0].target == ttnn.to_layout)
        self.assertTrue(repeat_node.args[0].args[0].target == ttnn.clone)
        self.assertTrue(type(repeat_node.args[0].args[1]) is type(TtnnRowMajorLayout()))
        self.assertTrue(repeat_node.args[1].target == ttnn.Shape)
        # to_layout that follows ttnn.repeat
        to_layout_idx = target.index(ttnn.to_layout, target.index(ttnn.repeat))
        to_layout_node = nodes[to_layout_idx]
        self.assertTrue(to_layout_node.args[0].target == ttnn.repeat)
        self.assertTrue(type(to_layout_node.args[1]) is type(TtnnTileLayout()))
        self.assertTrue(target.count(ttnn.add) == 1)
        self.assertTrue(to_layout_idx < target.index(ttnn.add))
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after, rtol=0.2))


if __name__ == "__main__":
    unittest.main()
