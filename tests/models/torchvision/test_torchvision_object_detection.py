# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from torchvision import models, transforms
from PIL import Image
import torch
import requests
import pytest
from tests.utils import ModelTester, repeat_inputs


# TODO: RuntimeError: "nms_kernel" not implemented for 'BFloat16'
class ThisTester(ModelTester):
    # pass model_info instead of model_name
    def __init__(self, model_info, mode, batch_size=1):
        if mode not in ["train", "eval"]:
            raise ValueError(f"Current mode is not supported: {mode}")
        self.model_info = model_info
        self.mode = mode
        self.model = self._load_model()
        self.inputs = self._load_inputs(batch_size)

    def _load_model(self):
        model_name, weights_name = self.model_info
        self.weights = getattr(models.detection, weights_name).DEFAULT
        model = getattr(models.detection, model_name)(weights=self.weights)  # .to(torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        preprocess = self.weights.transforms()
        # Load and preprocess the image
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        img_t = preprocess(image)
        batch_t = torch.unsqueeze(img_t, 0)  # .to(torch.bfloat16)
        batch_t = repeat_inputs(batch_t, batch_size)
        return batch_t


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize(
    "model_info",
    [
        ("ssd300_vgg16", "SSD300_VGG16_Weights"),
        ("ssdlite320_mobilenet_v3_large", "SSDLite320_MobileNet_V3_Large_Weights"),
        pytest.param(
            ("retinanet_resnet50_fpn", "RetinaNet_ResNet50_FPN_Weights"),
            marks=pytest.mark.skip(reason="https://github.com/tenstorrent/pytorch2.0_ttnn/issues/866"),
        ),
        pytest.param(
            ("retinanet_resnet50_fpn_v2", "RetinaNet_ResNet50_FPN_V2_Weights"),
            marks=pytest.mark.skip(reason="https://github.com/tenstorrent/pytorch2.0_ttnn/issues/866"),
        ),
    ],
)
def test_torchvision_object_detection(record_property, model_info, mode):
    model_name, _ = model_info
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_info, mode)
    results = tester.test_model()
    if mode == "eval":
        print(f"Model: {model_name} | Output: {results}")

    record_property("torch_ttnn", (tester, results))
