import os
import shutil
import torch
import torchvision
import torch_stat
import unittest

class TestModules(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.out_path = os.path.join(os.getcwd(), ".test_stat")

    def setUp(self):
        shutil.rmtree(self.out_path, ignore_errors = True)

    def tearDown(self):
        shutil.rmtree(self.out_path, ignore_errors = True)

    def test_alexnet(self):
        m = torchvision.models.get_model("alexnet", pretrained=False)
        m.eval()
        input_shapes = [1,3,224,224]
        inputs = torch.rand(input_shapes, dtype=torch.float32)
        option = torch_stat.TorchStatOption(model_name = "alexnet", 
                                            out = self.out_path)
        m = torch.compile(m, backend=torch_stat.backend(option))
        _ = m.forward(inputs)
        result_json = os.path.join(self.out_path, "raw", "alexnet_0.json")
        self.assertTrue(os.path.isfile(result_json))
