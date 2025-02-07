from transformers import BeitImageProcessor, BeitForImageClassification
from PIL import Image
import requests
import pytest
import torch
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model = BeitForImageClassification.from_pretrained(self.model_name)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        processor = BeitImageProcessor.from_pretrained(self.model_name)
        inputs = processor(images=image, return_tensors="pt")
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs

    def set_inputs_train(self, inputs):
        inputs["pixel_values"].requires_grad_(True)
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs.logits)

    def get_results_train(self, model, inputs, outputs):
        return inputs["pixel_values"].grad


@pytest.mark.parametrize("mode", ["train", "eval"])
@pytest.mark.parametrize("model_name", ["microsoft/beit-base-patch16-224", "microsoft/beit-large-patch16-224"])
def test_beit_image_classification(record_property, model_name, mode, get_batch_size):
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size) # This is necessary to avoid shape mismatch errors in tester processing

    if mode == "eval":
        logits = results.logits

        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        print("Predicted class:", tester.model.config.id2label[predicted_class_idx])

    record_property("torch_ttnn", (tester, results))
