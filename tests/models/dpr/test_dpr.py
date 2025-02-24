# Reference: https://huggingface.co/facebook/dpr-reader-single-nq-base

from transformers import DPRReader, DPRReaderTokenizer
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = DPRReaderTokenizer.from_pretrained("facebook/dpr-reader-single-nq-base")
        model = DPRReader.from_pretrained("facebook/dpr-reader-single-nq-base", torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        encoded_inputs = self.tokenizer(
            questions=["What is love ?"],
            titles=["Haddaway"],
            texts=["'What Is Love' is a song recorded by the artist Haddaway"],
            return_tensors="pt",
        )
        return encoded_inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_dpr(record_property, mode, get_batch_size):
    model_name = "DPR"
    record_property("model_name", model_name)
    record_property("mode", mode)

    batch_size = get_batch_size
    if batch_size is not None:
        batch_size = int(batch_size)
    validate_batch_size(batch_size)

    tester = ThisTester(model_name, mode)
    results = tester.test_model(batch_size=batch_size)
    batch_object_inputs(tester, batch_size)  # This is necessary to avoid shape mismatch errors in tester processing

    if mode == "eval":
        start_logits = results.start_logits
        end_logits = results.end_logits
        relevance_logits = results.relevance_logits
        print(results)

    record_property("torch_ttnn", (tester, results))
