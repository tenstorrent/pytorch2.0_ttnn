# Reference: https://huggingface.co/deepmind/language-perceiver

from transformers import PerceiverTokenizer, PerceiverForMaskedLM
import pytest


@pytest.mark.compilation_xfail
def test_perceiver_io(record_property):
    record_property("model_name", "Perceiver IO")

    tokenizer = PerceiverTokenizer.from_pretrained("deepmind/language-perceiver")
    model = PerceiverForMaskedLM.from_pretrained("deepmind/language-perceiver")

    text = "This is an incomplete sentence where some words are missing."
    # prepare input
    encoding = tokenizer(text, padding="max_length", return_tensors="pt")
    # mask " missing.". Note that the model performs much better if the masked span starts with a space.
    encoding.input_ids[0, 52:61] = tokenizer.mask_token_id
    ######inputs, input_mask = encoding.input_ids.to(device), encoding.attention_mask.to(device)

    arguments = {"inputs": encoding.input_ids, "attention_mask": encoding.attention_mask}
    # forward pass
    outputs = model(**arguments)
    logits = outputs.logits
    masked_tokens_predictions = logits[0, 51:61].argmax(dim=-1)
    print(tokenizer.decode(masked_tokens_predictions))

    record_property("torch_ttnn", (model, arguments, outputs))
