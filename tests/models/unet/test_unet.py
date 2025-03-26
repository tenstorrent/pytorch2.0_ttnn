# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://pytorch.org/hub/mateuszbuda_brain-segmentation-pytorch_unet/

import numpy as np
from PIL import Image
from os import path
from torchvision import transforms
import requests
import torch
import pytest
from tests.utils import ModelTester, get_cached_image_or_reload


class ThisTester(ModelTester):
    def _load_model(self):
        model = torch.hub.load(
            "mateuszbuda/brain-segmentation-pytorch",
            "unet",
            in_channels=3,
            out_channels=1,
            init_features=32,
            pretrained=True,
            skip_validation=True,
        )
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        image_file = get_cached_image_or_reload(
            cache_path="/mnt/tt-metal-pytorch-cache/.cache/inputs/TCGA_CS_4944.png",
            url="https://github.com/mateuszbuda/brain-segmentation-pytorch/raw/master/assets/TCGA_CS_4944.png",
        )
        input_image = Image.open(image_file)
        m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
        preprocess = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(mean=m, std=s),
            ]
        )
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)
        input_batch = input_batch.to(torch.bfloat16)
        return input_batch


@pytest.mark.parametrize(
    "mode",
    [
        "train",
        pytest.param("eval", marks=pytest.mark.converted_end_to_end),
    ],
)
def test_unet(record_property, mode):
    model_name = "U-Net"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        results = torch.round(results[0])

    record_property("torch_ttnn", (tester, results))
