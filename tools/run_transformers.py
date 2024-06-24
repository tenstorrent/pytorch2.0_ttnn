import os
import argparse
import torch
from PIL import Image
import requests

# Load model directly
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoImageProcessor,
    AutoModelForObjectDetection,
)

class TestModel():
    def __init__(self, model_name, model_task, test_input):
        self.model_name = model_name
        self.model_task = model_task
        self.test_input = test_input
    def __repr__(self):
        return self.model_name

def run_model(model: str, backend: str, backward: bool, out_path: str, graphviz: bool, to_profile: bool, device = None):

    text_modules = [
        AutoModelForQuestionAnswering,
        AutoModelForCausalLM,
        AutoModelForSequenceClassification
    ]
    vision_modules = [
        AutoModelForObjectDetection,
    ]

    if model.model_task in text_modules:
        tokenizer = AutoTokenizer.from_pretrained(model.model_name, padding_side="left")
    elif model.model_task in vision_modules:
        image_processor = AutoImageProcessor.from_pretrained(model.model_name)
    else:
        raise ValueError(f"model task: {model.model_task} not supported.")

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
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    elif backend == "torch_stat":
        option = torch_stat.TorchStatOption(model_name = model.model_name, backward = backward,
                                            out = out_path, gen_graphviz=graphviz)
        m = torch.compile(m, backend=torch_stat.backend(option))
    else:
        assert(0 and "Unsupport backend")

    if model.model_task == AutoModelForQuestionAnswering:
        inputs = tokenizer.encode_plus(
            model.test_input["question"],
            model.test_input["context"],
            add_special_tokens=True,
            return_tensors="pt",
            max_length=256,
            padding="max_length",
            truncation=True
        )
    elif (
        model.model_task == AutoModelForCausalLM or 
        model.model_task == AutoModelForSequenceClassification
    ):
        inputs = tokenizer(model.test_input, return_tensors="pt")
    elif model.model_task == AutoModelForObjectDetection:
        image = Image.open(requests.get(model.test_input, stream=True).raw)
        inputs = image_processor(images=image, return_tensors="pt")
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
            with torch.no_grad():
                outputs = m(**inputs)
            # if backward:
            #     result.backward(torch.ones_like(result))
        prof.export_chrome_trace(trace_file)
    else:
        with torch.no_grad():
            outputs = m(**inputs)
            if backend == "torch_ttnn":
                option._out_fx_graphs[0].print_tabular()
        # if backward:
        #     result.backward(torch.ones_like(result))

    if model.model_task == AutoModelForQuestionAnswering:
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        result = tokenizer.decode(response_tokens)
    elif model.model_task == AutoModelForCausalLM:
        next_token_logits = outputs.logits[:, -1]
        next_token = next_token_logits.softmax(dim=-1).argmax()
        result = tokenizer.decode([next_token])
    elif model.model_task == AutoModelForSequenceClassification:
        normalized = outputs.logits.softmax(dim=-1)
        print(normalized)
        result = normalized.argmax().item()
    elif model.model_task == AutoModelForObjectDetection:
        target_sizes = torch.tensor([image.size[::-1]])
        results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[0]
    else:
        raise ValueError(f"model task: {model.model_task} not supported.")

    if model.model_task in text_modules:
        print(f"model_name: {model.model_name}\ninput: {model.test_input}\nresult: {result}")
    elif model.model_task in vision_modules:
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            print(
                f"Detected {m.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )
    else:
        raise ValueError(f"model task: {model.model_task} not supported.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type = str, required = True)
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
        TestModel(
            "phiyodr/bert-large-finetuned-squad2",
            AutoModelForQuestionAnswering,
            {'question': 'What discipline did Winkelmann create?',
             'context': 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '}
        ),
        TestModel(
            "tiiuae/falcon-7b-instruct",
            AutoModelForCausalLM,
            "Once upon a time"
        ),
        TestModel(
            "mistralai/Mistral-7B-Instruct-v0.2",
            AutoModelForCausalLM,
            "My name is Johnny Appleseed, and today I"
        ),
        TestModel(
            "bigscience/bloom-1b1",
            AutoModelForCausalLM,
            "My cat and my dog"
        ),
        # Need torch 2.3.0+
        TestModel(
            "state-spaces/mamba-130m-hf",
            AutoModelForCausalLM,
            "Hey how are you doing?"
        ),
        TestModel(
            "huggyllama/llama-7b",
            AutoModelForCausalLM,
            "Spring is a good time to"
        ),
        TestModel(
            "mnoukhov/gpt2-imdb-sentiment-classifier",
            AutoModelForSequenceClassification,
            'This is the kind of movie you put in the background while working on other things.'
        ),
        TestModel(
            "hustvl/yolos-tiny",
            AutoModelForObjectDetection,
            "http://images.cocodataset.org/val2017/000000039769.jpg"
        ),
    ]
    def get_model(model_name):
        for m in models:
            if model_name == m.model_name:
                return m
        raise ValueError(f"model: {model_name} not supported. Supported models: {models}")

    device = torch_ttnn.ttnn.open_device(device_id = 0) if args.backend == "torch_ttnn" else None
    run_model(get_model(args.model), args.backend, args.backward, args.out_path, args.graphviz, args.profile, device)
    if args.backend == "torch_ttnn":
        torch_ttnn.ttnn.close_device(device)