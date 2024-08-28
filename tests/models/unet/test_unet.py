# Reference: https://pytorch.org/hub/mateuszbuda_brain-segmentation-pytorch_unet/

import numpy as np
from PIL import Image
from torchvision import transforms
import requests
import torch
import pytest


@pytest.mark.compilation_xfail
def test_unet(record_property):
    record_property("model_name", "U-Net")

    url = "https://github.com/mateuszbuda/brain-segmentation-pytorch/raw/master/assets/TCGA_CS_4944.png"
    input_image = Image.open(requests.get(url, stream=True).raw)

    m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
    preprocess = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=m, std=s),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    model = torch.hub.load(
        "mateuszbuda/brain-segmentation-pytorch",
        "unet",
        in_channels=3,
        out_channels=1,
        init_features=32,
        pretrained=True,
    )
    with torch.no_grad():
        output = model(input_batch)

    results = torch.round(output[0])

    record_property("torch_ttnn", (model, input_batch, output))
