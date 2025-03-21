import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image

import pytest
from tests.utils import ModelTester


# class ThisTester(ModelTester):
#     def _load_model(self):
#         # Load the MobileNetV2 model with updated API
#         self.weights = models.MobileNet_V2_Weights.DEFAULT
#         model = models.mobilenet_v2(weights=self.weights)
#         return model.to(torch.bfloat16)
#
#     def _load_inputs(self):
#         # Define a transformation to preprocess the input image using the weights transforms
#         preprocess = self.weights.transforms()
#
#         # Load and preprocess the image
#         url = "http://images.cocodataset.org/val2017/000000039769.jpg"
#         image = Image.open(requests.get(url, stream=True).raw)
#         img_t = preprocess(image)
#         batch_t = torch.unsqueeze(img_t, 0)
#         return batch_t.to(torch.bfloat16)
#
#
# @pytest.mark.parametrize(
#     "mode",
#     ["eval"],
# )
# @pytest.mark.converted_end_to_end
# def test_MobileNetV2(record_property, mode):
#     model_name = "MobileNetV2"
#     record_property("model_name", model_name)
#     record_property("mode", mode)
#     tester = ThisTester(model_name, mode)
#     results = tester.test_model()
#     if mode == "eval":
#         # Print the top 5 predictions
#         _, indices = torch.topk(results, 5)
#         print(f"Top 5 predictions: {indices[0].tolist()}")
#
#     record_property("torch_ttnn", (tester, results))


import torch
import torch_ttnn
import ttnn


class ConvModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(
            in_channels=3,
            out_channels=5,
            kernel_size=(3, 4),
            stride=(1, 2),
            padding=(2, 1),
            padding_mode="zeros",
            dilation=(1, 3),
            groups=1,
            bias=True,
        )

    def forward(self, x):
        return self.conv(x)

    def input_shapes(self):
        # B, C, H, W
        return [(2, 3, 32, 32)]


def test_conv():
    module = ConvModule().to(torch.bfloat16)
    input_shapes = module.input_shapes()
    inputs = [torch.rand(shape, requires_grad=True, dtype=torch.bfloat16) for shape in input_shapes]

    # Compile the module, with ttnn backend
    l1_small_size = 16384
    dispatch_core_config = ttnn.DispatchCoreConfig(ttnn.device.DispatchCoreType.ETH, ttnn.DispatchCoreAxis.ROW)
    mesh_device = ttnn.open_mesh_device(
        ttnn.MeshShape(1, 2), dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size
    )
    # mesh_device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size)
    try:
        option = torch_ttnn.TorchTtnnOption(device=mesh_device, gen_graphviz=False, data_parallel=True)
        ttnn_module = torch.compile(module, backend=torch_ttnn.backend, options=option)

        # Running inference / training
        output = ttnn_module(*inputs)
    finally:
        # Cleanup
        ttnn.synchronize_device(mesh_device)
        ttnn.close_mesh_device(mesh_device)
        # ttnn.close_device(mesh_device)


def do_mesh():
    # Create a module
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)
    module = model.to(torch.bfloat16)

    # Create input data
    preprocess = weights.transforms()
    # Load and preprocess the image
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)
    input_data = batch_t.to(torch.bfloat16)

    # Compile the module, with ttnn backend
    l1_small_size = 16384
    dispatch_core_config = ttnn.DispatchCoreConfig(ttnn.device.DispatchCoreType.ETH, ttnn.DispatchCoreAxis.ROW)
    mesh_device = ttnn.open_mesh_device(
        ttnn.MeshShape(1, 2), dispatch_core_config=dispatch_core_config, l1_small_size=l1_small_size
    )
    option = torch_ttnn.TorchTtnnOption(device=mesh_device)
    ttnn_module = torch.compile(module, backend=torch_ttnn.backend, options=option)

    # Running inference / training
    output = ttnn_module(input_data)

    # Cleanup
    ttnn.synchronize_device(mesh_device)
    ttnn.close_mesh_device(mesh_device)


def do_single():
    # Create a module
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)
    module = model.to(torch.bfloat16)

    # Create input data
    preprocess = weights.transforms()
    # Load and preprocess the image
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)
    input_data = batch_t.to(torch.bfloat16)

    # Compile the module, with ttnn backend
    device_id = 0
    l1_small_size = 16384
    dispatch_core_config = ttnn.DispatchCoreConfig(ttnn.device.DispatchCoreType.ETH, ttnn.DispatchCoreAxis.ROW)
    device = ttnn.open_device(device_id=device_id, dispatch_core_config=dispatch_core_config, l1_small_size=16384)

    option = torch_ttnn.TorchTtnnOption(device=device)
    ttnn_module = torch.compile(module, backend=torch_ttnn.backend, options=option)

    # Running inference / training
    output = ttnn_module(input_data)

    # Cleanup
    ttnn.synchronize_device(device)
    ttnn.close_device(device)


test_conv()
# do_mesh()
# do_single()
