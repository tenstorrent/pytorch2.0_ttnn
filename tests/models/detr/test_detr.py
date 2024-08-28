from PIL import Image
import requests
import torch
import numpy as np
from torchvision import transforms
import pytest


@pytest.mark.compilation_xfail
def test_detr(record_property):
    record_property("model_name", "DETR")

    """
    The model is from https://github.com/facebookresearch/detr
    """
    # Model
    model = torch.hub.load("facebookresearch/detr:main", "detr_resnet50", pretrained=True)

    # Images
    img_url = "https://ultralytics.com/images/zidane.jpg"  # batch of images
    input_image = Image.open(requests.get(img_url, stream=True).raw)
    m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
    preprocess = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=m, std=s),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    # Inference
    results = model(input_batch)

    # Results
    print(results)

    record_property("torch_ttnn", (model, input_batch, results))
