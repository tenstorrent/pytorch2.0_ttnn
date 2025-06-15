import torch
import ttnn  # For device management and conversion
import time
from torch_ttnn.cpp_extension import ttnn_module

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def run_bert_eager_mode(batch_size=1):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")

    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    model.eval()

    # Open TTNN device and map to torch
    device = ttnn.open_device(
        device_id=0,  # required
        l1_small_size=0,
        trace_region_size=0,
        dispatch_core_config=ttnn.DispatchCoreConfig(ttnn.DispatchCoreType.ETH),
        worker_l1_size=0
    )
    torch_device = ttnn_module.as_torch_device(device)
    model.to(torch_device)

    context = (
        "Johann Joachim Winckelmann was a German art historian and archaeologist. "
        "He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "
        "\"The prophet and founding hero of modern archaeology\", Winckelmann was one of the founders of scientific archaeology "
        "and first applied the categories of style on a large, systematic basis to the history of art."
    )
    questions = [
        "What discipline did Winckelmann create?",
        "Where did Winckelmann originate?",
        "What was Winckelmann's occupation?",
        "What quote was attributed to Winckelmann?",
        "What movement did Winckelmann pioneer?",
    ]
    expected_answers = [
        "scientific archaeology",
        "german",
        "art historian and archaeologist",
        "the difference between greek, greco - roman and roman art",
        "scientific archaeology",
    ]

    # Tokenize and prepare input batch
    inputs_list = []
    for question in questions:
        encoded = tokenizer.encode_plus(
            question,
            context,
            add_special_tokens=True,
            return_tensors="pt",
            max_length=384,
            padding="max_length",
            truncation=True,
        )
        # Expand batch dimension
        for key in encoded:
            encoded[key] = encoded[key].repeat(batch_size, 1)
        inputs_list.append(encoded)

    # Helper: decode logits to text
    def decode_output(start_logits, end_logits, input_ids):
        start_logits = start_logits[0]
        end_logits = end_logits[0]
        start_idx = torch.argmax(start_logits)
        end_idx = torch.argmax(end_logits) + 1
        return tokenizer.decode(input_ids[0][start_idx:end_idx])

    # Run inference
    for i, inputs in enumerate(inputs_list):
        input_ids_cpu = inputs["input_ids"].clone()
        inputs = {k: v.to(torch_device) for k, v in inputs.items()}
        with torch.no_grad():
            start = time.perf_counter() * 1000
            output = model(**inputs)
            end = time.perf_counter() * 1000
            print(f"Inference time (q{i}) on TTNN device: {end - start:.2f} ms")

        # Decode and check result
        answer = decode_output(output.start_logits, output.end_logits, input_ids_cpu)
        print(f"""
        Question:          {questions[i]}
        Answer (decoded):  {answer}
        Expected Answer:   {expected_answers[i]}
        """)
        assert expected_answers[i] == answer, "Mismatch in answer!"

if __name__ == "__main__":
    for bs in (1, 8, 16):
        print(f"\nRunning eager inference with batch size = {bs}")
        run_bert_eager_mode(batch_size=bs)
