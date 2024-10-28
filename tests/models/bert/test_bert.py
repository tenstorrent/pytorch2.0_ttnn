import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "phiyodr/bert-large-finetuned-squad2"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return m

    def _load_inputs(self):
        # Set up sample input
        self.context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
        self.question = "What discipline did Winkelmann create?"
        inputs = self.tokenizer.encode_plus(
            self.question,
            self.context,
            add_special_tokens=True,
            return_tensors="pt",
            max_length=256,
            padding="max_length",
            truncation=True,
        )
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_bert(record_property, mode):
    model_name = "BERT"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            response_start = torch.argmax(outputs.start_logits)
            response_end = torch.argmax(outputs.end_logits) + 1
            response_tokens = tester.inputs.input_ids[0, response_start:response_end]
            return tester.tokenizer.decode(response_tokens)

        answer = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input:
            context: {tester.context}
            question: {tester.question}
        answer: {answer}
        """
        )

    record_property("torch_ttnn", (tester, results))
