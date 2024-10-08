# Reference: https://huggingface.co/facebook/deit-base-patch16-224

from transformers import AutoFeatureExtractor, ViTForImageClassification
from PIL import Image
import requests
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(self.model_name)
        model = ViTForImageClassification.from_pretrained(self.model_name)
        return model

    def _load_inputs(self):
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        inputs = self.feature_extractor(images=image, return_tensors="pt")
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize("model_name", ["facebook/deit-base-patch16-224"])
@pytest.mark.compilation_xfail
def test_deit(record_property, model_name, mode):
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        logits = results.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        print("Predicted class:", tester.model.config.id2label[predicted_class_idx])

    record_property("torch_ttnn", (tester, results))
