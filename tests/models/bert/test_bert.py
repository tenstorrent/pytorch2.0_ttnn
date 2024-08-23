import torch

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


def test_bert(record_property):
    record_property("model_name", "BERT")

    # Download model from cloud
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    m.eval()

    # Set up sample input
    context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
    question = "What discipline did Winkelmann create?"

    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )

    # Run inference with the original model
    with torch.no_grad():
        outputs = m(**inputs)

    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    answer = decode_output(outputs)

    print(
        f"""
    model_name: {model_name}
    input:
        context: {context}
        question: {question}
    answer: {answer}
    """
    )

    record_property("torch_ttnn", (m, inputs, outputs))
