# Reference: https://huggingface.co/docs/transformers/en/model_doc/xlm-roberta#transformers.XLMRobertaForMaskedLM

from transformers import AutoTokenizer, XLMRobertaForMaskedLM
import torch
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
        model = XLMRobertaForMaskedLM.from_pretrained("FacebookAI/xlm-roberta-base", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        inputs = self.tokenizer("The capital of France is <mask>.", return_tensors="pt")
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_roberta(record_property, mode, get_batch_size):
    model_name = "RoBERTa"
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    else:
        batch_size = 165  # Max batch size found
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)
    if mode == "eval":
        logits = results.logits
        # retrieve index of <mask>
        mask_token_index = (tester.inputs.input_ids == tester.tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

        predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
        output = tester.tokenizer.decode(predicted_token_id)

    record_property("torch_ttnn", (tester, results))
