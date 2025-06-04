# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import requests
import torchvision.models as models
from torchvision import transforms
from PIL import Image

import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Load the MobileNetV2 model with updated API
        self.weights = models.MobileNet_V2_Weights.DEFAULT
        model = models.mobilenet_v2(weights=self.weights)
        return model.to(torch.bfloat16)

    def _load_inputs(self, batch_size):
        # Define a transformation to preprocess the input image using the weights transforms
        preprocess = self.weights.transforms()

        # Load and preprocess the image
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        img_t = preprocess(image)
        batch_t = torch.unsqueeze(img_t, 0)

        # TODO: get unique data instead of just repeating
        batch_t = repeat_inputs(batch_t, batch_size)

        return batch_t.to(torch.bfloat16)


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_MobileNetV2(record_property, mode):
    model_name = "MobileNetV2"
    record_property("model_name", model_name)
    record_property("mode", mode)
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
