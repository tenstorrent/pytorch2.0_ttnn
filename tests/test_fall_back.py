import torch
import torch_ttnn
<<<<<<< HEAD
import ttnn
import unittest
=======
import pytest
import ttnn

from tests.utils import check_with_pcc
>>>>>>> upstream/main


@pytest.mark.parametrize(
    "input_shapes",
    [[(4, 4), (4, 4)]],
)
def test_fall_back(device, input_shapes):
    class MixModule(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y):
            z = torch.div(x, y)
            z = torch.add(z, z)
            z = torch.matmul(z, z)
            z = torch.div(z, z)
            z = torch.div(z, z)
            return z

    m = MixModule()
    inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
    result_before = m.forward(*inputs)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(*inputs)
    assert 1 == len(option._out_fx_graphs)
    option._out_fx_graphs[0].print_tabular()

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)
    target = [node.target for node in nodes]
    assert target.count(ttnn.reciprocal) == 3
    assert target.count(ttnn.mul) == 3
    assert target.count(ttnn.add) == 1
    assert target.count(ttnn.matmul) == 1

<<<<<<< HEAD
class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_fall_back(self):
        m = MixModule()
        input_shapes = m.input_shapes()
        inputs = [torch.rand(shape, dtype=torch.bfloat16) for shape in input_shapes]
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
        self.assertEqual(nodes[2].target, torch.ops.aten.div.Tensor)
        self.assertEqual(nodes[3 + 0].target, ttnn.from_torch)
        self.assertEqual(nodes[3 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[3 + 2].target, ttnn.to_device)
        self.assertEqual(nodes[3 + 3].target, ttnn.to_layout)
        self.assertEqual(nodes[3 + 4].target, ttnn.to_device)
        self.assertEqual(nodes[8].target, ttnn.add)
        self.assertEqual(nodes[9].target, ttnn.matmul)
        self.assertEqual(nodes[10 + 0].target, ttnn.from_device)
        self.assertEqual(nodes[10 + 1].target, ttnn.to_layout)
        self.assertEqual(nodes[10 + 2].target, ttnn.to_torch)
        # Check inference result
        self.assertTrue(torch.allclose(result_before, result_after))
=======
    nodes = list(option._out_fx_graphs[-1].nodes)
    reciprocal_idx = [i for i, n in enumerate(target) if n == ttnn.reciprocal]
    multiply_idx = [i for i, n in enumerate(target) if n == ttnn.multiply]
    assert len(reciprocal_idx) == len(multiply_idx)
    for ri, mi in zip(reciprocal_idx, multiply_idx):
        assert ri < mi
    add_idx = target.index(ttnn.add)
    assert add_idx > multiply_idx[0]
    assert add_idx < multiply_idx[1]
    assert add_idx < multiply_idx[2]
    matmul_idx = target.index(ttnn.matmul)
    assert matmul_idx > multiply_idx[0]
    assert matmul_idx > add_idx
    assert matmul_idx < multiply_idx[1]
    assert matmul_idx < multiply_idx[2]

    # Check inference result
    assert check_with_pcc(result_before, result_after)
>>>>>>> upstream/main
