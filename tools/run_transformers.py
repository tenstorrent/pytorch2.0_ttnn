import os
import argparse
import torch
# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, AutoModelForCausalLM

class TestModel():
    def __init__(self, model_name, model_task, test_input):
        self.model_name = model_name
        self.model_task = model_task
        self.test_input = test_input

def run_model(model: str, backend: str, backward: bool, out_path: str, graphviz: bool, to_profile: bool, device = None):

    tokenizer = AutoTokenizer.from_pretrained(model.model_name)
    m = model.model_task.from_pretrained(model.model_name)

    if backward:
        try:
            m.train()
        except:
            print(f"{model.model_name} Cannot to the training mode, use just eval mode")
            m.eval()
            backward = False
    else:
        m.eval()
    if backend == "torch_ttnn":
        option = torch_ttnn.TorchTtnnOption(device=device)
        m = torch.compile(m, backend=torch_ttnn.backend(option))
    elif backend == "torch_stat":
        option = torch_stat.TorchStatOption(model_name = model.model_name, backward = backward,
                                            out = out_path, gen_graphviz=graphviz)
        m = torch.compile(m, backend=torch_stat.backend(option))
    else:
        assert(0 and "Unsupport backend")

    if model.model_task == AutoModelForQuestionAnswering:
        inputs = tokenizer.encode_plus(model.test_input["question"], model.test_input["context"], add_special_tokens=True, return_tensors="pt")
    elif model.model_task == AutoModelForCausalLM:
        inputs = tokenizer.encode_plus(model.test_input, add_special_tokens=True, return_tensors="pt")
    else:
        raise ValueError(f"model task: {model.model_task} not supported.")

    if to_profile:
        from torch.profiler import profile, record_function, ProfilerActivity
        trace_file = os.path.join(out_path, "profile", model.model_name)
        os.makedirs(os.path.dirname(trace_file), exist_ok=True)
        activities = [ProfilerActivity.CPU]
        if torch.cuda.is_available():
            activities.append(ProfilerActivity.CUDA)
        with profile(activities=activities, record_shapes=True) as prof:
            # with torch.no_grad():
            #     results = m(**inputs)
            # if backward:
            #     result.backward(torch.ones_like(result))
            if model.model_task == AutoModelForQuestionAnswering:
                results = m(**inputs)
            elif model.model_task == AutoModelForCausalLM:
                # results = m.generate(**inputs, do_sample=True, max_length=30)
                results = m(**inputs)
        prof.export_chrome_trace(trace_file)
    else:
        with torch.no_grad():
            results = m(**inputs)
        # if backward:
        #     result.backward(torch.ones_like(result))

    if model.model_task == AutoModelForQuestionAnswering:
        response_start = torch.argmax(results.start_logits)
        response_end = torch.argmax(results.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        response = tokenizer.decode(response_tokens)
    elif model.model_task == AutoModelForCausalLM:
        response = ""
        # response = tokenizer.batch_decode(results, skip_special_tokens=True)
    else:
        raise ValueError(f"model task: {model.model_task} not supported.")

    print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_path", "-o", type = str, default = os.path.join(os.getcwd(),"stat"))
    parser.add_argument("--backend", type = str)
    parser.add_argument("--graphviz", action="store_true")
    parser.add_argument("--backward", action="store_true")
    parser.add_argument("--profile", action="store_true")
    args = parser.parse_args()
    assert(args.backend in ["torch_ttnn", "torch_stat"])
    if args.backend == "torch_ttnn" and args.backward:
        assert(0 and "torch_ttnn not yet support backward")

    if args.backend == "torch_ttnn":
        import torch_ttnn
    elif args.backend == "torch_stat":
        from torch_ttnn import torch_stat

    models = [
        # TestModel(
        #     "phiyodr/bert-large-finetuned-squad2",
        #     AutoModelForQuestionAnswering,
        #     {'question': 'What discipline did Winkelmann create?',
        #      'context': 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '}
        # ),
        TestModel(
            "tiiuae/falcon-7b-instruct",
            AutoModelForCausalLM,
            "Once upon a time"
        )
    ]

    device = torch_ttnn.ttnn.open_device(device_id = 0) if args.backend == "torch_ttnn" else None
    for m in models:
        try:
            run_model(m, args.backend, args.backward, args.out_path, args.graphviz, args.profile, device)
        except:
            print(f"{m} FAIL")
    if args.backend == "torch_ttnn":
        torch_ttnn.ttnn.close_device(device)