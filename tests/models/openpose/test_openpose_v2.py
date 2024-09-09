# Reference: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/openpose/pytorch_lwopenpose_2d_osmr.py

import requests
import torch
from PIL import Image
from pytorchcv.model_provider import get_model as ptcv_get_model
from torchvision import transforms
import pytest


def get_image_tensor():
    # Image processing
    url = "https://raw.githubusercontent.com/axinc-ai/ailia-models/master/pose_estimation_3d/blazepose-fullbody/girl-5204299_640.jpg"
    input_image = Image.open(requests.get(url, stream=True).raw)
    preprocess = transforms.Compose(
        [
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model
    return input_batch


@pytest.mark.compilation_xfail
def test_openpose_v2(record_property):
    record_property("model_name", "OpenPose")

    # Create PyBuda module from PyTorch model
    model = ptcv_get_model("lwopenpose2d_mobilenet_cmupan_coco", pretrained=True)
    model.eval()

    input_batch = [get_image_tensor()]
    batch_input = torch.cat(input_batch, dim=0)

    # Run inference on Tenstorrent device
    output = model(batch_input)

    # Print output
    print(f"Output: {output}")

    record_property("torch_ttnn", (model, batch_input, output))
