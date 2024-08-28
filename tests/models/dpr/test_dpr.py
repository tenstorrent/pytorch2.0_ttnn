# Reference: https://huggingface.co/facebook/dpr-reader-single-nq-base

from transformers import DPRReader, DPRReaderTokenizer
import pytest


@pytest.mark.compilation_xfail
def test_dpr(record_property):
    record_property("model_name", "DPR")

    tokenizer = DPRReaderTokenizer.from_pretrained("facebook/dpr-reader-single-nq-base")
    model = DPRReader.from_pretrained("facebook/dpr-reader-single-nq-base")
    encoded_inputs = tokenizer(
        questions=["What is love ?"],
        titles=["Haddaway"],
        texts=["'What Is Love' is a song recorded by the artist Haddaway"],
        return_tensors="pt",
    )
    outputs = model(**encoded_inputs)
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits
    relevance_logits = outputs.relevance_logits
    print(outputs)

    record_property("torch_ttnn", (model, encoded_inputs, outputs))
