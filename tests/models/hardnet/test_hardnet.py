# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://pytorch.org/hub/pytorch_vision_hardnet/
# Reference: https://github.com/PingoLH/Pytorch-HarDNet

from PIL import Image
from torchvision import transforms
import requests
import torch
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model = torch.hub.load("PingoLH/Pytorch-HarDNet", "hardnet68", pretrained=False, skip_validation=True)
        checkpoint = "https://github.com/PingoLH/Pytorch-HarDNet/raw/refs/heads/master/hardnet68.pth"
        model.load_state_dict(torch.hub.load_state_dict_from_url(checkpoint, progress=False, map_location="cpu"))
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        url = "https://github.com/mateuszbuda/brain-segmentation-pytorch/raw/master/assets/TCGA_CS_4944.png"
        input_image = Image.open(requests.get(url, stream=True).raw)
        preprocess = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model
        input_batch = input_batch.to(torch.bfloat16)
        input_batch = repeat_inputs(input_batch, batch_size)
        return input_batch


@pytest.mark.parametrize(
    "mode",
    [
        "train",
        pytest.param("eval", marks=pytest.mark.converted_end_to_end),
    ],
)
def test_hardnet(record_property, mode, cached_results):
    model_name = "HardNet"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        # Tensor of shape 1000, with confidence scores over ImageNet's 1000 classes
        print(results[0])
        # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
        probabilities = torch.nn.functional.softmax(results[0], dim=0)
        print(probabilities)

    record_property("torch_ttnn", (tester, results))
