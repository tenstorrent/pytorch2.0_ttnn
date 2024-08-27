from transformers import T5Tokenizer, T5ForConditionalGeneration
import pytest


@pytest.mark.parametrize("model_name", ["t5-small", "t5-base", "t5-large"])
@pytest.mark.torch_only
def test_t5(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    input_text = "translate English to French: How are you?"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output_ids = model.generate(input_ids)

    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    print(f"Model: {model_name} | Input: {input_text} | Output: {output_text}")

    record_property("torch_ttnn", (model, input_ids, output_ids))
