# Reference: https://huggingface.co/facebook/dpr-reader-single-nq-base

from transformers import DPRReader, DPRReaderTokenizer
import pytest
from tests.utils import ModelTester
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
@pytest.mark.compilation_xfail
def test_dpr(record_property, mode):
    model_name = "DPR"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        start_logits = results.start_logits
        end_logits = results.end_logits
        relevance_logits = results.relevance_logits
        print(results)

    record_property("torch_ttnn", (tester, results))
