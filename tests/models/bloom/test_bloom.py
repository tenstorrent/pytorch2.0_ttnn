import torch
import pytest

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "bigscience/bloom-1b1"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
        m = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return m

    def _load_inputs(self):
        # Set up sample input
        self.test_input = "This is a sample text from "
        inputs = self.tokenizer.encode_plus(
            self.test_input,
            return_tensors="pt",
            max_length=32,
            padding="max_length",
            add_special_tokens=True,
            truncation=True,
        )
        return inputs

    def set_inputs_train(self, inputs):
        # inputs all are int tensor, cannot calculate grad
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs.logits)

    # TODO: inputs cannot calculate grad, need to find other tensor to calculate training accuracy
    # def get_results_train(self, model, inputs, outputs):
    #     return


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
def test_bloom(record_property, mode):
    model_name = "Bloom"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            next_token_logits = outputs.logits[:, -1]
            next_token = next_token_logits.softmax(dim=-1).argmax()
            return tester.tokenizer.decode([next_token])

        decoded_output = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input: {tester.test_input}
        output: {decoded_output}
        """
        )

    record_property("torch_ttnn", (tester, results))
