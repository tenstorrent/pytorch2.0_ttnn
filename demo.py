import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, AutoModelForCausalLM, set_seed
import torch_ttnn
import ttnn
import streamlit as st
import time
import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from PIL import Image
import torch.nn as nn
import torch.nn.functional as F
import io
import sys


def get_dispatch_core_type():
    return ttnn.device.DispatchCoreType.ETH


def get_dispatch_core_axis():
    return ttnn.DispatchCoreAxis.ROW


def get_dispatch_core_config():
    dispatch_core_type = get_dispatch_core_type()
    dispatch_core_axis = get_dispatch_core_axis()
    dispatch_core_config = ttnn.DispatchCoreConfig(dispatch_core_type, dispatch_core_axis)
    return dispatch_core_config


class MnistModel(torch.nn.Module):
    def __init__(self):
        super(MnistModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


def capture_output(func):
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        sys.stdout = output = io.StringIO()
        try:
            result = func(*args, **kwargs)
            output_str = output.getvalue()
            words = output_str.split()
            if len(words) > 200:
                output_str = " ".join(words[:200]) + " [Truncated...]"
            return result, output_str
        finally:
            sys.stdout = old_stdout

    return wrapper




@capture_output
def classify_mnist(use_ttnn=False, iterations=1):
    print("Loading MNIST dataset...")
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    mnist_test = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
    image, label = mnist_test[0]
    input_tensor = image.unsqueeze(0)
    print("Initializing MnistModel...")
    model = MnistModel()
    model.eval()
    for param in model.parameters():
        param.requires_grad = False
    display_image = (image * 0.3081) + 0.1307
    display_image = display_image.clamp(0, 1)
    st.image(display_image.squeeze().numpy(), caption=f"Sample MNIST Digit (Label: {label})", width=100)
    if use_ttnn:
        print("Opening TTNN device...")
        dispatch_core_config = get_dispatch_core_config()
        device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
        ttnn.enable_program_cache(device)
        print("Compiling model with TTNN...")
        option = torch_ttnn.TorchTtnnOption(device=device)
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        with torch.no_grad():
            for i in range(iterations - 1):
                _ = model(input_tensor)

    print(f"Running inference for {iterations} iterations...")
    start_time = time.time()
    logits = model(input_tensor)
    end_time = time.time()
    inference_time = end_time - start_time
    probabilities = torch.exp(logits)
    confidence, predicted_idx = torch.max(probabilities, 1)
    predicted_label = predicted_idx.item()
    confidence_score = confidence.item() * 100
    print(f"Prediction: {predicted_label}, Confidence: {confidence_score:.2f}% after {iterations} iterations")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return logits, predicted_label, confidence_score, inference_time

@capture_output
def ask_question(context, question, use_ttnn=True, iterations=1):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    print(f"Loading tokenizer and model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    print("Encoding inputs...")
    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )
    total_token_count = inputs["input_ids"].ne(tokenizer.pad_token_id).sum().item()  # Count non-padding tokens
    if use_ttnn:
        print("Opening TTNN device...")
        dispatch_core_config = get_dispatch_core_config()
        device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
        ttnn.enable_program_cache(device)
        print("Compiling model with TTNN...")
        option = torch_ttnn.TorchTtnnOption(device=device)
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        for i in range(iterations - 1):
            _ = model(**inputs)
    start_time = time.time()
    outputs = model(**inputs)
    end_time = time.time()
    inference_time = end_time - start_time

    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = inputs.input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    answer = decode_output(outputs)
    print(f"Answer: {answer}")
    print(f"Total tokens (context + question): {total_token_count}")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return answer, inference_time, total_token_count

@capture_output
def generate_text(prompt, max_length=500, num_return_sequences=1, use_ttnn=True, iterations=1):
    model_name = "gpt2"
    print(f"Loading tokenizer and model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id
    print("Encoding prompt...")
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )
    set_seed(42)
    if use_ttnn:
        print("Opening TTNN device...")
        dispatch_core_config = get_dispatch_core_config()
        device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
        ttnn.enable_program_cache(device)
        print("Compiling model with TTNN...")
        option = torch_ttnn.TorchTtnnOption(device=device)
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        print("Initial TTNN generation...")
        for i in range(iterations - 1):
            _ = model.generate(
                **inputs,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                do_sample=True,
            )
    print(f"Generating text for {iterations} iterations...")
    start_time = time.time()
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
    )
    num_generated_tokens = len(outputs[0])  # Count tokens in first sequence
    end_time = time.time()
    inference_time = end_time - start_time
    generated_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    print(f"Generated text (first sequence): {generated_texts[0][:100]}...")
    print(f"Generated tokens: {num_generated_tokens}")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return generated_texts, inference_time, num_generated_tokens

@capture_output
def generate_code(prompt, max_length=500, num_return_sequences=1, use_ttnn=True, iterations=1):
    model_name = "Salesforce/codegen-350M-mono"
    print(f"Loading tokenizer and model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id
    print("Encoding prompt...")
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )
    set_seed(42)
    if use_ttnn:
        print("Opening TTNN device...")
        dispatch_core_config = get_dispatch_core_config()
        device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
        ttnn.enable_program_cache(device)
        print("Compiling model with TTNN...")
        option = torch_ttnn.TorchTtnnOption(device=device)
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        print("Initial TTNN generation...")
        for i in range(iterations - 1):
            _ = model.generate(
                **inputs,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                do_sample=True,
            )
    print(f"Generating code for {iterations} iterations...")
    start_time = time.time()
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
    )
    num_generated_tokens = len(outputs[0])  # Count tokens in first sequence
    end_time = time.time()
    inference_time = end_time - start_time
    generated_codes = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    print(f"Generated code (first sequence): {generated_codes[0][:100]}...")
    print(f"Generated tokens: {num_generated_tokens}")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return generated_codes, inference_time, num_generated_tokens

@capture_output
def classify_image(image, use_ttnn=True, iterations=1):
    classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    print("Loading ResNet18 model...")
    model = models.resnet18(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 10)
    model.eval()
    print("Preprocessing image...")
    transform = transforms.Compose(
        [transforms.Resize((32, 32)), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    )
    input_tensor = transform(image).unsqueeze(0)
    if use_ttnn:
        print("Opening TTNN device...")
        dispatch_core_config = get_dispatch_core_config()
        device = ttnn.open_device(device_id=0, dispatch_core_config=dispatch_core_config, l1_small_size=16384)
        ttnn.enable_program_cache(device)
        print("Compiling model with TTNN...")
        option = torch_ttnn.TorchTtnnOption(device=device, bypass_compile=True)
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        for _ in range(iterations - 1):
            outputs = model(input_tensor)
    print(f"Running inference for {iterations} iterations...")
    start_time = time.time()
    outputs = model(input_tensor)
    end_time = time.time()
    inference_time = end_time - start_time
    probabilities = torch.nn.functional.softmax(outputs, dim=1)
    confidence, predicted_idx = torch.max(probabilities, 1)
    label = classes[predicted_idx.item()]
    confidence_score = confidence.item() * 100
    print(f"Predicted label: {label}, Confidence: {confidence_score:.2f}%")
    if use_ttnn:
        ttnn.close_device(device)
        print("TTNN device closed.")
    return label, confidence_score, inference_time

def stream_response(response):
    for char in response:
        yield char

def main():
    st.title("Compiler Performance Benchmark (models)")

    task = st.selectbox(
        "Select Task:",
        [
            "Question Answering with BERT",
            "Text Generation with GPT-2",
            "Image Classification with ResNet18",
            "MNIST Classification",
            "Code Generation with CodeGen",
        ],
    )

    st.subheader(f"About {task}")
    if task == "Question Answering with BERT":
        st.info(
            """
            **BERT**: Fine tuned for finding the answers to questions in a given context (SQuAD 2.0 https://rajpurkar.github.io/SQuAD-explorer/).
            **How to Use**: Set context and question, set iterations, then click "Run".
            **Note** Different length context-question pairs will give different performance (token/sec), all else being equal. Be sure to use the same prompt when comparing performance.
        """
        )
    elif task == "Text Generation with GPT-2":
        st.info(
            """
            **GPT-2**: Autoregressive model by OpenAI for text generation.
            **How to Use**: Edit prompt, set iterations, then click "Run".
            **Note** Different length prompts will give different performance (token/sec), all else being equal. Be sure to use the same prompt when comparing performance.
        """
        )
    elif task == "Image Classification with ResNet18":
        st.info(
            """
            **ResNet18**: CNN by Microsoft Research for image classification.
            **How to Use**: Select image, set iterations, then click "Run".
            **Note** This model is untrained and is not expected to give an accurate prediction.
        """
        )
    elif task == "MNIST Classification":
        st.info(
            """
            **MNIST Classification**: Custom CNN for MNIST digit classification.
            **How to Use**: Set iterations, click "Run" for a sample digit.
            **Note** This model is untrained and is not expected to give an accurate prediction.
        """
        )
    else:  # Code Generation with CodeGen
        st.info(
            """
            **CodeGen**: Salesforce model for Python code generation.
            **How to Use**: Edit prompt, set iterations, then click "Run".
            **Note** Different length prompts will give different performance (token/sec), all else being equal. Be sure to use the same prompt when comparing performance.
        """
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "context" not in st.session_state:
        st.session_state.context = "a corvette has a naturally aspirated V8 engine."
    if "default_prompt" not in st.session_state:
        st.session_state.default_prompt = {
            "Question Answering with BERT": "What kind of engine does a corvette have?",
            "Text Generation with GPT-2": "Can machines think?",
            "Code Generation with CodeGen": "def compile_ttnn():",
        }
    if "cifar10_samples" not in st.session_state and task == "Image Classification with ResNet18":
        cifar10_test = datasets.CIFAR10(root="./data", train=False, download=True)
        classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        st.session_state.cifar10_samples = {}
        for i in range(10):
            for img, label in cifar10_test:
                if label == i:
                    st.session_state.cifar10_samples[classes[i]] = img
                    break

    if task == "Question Answering with BERT":
        st.subheader("Provide Context")
        context_input = st.text_area("Context:", value=st.session_state.context, height=200, key="context_input")
        st.session_state.context = context_input
        prompt = st.text_input("Question:", value=st.session_state.default_prompt[task], key="bert_prompt")
    elif task == "Text Generation with GPT-2":
        prompt = st.text_input("Prompt:", value=st.session_state.default_prompt[task], key="gpt2_prompt")
    elif task == "Code Generation with CodeGen":
        prompt = st.text_input("Prompt:", value=st.session_state.default_prompt[task], key="codegen_prompt")
    elif task == "Image Classification with ResNet18":
        st.subheader("Select an Image")
        image_choice = st.selectbox("Choose a CIFAR-10 image:", list(st.session_state.cifar10_samples.keys()))
        selected_image = st.session_state.cifar10_samples[image_choice]
        st.image(selected_image, caption=image_choice, width=100)
        prompt = "Classify Image"
    else:  # MNIST Classification
        prompt = "Classify MNIST Digit"

    iterations = st.number_input("Number of Iterations:", min_value=1, value=5, step=1, format="%d")
    test_cpu = st.checkbox("Get CPU performance in addition to TTNN", value=True)
    run_button = st.button("Run")

    st.subheader("Chat History")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.subheader("Process Output")
    terminal_output = st.text_area("Terminal", value="No process output yet.", height=100, disabled=True)

    if run_button:
        if task == "Question Answering with BERT" and not st.session_state.context:
            st.error("Please provide context via text before asking a question.")
        else:
            user_input = prompt if isinstance(prompt, str) else prompt
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": f"{user_input} (Iterations: {iterations}{', CPU Tested' if test_cpu else ''})",
                }
            )
            with st.chat_message("user"):
                st.markdown(f"{user_input} (Iterations: {iterations}{', CPU Tested' if test_cpu else ''})")

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                if task == "Question Answering with BERT":
                    (ttnn_answer, ttnn_time, ttnn_total_tokens), ttnn_output = ask_question(
                        st.session_state.context, prompt, use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_answer, cpu_time, cpu_total_tokens), cpu_output = ask_question(
                            st.session_state.context, prompt, use_ttnn=False, iterations=iterations
                        )
                    for chunk in stream_response(ttnn_answer):
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                    terminal_output_value = f"TTNN:\n{ttnn_output}"
                    if test_cpu:
                        terminal_output_value += f"\n\nCPU:\n{cpu_output}"
                    terminal_output = st.text_area(
                        "Terminal",
                        value=terminal_output_value,
                        height=100,
                        disabled=True,
                    )
                    ttnn_tokens_per_sec = ttnn_total_tokens / ttnn_time if ttnn_time > 0 else float("inf")
                    if test_cpu:
                        cpu_tokens_per_sec = cpu_total_tokens / cpu_time if cpu_time > 0 else float("inf")
                        speedup = (
                            ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
                        )
                        response_with_metrics = (
                            f"{full_response}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}\n"
                            f"CPU Time: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}\n"
                            f"Speedup: {speedup:.3f}x (Tokens/Sec, after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = (
                            f"{full_response}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}"
                        )
                elif task == "Text Generation with GPT-2":
                    (ttnn_outputs, ttnn_time, ttnn_tokens), ttnn_output = generate_text(
                        prompt, max_length=500, num_return_sequences=2, use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_outputs, cpu_time, cpu_tokens), cpu_output = generate_text(
                            prompt, max_length=500, num_return_sequences=2, use_ttnn=False, iterations=iterations
                        )
                    for chunk in stream_response(ttnn_outputs[0]):
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                    st.write("**Generated Texts (TTNN):**")
                    for i, text in enumerate(ttnn_outputs):
                        st.write(f"Sequence {i+1}: {text}")
                    terminal_output_value = f"TTNN:\n{ttnn_output}"
                    if test_cpu:
                        terminal_output_value += f"\n\nCPU:\n{cpu_output}"
                    terminal_output = st.text_area(
                        "Terminal",
                        value=terminal_output_value,
                        height=100,
                        disabled=True,
                    )
                    ttnn_tokens_per_sec = ttnn_tokens / ttnn_time if ttnn_time > 0 else float("inf")
                    if test_cpu:
                        cpu_tokens_per_sec = cpu_tokens / cpu_time if cpu_time > 0 else float("inf")
                        speedup = (
                            ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
                        )
                        response_with_metrics = (
                            f"{ttnn_outputs[0]}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}\n"
                            f"CPU Time: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}\n"
                            f"Speedup: {speedup:.3f}x (Tokens/Sec, after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = (
                            f"{ttnn_outputs[0]}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}"
                        )
                elif task == "Code Generation with CodeGen":
                    (ttnn_outputs, ttnn_time, ttnn_tokens), ttnn_output = generate_code(
                        prompt, max_length=500, num_return_sequences=1, use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_outputs, cpu_time, cpu_tokens), cpu_output = generate_code(
                            prompt, max_length=500, num_return_sequences=1, use_ttnn=False, iterations=iterations
                        )
                    for chunk in stream_response(ttnn_outputs[0]):
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                    st.write("**Generated Code (TTNN):**")
                    for i, code in enumerate(ttnn_outputs):
                        st.write(f"Sequence {i+1}:")
                        st.code(code, language="python")
                    terminal_output_value = f"TTNN ({ttnn_tokens} tokens):\n{ttnn_output}"
                    if test_cpu:
                        terminal_output_value += f"\n\nCPU ({cpu_tokens} tokens):\n{cpu_output}"
                    terminal_output = st.text_area(
                        "Terminal",
                        value=terminal_output_value,
                        height=100,
                        disabled=True,
                    )
                    ttnn_tokens_per_sec = ttnn_tokens / ttnn_time if ttnn_time > 0 else float("inf")
                    if test_cpu:
                        cpu_tokens_per_sec = cpu_tokens / cpu_time if cpu_time > 0 else float("inf")
                        speedup = (
                            ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
                        )
                        response_with_metrics = (
                            f"{ttnn_outputs[0]}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}\n"
                            f"CPU Time: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}\n"
                            f"Speedup: {speedup:.3f}x (Tokens/Sec, after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = (
                            f"{ttnn_outputs[0]}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}"
                        )
                elif task == "Image Classification with ResNet18":
                    (ttnn_label, ttnn_confidence, ttnn_time), ttnn_output = classify_image(
                        selected_image, use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_label, cpu_confidence, cpu_time), cpu_output = classify_image(
                            selected_image, use_ttnn=False, iterations=iterations
                        )
                    full_response = f"Predicted Label: {ttnn_label} (Confidence: {ttnn_confidence:.2f}%)"
                    message_placeholder.markdown(full_response)
                    terminal_output_value = f"TTNN:\n{ttnn_output}"
                    if test_cpu:
                        terminal_output_value += f"\n\nCPU:\n{cpu_output}"
                    terminal_output = st.text_area(
                        "Terminal",
                        value=terminal_output_value,
                        height=100,
                        disabled=True,
                    )
                    if test_cpu:
                        speedup = cpu_time / ttnn_time if ttnn_time > 0 else float("inf")
                        response_with_metrics = (
                            f"{full_response}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, CPU Time: {cpu_time:.4f}s, Speedup: {speedup:.3f}x (after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = f"{full_response}\n\n" f"TTNN Time: {ttnn_time:.4f}s"
                else:  # MNIST Classification
                    (ttnn_logits, ttnn_label, ttnn_confidence, ttnn_time), ttnn_output = classify_mnist(
                        use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_logits, cpu_label, cpu_confidence, cpu_time), cpu_output = classify_mnist(
                            use_ttnn=False, iterations=iterations
                        )
                    full_response = f"Predicted Digit: {ttnn_label} (Confidence: {ttnn_confidence:.2f}%)"
                    message_placeholder.markdown(full_response)
                    st.write("**Logits (TTNN):**")
                    st.write(ttnn_logits.numpy())
                    terminal_output_value = f"TTNN:\n{ttnn_output}"
                    if test_cpu:
                        terminal_output_value += f"\n\nCPU:\n{cpu_output}"
                    terminal_output = st.text_area(
                        "Terminal",
                        value=terminal_output_value,
                        height=100,
                        disabled=True,
                    )
                    if test_cpu:
                        speedup = cpu_time / ttnn_time if ttnn_time > 0 else float("inf")
                        response_with_metrics = (
                            f"{full_response}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, CPU Time: {cpu_time:.4f}s, Speedup: {speedup:.3f}x (after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = f"{full_response}\n\n" f"TTNN Time: {ttnn_time:.4f}s"

                st.write(f"**Performance Comparison (Latency):**")
                if task == "Question Answering with BERT":
                    st.write(f"- TTNN: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}")
                    if test_cpu:
                        st.write(f"- CPU: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}")
                elif task in ["Text Generation with GPT-2", "Code Generation with CodeGen"]:
                    st.write(f"- TTNN: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}")
                    if test_cpu:
                        st.write(f"- CPU: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}")
                else:
                    st.write(f"- TTNN: {ttnn_time:.4f}s")
                    if test_cpu:
                        st.write(f"- CPU: {cpu_time:.4f}s")
                if test_cpu:
                    st.write(
                        f"- Speedup: {speedup:.3f}x ({'Tokens/Sec' if task in ['Question Answering with BERT', 'Text Generation with GPT-2', 'Code Generation with CodeGen'] else 'Time'} after {iterations} iterations)"
                    )

            st.session_state.messages.append({"role": "assistant", "content": response_with_metrics})


if __name__ == "__main__":
    main()
