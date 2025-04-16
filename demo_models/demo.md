Streamlit Compiler Performance Benchmark Guide
This guide describes the functionality and usage of a Streamlit application (demo.py) designed to benchmark the performance of various machine learning models using the TTNN compiler. The app supports five tasks: Question Answering with BERT, Text Generation with GPT-2, Image Classification with ResNet18, MNIST Classification, and Code Generation with CodeGen. The app measures metrics like execution time, tokens per second (for text-based models), and speedup (TTNN vs. CPU).

Table of Contents

Overview
Setup Instructions
How to Use the App
Model-Specific Benchmarks
Question Answering with BERT
Text Generation with GPT-2
Image Classification with ResNet18
MNIST Classification
Code Generation with CodeGen


Output and Metrics
Troubleshooting

Overview
The Streamlit app (demo.py) provides a user-friendly interface to benchmark the performance of five machine learning models:

BERT: For question answering based on a given context (SQuAD 2.0 dataset).
GPT-2: For autoregressive text generation.
ResNet18: For image classification (CIFAR-10 images).
MNIST Classification: For digit classification using a custom CNN.
CodeGen: For Python code generation.

For each model, the app:

Runs the model on TTNN (a specialized compiler) for a specified number of warm-up iterations, and optionally on CPU.
Measures execution time and, for text-based models, tokens per second.
Computes speedup (TTNN vs. CPU) to compare performance.
Displays results in real-time, including model outputs, terminal logs, and performance metrics.

The app is designed for researchers, developers, and engineers who want to evaluate TTNN’s performance on various ML tasks. It includes interactive inputs (e.g., text prompts, image selection) and supports customizable iterations for benchmarking.

Setup Instructions
To run the Streamlit app, follow these steps:

Install Dependencies:Ensure you have Python 3.8+ installed. Install the required packages:
pip install streamlit torch ttnn pillow datasets

Note: The ttnn library and demo_models module (imported in demo.py) may require specific installations or access to proprietary libraries. Contact the repository owner or documentation for ttnn setup.

Download the Code:Save the demo.py file in a working directory.

Run the App:Launch the Streamlit app:
streamlit run demo.py

This opens the app in your default browser (typically at http://localhost:8501).

Prepare Data:

For ResNet18, the app automatically downloads CIFAR-10 images during the first run.
No additional data is required for other models, as prompts and inputs are provided via the UI.


Hardware Requirements:

A compatible TTNN device for TTNN benchmarks.
A CPU for CPU benchmarks (optional).
Sufficient memory for model inference (e.g., 8GB+ RAM).



How to Use the App

Select a Task:

Use the dropdown menu to choose a task (e.g., “Question Answering with BERT”).
Read the “About” section for task-specific details and notes.


Configure Inputs:

BERT: Enter a context (text) and a question.
GPT-2/CodeGen: Enter a text prompt.
ResNet18: Select a CIFAR-10 image from the dropdown.
MNIST: No input required (uses a sample digit).
Default prompts/images are provided for convenience.


Set Parameters:

Iterations: Choose the number of iterations (default: 5) for benchmarking. More iterations provide more reliable averages.
Test CPU: Check the box to compare TTNN with CPU performance (enabled by default).


Run the Benchmark:

Click the “Run” button to start the benchmark.
The app displays a progress bar, model outputs, terminal logs, and performance metrics.


View Results:

Chat History: Shows user inputs and model responses.
Process Output: Displays terminal logs (e.g., TTNN and CPU outputs).
Performance Comparison: Lists execution times, tokens per second (for text models), and speedup.




Model-Specific Benchmarks
Each model has unique inputs, outputs, and performance considerations. Below are detailed instructions for each.
Question Answering with BERT

Description: Uses a fine-tuned BERT model (SQuAD 2.0) to answer questions based on a provided context.
Inputs:
Context: A text paragraph (e.g., “A corvette has a naturally aspirated V8 engine.”).
Question: A question about the context (e.g., “What kind of engine does a corvette have?”).
Default values are provided.


How to Use:
Select “Question Answering with BERT” from the dropdown.
Edit the context and question in the text areas.
Set iterations and CPU testing preference.
Click “Run” to get the answer and performance metrics.


Outputs:
Answer text (e.g., “A naturally aspirated V8 engine”).
Terminal logs for TTNN and CPU (if tested).
Metrics: TTNN time, CPU time, tokens per second, speedup.


Notes:
Longer context-question pairs may affect tokens per second. Use consistent prompts for fair comparisons.
Requires context to run (error if context is empty).




Text Generation with GPT-2

Description: Uses GPT-2 for autoregressive text generation, producing multiple sequences from a prompt.
Inputs:
Prompt: A starting text (e.g., “Can machines think?”).
Maximum generation length is 512 tokens.


How to Use:
Select “Text Generation with GPT-2”.
Edit the prompt.
Set iterations and CPU testing.
Click “Run” to generate text.


Outputs:
Two generated text sequences (TTNN).
Terminal logs.
Metrics: TTNN time, CPU time, tokens per second, speedup.


Notes:
Prompt length affects performance. Use the same prompt for comparisons.
Outputs are displayed as plain text below the chat response.




Image Classification with ResNet18

Description: Uses ResNet18 to classify CIFAR-10 images (e.g., airplane, cat).
Inputs:
Image: Select a CIFAR-10 image from a dropdown (e.g., “dog”).
Images are preloaded from the CIFAR-10 dataset.


How to Use:
Select “Image Classification with ResNet18”.
Choose an image from the dropdown.
Set iterations and CPU testing.
Click “Run” to classify the image.


Outputs:
Predicted label and confidence (e.g., “dog, Confidence: 85.23%”).
Terminal logs.
Metrics: TTNN time, CPU time, speedup.


Notes:
The model is untrained, so predictions are not accurate.
Performance is measured in execution time, not tokens per second.




MNIST Classification

Description: Uses a custom CNN to classify a sample MNIST digit.
Inputs:
None (uses a predefined sample digit).


How to Use:
Select “MNIST Classification”.
Set iterations and CPU testing.
Click “Run” to classify the digit.


Outputs:
Predicted digit and confidence (e.g., “Predicted Digit: 7, Confidence: 92.10%”).
Logits (TTNN) as a NumPy array.
Terminal logs.
Metrics: TTNN time, CPU time, speedup.


Notes:
The model is untrained, so predictions are not accurate.
No user input is required, making it the simplest task.




Code Generation with CodeGen

Description: Uses CodeGen to generate Python code from a prompt.
Inputs:
Prompt: A code snippet or description (e.g., “def compile_ttnn():”).
Maximum generation length is 512 tokens.


How to Use:
Select “Code Generation with CodeGen”.
Edit the prompt.
Set iterations and CPU testing.
Click “Run” to generate code.


Outputs:
Generated Python code (displayed in a code block).
Terminal logs.
Metrics: TTNN time, CPU time, tokens per second, speedup.


Notes:
Prompt length affects performance. Use consistent prompts for comparisons.
Generated code is shown with syntax highlighting.




Output and Metrics
For each task, the app provides:

Chat History: User inputs and model responses, including metrics.
Process Output: Terminal logs from TTNN and CPU runs (e.g., compiler outputs).
Performance Comparison:
Text-Based Models (BERT, GPT-2, CodeGen):
TTNN: Execution time (seconds), tokens per second.
CPU (if tested): Execution time, tokens per second.
Speedup: Ratio of TTNN to CPU tokens per second.


Image-Based Models (ResNet18, MNIST):
TTNN: Execution time.
CPU (if tested): Execution time.
Speedup: Ratio of CPU time to TTNN time.




Example:TTNN Time: 2.3456s, Tokens/Sec: 123.456
CPU Time: 5.6789s, Tokens/Sec: 50.123
Speedup: 2.463x (Tokens/Sec after 5 iterations)




Troubleshooting

No Output in UI:
Check the terminal for errors (e.g., missing ttnn or demo_models).
Ensure Streamlit is updated (pip install --upgrade streamlit).


Slow Performance:
Reduce iterations for faster testing.


CIFAR-10 Download Fails:
Ensure internet access and sufficient disk space (./data directory).


Model Outputs Incorrect:
ResNet18 and MNIST models are untrained, so predictions are not expected to be accurate.  Codegen and GPT-2 are expected to give coherent responses, jibberish outputs may point to accuracy issues. 

Contact Support:
For TTNN-specific issues, consult the ttnn documentation or repository.



