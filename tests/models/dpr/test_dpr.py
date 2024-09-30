# Reference: https://huggingface.co/facebook/dpr-reader-single-nq-base

from transformers import DPRReader, DPRReaderTokenizer
import pytest
from tests.utils import ModelTester
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = DPRReaderTokenizer.from_pretrained("facebook/dpr-reader-single-nq-base")
        model = DPRReader.from_pretrained("facebook/dpr-reader-single-nq-base")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        encoded_inputs = self.tokenizer(
            questions=["What is love ?"],
            titles=["Haddaway"],
            texts=["'What Is Love' is a song recorded by the artist Haddaway"],
            return_tensors="pt",
        )
        return encoded_inputs

    def set_inputs_train(self, inputs):
        # inputs all are int tensor, cannot calculate grad
        return inputs

    def append_fake_loss_function(self, outputs):
        return torch.mean(outputs.start_logits) + torch.mean(outputs.end_logits) + torch.mean(outputs.relevance_logits)

    # TODO: inputs cannot calculate grad, need to find other tensor to calculate training accuracy
    # def get_results_train(self, model, inputs, outputs):
    #     return


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
@pytest.mark.compilation_xfail
def test_dpr(record_property, mode):
    model_name = "DPR"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        start_logits = results.start_logits
        end_logits = results.end_logits
        relevance_logits = results.relevance_logits
        print(results)

    record_property("torch_ttnn", (tester, results))
