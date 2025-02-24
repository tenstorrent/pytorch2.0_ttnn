import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image

import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Load the ResNet-50 model with updated API
        self.weights = models.ResNet50_Weights.DEFAULT
        model = models.resnet50(weights=self.weights)
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
    [
        "train",
        pytest.param("eval", marks=pytest.mark.converted_end_to_end),
    ],
)
def test_resnet(record_property, mode, get_batch_size):
    model_name = "ResNet50"
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    else:
        batch_size = 8  # Max batch size found
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)
    if mode == "eval":
        # Print the top 5 predictions
        _, indices = torch.topk(results, 5)
        print(f"Top 5 predictions: {indices[0].tolist()}")

    record_property("torch_ttnn", (tester, results))


# Empty property record_property
def empty_record_property(a, b):
    pass


# Run pytorch implementation
if __name__ == "__main__":
    test_resnet(empty_record_property)
