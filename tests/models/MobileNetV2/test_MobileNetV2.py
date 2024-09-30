import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image

import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        # Load the MobileNetV2 model with updated API
        self.weights = models.MobileNet_V2_Weights.DEFAULT
        model = models.mobilenet_v2(weights=self.weights)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        # Define a transformation to preprocess the input image using the weights transforms
        preprocess = self.weights.transforms()

        # Load and preprocess the image
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        img_t = preprocess(image)
        batch_t = torch.unsqueeze(img_t, 0)
        batch_t = batch_t.to(torch.bfloat16)
        return batch_t


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
@pytest.mark.compilation_xfail
def test_MobileNetV2(record_property, mode):
    model_name = "MobileNetV2"
    record_property("model_name", f"{model_name} {mode}")
    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        # Print the top 5 predictions
        _, indices = torch.topk(results, 5)
        print(f"Top 5 predictions: {indices[0].tolist()}")

    record_property("torch_ttnn", (tester, results))


# Empty property record_property
def empty_record_property(a, b):
    pass


# Main
if __name__ == "__main__":
    test_MobileNetV2(empty_record_property)
