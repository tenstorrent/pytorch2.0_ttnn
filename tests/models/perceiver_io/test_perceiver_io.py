# Reference: https://huggingface.co/deepmind/language-perceiver

from transformers import PerceiverTokenizer, PerceiverForMaskedLM
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = PerceiverTokenizer.from_pretrained("deepmind/language-perceiver")
        model = PerceiverForMaskedLM.from_pretrained("deepmind/language-perceiver")
        return model

    def _load_inputs(self):
        text = "This is an incomplete sentence where some words are missing."
        # prepare input
        encoding = self.tokenizer(text, padding="max_length", return_tensors="pt")
        # mask " missing.". Note that the model performs much better if the masked span starts with a space.
        encoding.input_ids[0, 52:61] = self.tokenizer.mask_token_id
        ######inputs, input_mask = encoding.input_ids.to(device), encoding.attention_mask.to(device)

        arguments = {"inputs": encoding.input_ids, "attention_mask": encoding.attention_mask}
        return arguments


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_perceiver_io(record_property, mode):
    model_name = "Perceiver IO"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        logits = results.logits
        masked_tokens_predictions = logits[0, 51:61].argmax(dim=-1)
        print(tester.tokenizer.decode(masked_tokens_predictions))

    record_property("torch_ttnn", (tester, results))
