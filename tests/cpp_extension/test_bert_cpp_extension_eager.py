import torch
import ttnn
import time
from torch_ttnn.cpp_extension import ttnn_module
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


def run_bert_eager_mode(batch_size=1):
    model_name = "bert-large-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")

    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    model.eval()

    device = ttnn.open_device(
        device_id=0,
        l1_small_size=0,
        trace_region_size=0,
        dispatch_core_config=ttnn.DispatchCoreConfig(ttnn.DispatchCoreType.ETH),
        worker_l1_size=0
    )
    torch_device = ttnn_module.as_torch_device(device)
    model = model.to(dtype=torch.bfloat16)
    model = model.to(torch_device)

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
        for key in encoded:
            encoded[key] = encoded[key].repeat(batch_size, 1)
        inputs_list.append(encoded)

    def decode_output(start_logits, end_logits, input_ids, attention_mask):
        start_logits = start_logits[0]
        end_logits = end_logits[0]
        input_ids = input_ids[0]
        attention_mask = attention_mask[0]

        invalid_mask = (attention_mask == 0)
        start_logits[invalid_mask] = float("-inf")
        end_logits[invalid_mask] = float("-inf")

        start_idx = int(torch.argmax(start_logits))
        end_idx = int(torch.argmax(end_logits))

        if end_idx < start_idx:
            end_idx = start_idx
        end_idx = min(end_idx, input_ids.shape[0] - 1)

        answer_tokens = input_ids[start_idx:end_idx + 1]

        answer = tokenizer.decode(answer_tokens, skip_special_tokens=True).strip().lower()

        if not answer:
            for window in [5, 10, 15]:
                start_alt = max(0, start_idx - window)
                end_alt = min(input_ids.shape[0], start_idx + window)
                alt_tokens = input_ids[start_alt:end_alt]
                alt_answer = tokenizer.decode(alt_tokens, skip_special_tokens=True).strip().lower()
                if alt_answer and len(alt_answer) > 3:
                    return alt_answer
        return answer

    for i, inputs in enumerate(inputs_list):
        input_ids_cpu = inputs["input_ids"].clone()
        attention_mask_cpu = inputs["attention_mask"].clone()

        inputs = {k: v.to(torch_device, dtype=torch.bfloat16) for k, v in inputs.items()}

        with torch.no_grad():
            start = time.perf_counter() * 1000
            output = model(**inputs)
            end = time.perf_counter() * 1000

        start_logits_cpu = output.start_logits.cpu()
        end_logits_cpu = output.end_logits.cpu()

        answer = decode_output(start_logits_cpu, end_logits_cpu, input_ids_cpu, attention_mask_cpu)

        print(f"Question: {questions[i]}")
        print(f"Answer (decoded): {answer}")
        print(f"Expected Answer: {expected_answers[i]}")

        if expected_answers[i].lower() not in answer:
            print(f"Warning: Expected answer '{expected_answers[i]}' not found in decoded answer")
        
        print("")

    try:
        ttnn.close_device(device)
        print("Device closed successfully")
    except Exception as e:
        print(f"Error closing device: {e}")


if __name__ == "__main__":
    try:
        for bs in (1,):
            print(f"\nRunning eager inference with batch size = {bs}")
            run_bert_eager_mode(batch_size=bs)
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
