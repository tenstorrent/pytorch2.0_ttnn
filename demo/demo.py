import ttnn
import streamlit as st
from PIL import Image
import io
import sys
from bert import *
from codegen import *
from gpt2 import *
from resnet18 import *
from mnist import *
from whisper import *

MAX_GENERATION_LENGTH = 512


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
            "Audio Transcription with Whisper",
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
    elif task == "Code Generation with CodeGen":
        st.info(
            """
            **CodeGen**: Salesforce model for Python code generation.
            **How to Use**: Edit prompt, set iterations, then click "Run".
            **Note** Different length prompts will give different performance (token/sec), all else being equal. Be sure to use the same prompt when comparing performance.
        """
        )
    else:  # Audio Transcription with Whisper
        st.info(
            """
            **Whisper (distil-large-v3)**: Distilled version of OpenAI's Whisper model for audio transcription.
            **How to Use**: Use sample audio or upload your own, set iterations, then click "Transcribe".
            **Target Performance**: 54.7 tokens/sec/user (n150 hardware) with 244ms TTFT for batch size 1.
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
        sequence_length_input = st.number_input(
            "Sequence Length",
            min_value=8,
            max_value=16384,
            value=256,
            help="The input will be padded or truncated to this length, controlling how many tokens are being processed by the model",
            label_visibility="visible",
        )
        prompt = st.text_input("Question:", value=st.session_state.default_prompt[task], key="bert_prompt")
    elif task == "Text Generation with GPT-2":
        prompt = st.text_input("Prompt:", value=st.session_state.default_prompt[task], key="gpt2_prompt")
        sequence_length_input = st.number_input(
            "Input Sequence Length",
            min_value=8,
            max_value=16384,
            value=256,
            help="The input will be padded or truncated to this length, controlling how many tokens are being processed by the model",
            label_visibility="visible",
        )
        new_tokens = st.number_input(
            "New Tokens To Generate",
            min_value=8,
            max_value=16384,
            value=256,
            help="The input will be padded or truncated to this length, controlling how many tokens are being processed by the model",
            label_visibility="visible",
        )
    elif task == "Code Generation with CodeGen":
        prompt = st.text_input("Prompt:", value=st.session_state.default_prompt[task], key="codegen_prompt")
        sequence_length_input = st.number_input(
            "Input Sequence Length",
            min_value=8,
            max_value=16384,
            value=256,
            help="The input will be padded or truncated to this length, controlling how many tokens are being processed by the model",
            label_visibility="visible",
        )
        new_tokens = st.number_input(
            "New Tokens To Generate",
            min_value=8,
            max_value=16384,
            value=256,
            help="The input will be padded or truncated to this length, controlling how many tokens are being processed by the model",
            label_visibility="visible",
        )
    elif task == "Image Classification with ResNet18":
        st.subheader("Select an Image")
        image_choice = st.selectbox("Choose a CIFAR-10 image:", list(st.session_state.cifar10_samples.keys()))
        selected_image = st.session_state.cifar10_samples[image_choice]
        st.image(selected_image, caption=image_choice, width=100)
        prompt = "Classify Image"
    elif task == "Audio Transcription with Whisper":
        st.subheader("Audio Input")
        st.info("Using sample audio from LibriSpeech dataset")
        prompt = "Transcribe Audio"
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
                        st.session_state.context,
                        prompt,
                        use_ttnn=True,
                        iterations=iterations,
                        sequence_length=sequence_length_input,
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
                        speedup = ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
                        response_with_metrics = (
                            f"{full_response}\n\n"
                            f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}\n"
                            f"CPU Time: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}\n"
                            f"Speedup: {speedup:.3f}x (Tokens/Sec, after {iterations} iterations)"
                        )
                    else:
                        response_with_metrics = (
                            f"{full_response}\n\n" f"TTNN Time: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}"
                        )
                elif task == "Text Generation with GPT-2":
                    (ttnn_outputs, ttnn_time, ttnn_tokens), ttnn_output = generate_text(
                        prompt,
                        input_length=sequence_length_input,
                        max_new_tokens=new_tokens,
                        use_ttnn=True,
                        iterations=iterations,
                    )
                    if test_cpu:
                        (cpu_outputs, cpu_time, cpu_tokens), cpu_output = generate_text(
                            prompt,
                            input_length=sequence_length_input,
                            max_new_tokens=new_tokens,
                            use_ttnn=False,
                            iterations=iterations,
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
                        speedup = ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
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
                        prompt,
                        input_length=sequence_length_input,
                        max_new_tokens=new_tokens,
                        use_ttnn=True,
                        iterations=iterations,
                    )
                    if test_cpu:
                        (cpu_outputs, cpu_time, cpu_tokens), cpu_output = generate_code(
                            prompt,
                            input_length=sequence_length_input,
                            max_new_tokens=new_tokens,
                            use_ttnn=False,
                            iterations=iterations,
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
                        speedup = ttnn_tokens_per_sec / cpu_tokens_per_sec if cpu_tokens_per_sec > 0 else float("inf")
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
                elif task == "MNIST Classification":
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
                else:  # Audio Transcription with Whisper
                    (transcription, ttnn_time, ttnn_tokens, ttnn_tokens_per_sec), ttnn_output = transcribe_audio(
                        use_ttnn=True, iterations=iterations
                    )
                    if test_cpu:
                        (cpu_transcription, cpu_time, cpu_tokens, cpu_tokens_per_sec), cpu_output = transcribe_audio(
                            use_ttnn=False, iterations=iterations
                        )
                    for chunk in stream_response(transcription):
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
                elif task in ["Text Generation with GPT-2", "Code Generation with CodeGen", "Audio Transcription with Whisper"]:
                    st.write(f"- TTNN: {ttnn_time:.4f}s, Tokens/Sec: {ttnn_tokens_per_sec:.3f}")
                    if test_cpu:
                        st.write(f"- CPU: {cpu_time:.4f}s, Tokens/Sec: {cpu_tokens_per_sec:.3f}")
                else:
                    st.write(f"- TTNN: {ttnn_time:.4f}s")
                    if test_cpu:
                        st.write(f"- CPU: {cpu_time:.4f}s")
                if test_cpu:
                    st.write(
                        f"- Speedup: {speedup:.3f}x ({'Tokens/Sec' if task in ['Question Answering with BERT', 'Text Generation with GPT-2', 'Code Generation with CodeGen', 'Audio Transcription with Whisper'] else 'Time'} after {iterations} iterations)"
                    )

            st.session_state.messages.append({"role": "assistant", "content": response_with_metrics})


if __name__ == "__main__":
    main()
