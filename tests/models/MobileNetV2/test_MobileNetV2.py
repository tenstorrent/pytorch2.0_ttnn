import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image

import pytest


@pytest.mark.compilation_xfail
def test_MobileNetV2(record_property):
    record_property("model_name", "MobileNetV2")

    # Load the MobileNetV2 model with updated API
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)
    model.eval()  # Set the model to evaluation mode

    # Define a transformation to preprocess the input image using the weights transforms
    preprocess = weights.transforms()

    # Load and preprocess the image
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)

    # Perform inference
    with torch.no_grad():
        output = model(batch_t)

    # Print the top 5 predictions
    _, indices = torch.topk(output, 5)
    print(f"Top 5 predictions: {indices[0].tolist()}")

    record_property("torch_ttnn", (model, batch_t, output))


# Empty property record_property
def empty_record_property(a, b):
    pass


# Main
if __name__ == "__main__":
    test_MobileNetV2(empty_record_property)
