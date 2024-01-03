import torch
import torchvision
import torch_ttnn
import unittest
from torch_ttnn import ttnn

class TestModules(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open(0)

    def tearDown(self):
        # Close the device
        ttnn.close(self.device)
    
    def template(self, model_name: str, input_shapes: list, source: str = "torchvision"):
        if source == "torchvision":
            m = torchvision.models.get_model(model_name, pretrained=True)
        elif source == "torch.hub.dinov2":
            m = torch.hub.load('facebookresearch/dinov2', model_name)
        else:
            assert(0 and "unsupport source")
        m.eval()
        input_shapes = input_shapes
        inputs = torch.rand(input_shapes, dtype=torch.float32)
        # inputs = torch.rand(input_shapes, dtype=torch.bfloat16)
        option = torch_ttnn.TorchTtnnOption(device=self.device,
                                            enable_stat = True,
                                            model_name = model_name)
        result_before = m.forward(inputs)
        m = torch.compile(m, backend=torch_ttnn.backend(option))
        # m = torch.compile(m)
        result_after = m.forward(inputs)
        # self.assertTrue(torch.allclose(result_before, result_after))

    def test_dinov2(self):
        self.template("dinov2_vits14", [1,3,224,224], "torch.hub.dinov2")

for m in torchvision.models.list_models():
    setattr(TestModules, f"test_{m}", lambda self, model_name = m: self.template(model_name, [1,3,224,224]))
