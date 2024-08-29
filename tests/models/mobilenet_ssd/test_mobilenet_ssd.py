# Reference: https://pytorch.org/vision/stable/models/generated/torchvision.models.detection.ssdlite320_mobilenet_v3_large.html
# Image URL from: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/mobilenet_ssd/tflite_mobilenet_v2_ssd_1x1.py

import torchvision
import torch
from PIL import Image
from torchvision import transforms
import requests
import pytest


@pytest.mark.compilation_xfail
def test_mobilenet_ssd(record_property):
    record_property("model_name", "MobileNetSSD")

    model = torchvision.models.detection.ssdlite320_mobilenet_v3_large(
        weights=torchvision.models.detection.SSDLite320_MobileNet_V3_Large_Weights.DEFAULT
    )
    model.eval()

    # Image preprocessing
    image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(image_url, stream=True).raw)
    transform = transforms.Compose([transforms.Resize((320, 320)), transforms.ToTensor()])
    img_tensor = [transform(image).unsqueeze(0)]
    batch_tensor = torch.cat(img_tensor, dim=0)

    predictions = model(batch_tensor)

    record_property("torch_ttnn", (model, batch_tensor, predictions))
