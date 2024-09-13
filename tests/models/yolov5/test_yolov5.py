import torch
from PIL import Image
from torchvision import transforms
import requests
import subprocess
import sys
import pytest

dependencies = ["ultralytics==8.2.92", "ultralytics-thop==2.0.6"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_yolov5(record_property):
    record_property("model_name", "YOLOv5")

    """
    The model is from https://pytorch.org/hub/ultralytics_yolov5/
    """

    """
    Workaround!
    -----------
    We decided to install the Python package below within the test, rather than
    using the typical approach with the `dependencies` variable mentioned above.
    The reason is that we want to overwrite the dependencies installed by the
    standard method and ensure we are using the exact package specified below.
    If we don't, we may unintentionally use a package that requires GPU support.

    Here's the background: this test uses the YOLOv5 model from the `ultralytics`
    package, which we need to install. However, installing this package also
    pulls in a dependent package, `opencv-python`, which unfortunately requires
    GPU support. Fortunately, we found a lightweight alternative,
    `opencv-python-headless`, that does not require GPU support. Since we can't
    prevent the installation of the undesired package, we install the preferred
    one afterward to ensure it is being used. This is the most efficient
    workaround I can think of.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python-headless==4.8.0.74"])

    # Model
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, autoshape=False, device="cpu")

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "opencv-python-headless"])

    # Image preprocessing
    image_url = "https://raw.githubusercontent.com/pytorch/hub/master/images/dog.jpg"
    image = Image.open(requests.get(image_url, stream=True).raw)
    transform = transforms.Compose([transforms.Resize((512, 512)), transforms.ToTensor()])
    img_tensor = [transform(image).unsqueeze(0)]
    batch_tensor = torch.cat(img_tensor, dim=0)

    # Inference
    results = model(batch_tensor)

    record_property("torch_ttnn", (model, batch_tensor, results))
