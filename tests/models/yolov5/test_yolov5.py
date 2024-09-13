import torch
from PIL import Image
from torchvision import transforms
import requests
import pytest

dependencies = ["ultralytics==8.2.92", "ultralytics-thop==2.0.6", "opencv-python-headless==4.8.0.74"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_yolov5(record_property):
    record_property("model_name", "YOLOv5")

    """
    The model is from https://pytorch.org/hub/ultralytics_yolov5/
    """
    # Model
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, autoshape=False, device="cpu")

    # Image preprocessing
    image_url = "https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg"
    image = Image.open(requests.get(image_url, stream=True).raw)
    transform = transforms.Compose([transforms.Resize((512, 512)), transforms.ToTensor()])
    img_tensor = [transform(image).unsqueeze(0)]
    batch_tensor = torch.cat(img_tensor, dim=0)

    # Inference
    results = model(batch_tensor)

    record_property("torch_ttnn", (model, batch_tensor, results))
