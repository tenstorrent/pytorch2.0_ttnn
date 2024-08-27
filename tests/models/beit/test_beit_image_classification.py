from transformers import BeitImageProcessor, BeitForImageClassification
from PIL import Image
import requests
import pytest


@pytest.mark.parametrize("model_name", ["microsoft/beit-base-patch16-224", "microsoft/beit-large-patch16-224"])
@pytest.mark.torch_only
def test_beit_image_classification(record_property, model_name):
    record_property("model_name", model_name)

    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(url, stream=True).raw)

    processor = BeitImageProcessor.from_pretrained(model_name)
    model = BeitForImageClassification.from_pretrained(model_name)

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    print("Predicted class:", model.config.id2label[predicted_class_idx])

    record_property("torch_ttnn", (model, inputs, outputs))
