# Reference: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        return model

    def _load_inputs(self):
        # prepare image + question
        url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(url, stream=True).raw)
        text = "How many cats are there?"
        # prepare inputs
        encoding = self.processor(image, text, return_tensors="pt")
        return encoding


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_vilt(record_property, mode):
    model_name = "ViLT"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        logits = results.logits
        idx = logits.argmax(-1).item()
        print("Predicted answer:", tester.model.config.id2label[idx])

    record_property("torch_ttnn", (tester, results))
