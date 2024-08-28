import urllib
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
import pytest


@pytest.mark.compilation_xfail
def test_unet_brain(record_property):
    record_property("model_name", "Unet-brain")

    """
    Test UNet for brain MRI segmentation
    The model is from https://pytorch.org/hub/mateuszbuda_brain-segmentation-pytorch_unet/
    """
    model = torch.hub.load(
        "mateuszbuda/brain-segmentation-pytorch",
        "unet",
        in_channels=3,
        out_channels=1,
        init_features=32,
        pretrained=True,
    )

    url, filename = (
        "https://github.com/mateuszbuda/brain-segmentation-pytorch/raw/master/assets/TCGA_CS_4944.png",
        "TCGA_CS_4944.png",
    )
    try:
        urllib.URLopener().retrieve(url, filename)
    except:
        urllib.request.urlretrieve(url, filename)

    input_image = Image.open(filename)
    m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
    preprocess = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=m, std=s),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    print(torch.round(output[0]))

    record_property("torch_ttnn", (model, input_batch, output))
