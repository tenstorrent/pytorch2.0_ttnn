# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForQuestionAnswering

from transformers import AutoTokenizer, AlbertForQuestionAnswering
import torch
import pytest
from tests.utils import ModelTester, validate_batch_size, process_batched_logits, batch_object_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model = AlbertForQuestionAnswering.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        return model

    def _load_inputs(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.question, self.text = "Who was Jim Henson?", "Jim Henson was a nice puppet"
        inputs = self.tokenizer(self.question, self.text, return_tensors="pt")
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
@pytest.mark.parametrize("model_name", ["twmkn9/albert-base-v2-squad2"])
def test_albert_question_answering(record_property, model_name, mode, get_batch_size):
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
        answer_start_index = process_batched_logits(results.start_logits, batch_size).argmax()
        answer_end_index = process_batched_logits(results.end_logits, batch_size).argmax()
        predict_answer_tokens = tester.inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        answer = tester.tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)

        print(f"Model: {model_name} | Question: {tester.question} | Text: {tester.text} | Answer: {answer}")

    record_property("torch_ttnn", (tester, results))
