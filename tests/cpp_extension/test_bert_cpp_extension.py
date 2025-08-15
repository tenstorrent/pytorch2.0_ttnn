import torch
import torch_ttnn
from torch_ttnn.cpp_extension import ttnn_module
import time
import pytest

from transformers import AutoTokenizer, AutoModelForQuestionAnswering


@pytest.mark.parametrize(
    "batch_size",
    (1, 8, 16),
)
def test_bert_with_cpp_extension(device, batch_size):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    m = m.eval()

    context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
    questions = [
        "What discipline did Winckelmann create?",
        "Where did Winckelmann originate?",
        "What was Winckelmann's occupation?",
        "What quote was attributed to Winckelmann?",
        "What movement did Winckelmann pioneer?",
    ]
    # Pre-generated answers from CPU run
    answers = [
        "scientific archaeology",
        "german",
        "art historian and archaeologist",
        "the difference between greek, greco - roman and roman art",
        "scientific archaeology",
    ]

    inputs = [
        tokenizer.encode_plus(
            q,
            context,
            add_special_tokens=True,
            return_tensors="pt",
            max_length=384,
            padding="max_length",
            truncation=True,
        )
        for q in questions
    ]

    option = torch_ttnn.TorchTtnnOption(
        device=device,
        gen_graphviz=False,
        run_mem_analysis=False,
        metrics_path=model_name,
        verbose=True,
        load_params_once=False,
    )

    # custom device
    ttnn_device = ttnn_module.as_torch_device(device)

    # clone input_ids on cpu since this the data transfer is somehow inplace?
    input_ids = inputs[0].input_ids.clone()

    # Helper function to decode output to human-readable text
    # Helper: decode logits to text
def decode_output(start_logits, end_logits, input_ids):
    # Step 1: move to CPU and handle dtype properly
    start_logits_cpu = start_logits[0]
    end_logits_cpu = end_logits[0]
    
    print(f"[DEBUG] start_logits device: {start_logits_cpu.device}")
    print(f"[DEBUG] start_logits dtype: {start_logits_cpu.dtype}")
    print(f"[DEBUG] end_logits device: {end_logits_cpu.device}")
    print(f"[DEBUG] end_logits dtype: {end_logits_cpu.dtype}")
    
    # Convert to CPU if on device - handle the dtype conversion properly
    if start_logits_cpu.device.type != 'cpu':
        # First convert to float32 on device, then move to CPU
        start_logits_cpu = start_logits_cpu.float().cpu()
    else:
        # If already on CPU, just convert dtype if needed
        if start_logits_cpu.dtype != torch.float32:
            start_logits_cpu = start_logits_cpu.float()
    
    if end_logits_cpu.device.type != 'cpu':
        # First convert to float32 on device, then move to CPU
        end_logits_cpu = end_logits_cpu.float().cpu()
    else:
        # If already on CPU, just convert dtype if needed
        if end_logits_cpu.dtype != torch.float32:
            end_logits_cpu = end_logits_cpu.float()
    
    print(f"[DEBUG] After conversion - start_logits dtype: {start_logits_cpu.dtype}")
    print(f"[DEBUG] After conversion - end_logits dtype: {end_logits_cpu.dtype}")

    # Step 2: find best span
    try:
        start_idx = int(torch.argmax(start_logits_cpu).item())
        end_idx = int(torch.argmax(end_logits_cpu).item()) + 1
        print(f"[DEBUG] start_idx: {start_idx}, end_idx: {end_idx}")
    except Exception as e:
        print(f"[DEBUG] Error in argmax: {e}")
        # Fallback to first token if argmax fails
        start_idx = 0
        end_idx = 1

    # Step 3: decode tokens to text
    return tokenizer.decode(input_ids[0][start_idx:end_idx])

    # comment out these to disable cpp extension
    start_to = time.perf_counter() * 1000
    # modules are inplace, tensors are not
    m.to(ttnn_device)
    end_to = time.perf_counter() * 1000
    print(f"model weights to ttnn time: {end_to - start_to} (ms)")

    model = torch.compile(m, backend=torch_ttnn.backend, options=option)

    # use torch.stack to artificially increase batch size
    for idx in range(len(inputs)):
        old_input = inputs[idx]
        for k, v in old_input.items():
            inputs[idx][k] = v.repeat(batch_size, 1)

    outputs = []

    for idx in range(len(inputs)):
        with torch.no_grad():
            start = time.perf_counter() * 1000
            inputs_dev = inputs[idx].to(ttnn_device)
            # Don't need to reset options if inputs don't change because of cache
            outputs.append(model(**inputs_dev))
            end = time.perf_counter() * 1000
            run_time = end - start
            print(f"iter {idx}: {run_time} (ms)")

    print(
        f"""
    model_name: {model_name}
    input:
        context: {context}
        """
    )
    for q, out, ea in zip(questions, outputs, answers):
        answer = decode_output(out)

        print(
            f"""
            question: {q}
            actual answer:   {answer}
            expected answer: {ea}
        """
        )
        assert ea == answer
