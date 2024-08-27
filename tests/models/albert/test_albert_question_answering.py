# Reference: https://huggingface.co/docs/transformers/v4.44.2/en/model_doc/albert#transformers.AlbertForQuestionAnswering

from transformers import AutoTokenizer, AlbertForQuestionAnswering
import torch
import pytest


@pytest.mark.parametrize("model_name", ["twmkn9/albert-base-v2-squad2"])
@pytest.mark.compilation_xfail
def test_albert_question_answering(record_property, model_name):
    record_property("model_name", model_name)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AlbertForQuestionAnswering.from_pretrained(model_name)

    question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"

    inputs = tokenizer(question, text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs)

    answer_start_index = output.start_logits.argmax()
    answer_end_index = output.end_logits.argmax()

    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    answer = tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)

    print(f"Model: {model_name} | Question: {question} | Text: {text} | Answer: {answer}")

    record_property("torch_ttnn", (model, inputs, output))
