import torch
import torch_ttnn
from torch_ttnn.cpp_extension.ttnn_device_mode import ttnn_module
import time

from transformers import AutoTokenizer, AutoModelForQuestionAnswering


def test_bert_with_cpp_extension(device):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
    questions = [
        "What discipline did Winckelmann create?",
        "Where did Winckelmann originate?",
        "What was Winckelmann's occupation?",
        "What quote was attributed to Winckelmann?",
        "What movement did Winckelmann pioneer?",
    ]

    inputs = [
        tokenizer.encode_plus(
            q,
            context,
            add_special_tokens=True,
            return_tensors="pt",
            max_length=256,
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
    )

    # custom device
    # torch.utils.rename_privateuse1_backend("ttnn")
    ttnn_device = ttnn_module.as_torch_device(device)

    # clone input_ids on cpu since this the data transfer is somehow inplace?
    input_ids = inputs[0].input_ids.clone()

    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    # comment out these to disable cpp extension
    start_to = time.perf_counter() * 1000
    # inputs = inputs.to(ttnn_device)
    # modules are inplace, tensors are not
    m.to(ttnn_device)
    end_to = time.perf_counter() * 1000
    print(f"to: {end_to - start_to} (ms)")

    model = torch.compile(m, backend=torch_ttnn.backend, options=option)

    outputs = []
    for idx in range(5):
        start = time.perf_counter() * 1000
        inputs_dev = inputs[idx].to(ttnn_device)
        # inputs_dev = inputs[idx]
        # Don't need to reset options if inputs don't change because of cache
        outputs.append(model(**inputs_dev))
        end = time.perf_counter() * 1000
        run_time = end - start
        print(f"iter {idx}: {run_time} (ms)")

    # print("finished:")
    # print(outputs)

    print(
        f"""
    model_name: {model_name}
    input:
        context: {context}
        """
    )
    for q, out in zip(questions, outputs):
        answer = decode_output(out)

        print(
            f"""
            question: {q}
            answer: {answer}
        """
        )
