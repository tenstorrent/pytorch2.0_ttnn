# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/docs/transformers/en/model_doc/squeezebert#transformers.SqueezeBertForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16)
        model = AutoModelForSequenceClassification.from_pretrained(
            "squeezebert/squeezebert-mnli", torch_dtype=torch.bfloat16
        )
        return model

    def _load_inputs(self, batch_size):
        inputs = self.tokenizer("Hello, my dog is cute", return_tensors="pt")
        inputs = repeat_inputs(inputs, batch_size)
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_squeeze_bert(record_property, mode, request, cached_results):
    # FIXME: https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1176
    if int(request.config.getoption("--report_nth_iteration")) > 1:
        pytest.skip("Error when enabled with run_once")

    model_name = "SqueezeBERT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = cached_results
    if results is None:
        results = tester.test_model()
    if mode == "eval":
        logits = results.logits
        predicted_class_id = logits.argmax().item()

    record_property("torch_ttnn", (tester, results))
