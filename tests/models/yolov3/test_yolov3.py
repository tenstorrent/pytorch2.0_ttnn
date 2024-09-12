# Reference: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/yolo_v3/pytorch_yolov3_holli.py

import torch
from PIL import Image
from torchvision import transforms
import requests
from pathlib import Path
import pytest

from tests.models.yolov3.holli_src.yolov3 import *


@pytest.mark.compilation_xfail
def test_yolov3(record_property):
    record_property("model_name", "YOLOv3")

    # Download model weights
    url = "https://www.ollihuotari.com/data/yolov3_pytorch/yolov3_coco_01.h5"

    download_dir = Path.home() / ".cache/custom_weights"
    download_dir.mkdir(parents=True, exist_ok=True)

    load_path = download_dir / url.split("/")[-1]
    if not load_path.exists():
        response = requests.get(url, stream=True)
        with open(str(load_path), "wb") as f:
            f.write(response.content)

    # Load model
    model = Yolov3(num_classes=80)
    model.load_state_dict(
        torch.load(
            str(load_path),
            map_location=torch.device("cpu"),
        )
    )
    model.eval()

    # Image preprocessing
    image_url = "https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg"
    image = Image.open(requests.get(image_url, stream=True).raw)
    transform = transforms.Compose([transforms.Resize((512, 512)), transforms.ToTensor()])
    img_tensor = [transform(image).unsqueeze(0)]
    batch_tensor = torch.cat(img_tensor, dim=0)

    predictions = model(batch_tensor)

    record_property("torch_ttnn", (model, batch_tensor, predictions))
