from transformers import T5Tokenizer, T5ForConditionalGeneration
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        return model

    def _load_inputs(self):
        self.input_text = "translate English to French: How are you?"
        input_ids = self.tokenizer.encode(self.input_text, return_tensors="pt")
        return input_ids

    def run_model(self, model, inputs):
        output_ids = model.generate(inputs)
        return output_ids


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.parametrize("model_name", ["t5-small", "t5-base", "t5-large"])
@pytest.mark.compilation_xfail
def test_t5(record_property, model_name, mode):
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        output_text = tester.tokenizer.decode(results[0], skip_special_tokens=True)
        print(f"Model: {model_name} | Input: {tester.input_text} | Output: {output_text}")

    record_property("torch_ttnn", (tester, results))
