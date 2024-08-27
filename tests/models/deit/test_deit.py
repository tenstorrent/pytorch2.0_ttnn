# Reference: https://huggingface.co/facebook/deit-base-patch16-224

from transformers import AutoFeatureExtractor, ViTForImageClassification
from PIL import Image
import requests
import torch
import pytest


@pytest.mark.parametrize("model_name", ["facebook/deit-base-patch16-224"])
@pytest.mark.torch_only
def test_deit(record_property, model_name):
    record_property("model_name", model_name)

    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)
    inputs = feature_extractor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    print("Predicted class:", model.config.id2label[predicted_class_idx])

    record_property("torch_ttnn", (model, inputs, outputs))
