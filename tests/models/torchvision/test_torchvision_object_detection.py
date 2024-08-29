from torchvision import models, transforms
from PIL import Image
import torch
import requests
import pytest


@pytest.mark.parametrize(
    "model_info",
    [
        ("ssd300_vgg16", "SSD300_VGG16_Weights"),
        ("ssdlite320_mobilenet_v3_large", "SSDLite320_MobileNet_V3_Large_Weights"),
        ("retinanet_resnet50_fpn", "RetinaNet_ResNet50_FPN_Weights"),
        ("retinanet_resnet50_fpn_v2", "RetinaNet_ResNet50_FPN_V2_Weights"),
    ],
)
@pytest.mark.compilation_xfail
def test_torchvision_object_detection(record_property, model_info):
    model_name, weights_name = model_info

    record_property("model_name", model_name)

    weights = getattr(models.detection, weights_name).DEFAULT
    model = getattr(models.detection, model_name)(weights=weights)
    model.eval()

    preprocess = weights.transforms()

    # Load and preprocess the image
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)

    with torch.no_grad():
        output = model(batch_t)

    print(f"Model: {model_name} | Output: {output}")

    record_property("torch_ttnn", (model, batch_t, output))
