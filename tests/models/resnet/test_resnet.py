import torch
import torchvision
import torch_ttnn
import unittest
import ttnn
import collections
from torch_ttnn.utils import RunTimeMetrics
from tests.utils import check_with_pcc


class TestRestNet(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_resnet(self):
        # Download model from cloud
        model = torchvision.models.get_model("resnet18", pretrained=True)
        model.eval()
        model = model.to(torch.bfloat16)

        # Create random input tensor
        input_batch = torch.rand((1, 3, 224, 224), dtype=torch.bfloat16)

        metrics_path = "ResNet18"
        # Run inference with the original model
        with torch.no_grad():
            output_before = RunTimeMetrics(
                metrics_path, "original", lambda: model(input_batch)
            )

        # Compile the model
        option = torch_ttnn.TorchTtnnOption(
            device=self.device, metrics_path=metrics_path
        )
        option.gen_graphviz = True
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)

        # Run inference with the compiled model
        with torch.no_grad():
            output_after = RunTimeMetrics(
                metrics_path, "compiled", lambda: model(input_batch)
            )
        option._out_fx_graphs[0].print_tabular()

        # TODO: Check the graph has be rewritten and contain ttnn ops

        # Check inference result
        self.assertTrue(check_with_pcc(output_before, output_after))
