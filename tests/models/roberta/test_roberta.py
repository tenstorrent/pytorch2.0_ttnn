# Reference: https://huggingface.co/docs/transformers/en/model_doc/xlm-roberta#transformers.XLMRobertaForMaskedLM

from transformers import AutoTokenizer, XLMRobertaForMaskedLM
import torch
import pytest


@pytest.mark.compilation_xfail
def test_roberta(record_property):
    record_property("model_name", "RoBERTa")

    tokenizer = AutoTokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
    model = XLMRobertaForMaskedLM.from_pretrained("FacebookAI/xlm-roberta-base")

    inputs = tokenizer("The capital of France is <mask>.", return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    # retrieve index of <mask>
    mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

    predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
    output = tokenizer.decode(predicted_token_id)

    record_property("torch_ttnn", (model, inputs, outputs))
