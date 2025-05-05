# Streamlit Compiler Performance Benchmark Guide

This guide describes the functionality and usage of a [Streamlit](https://docs.streamlit.io) application ([demo.py](https://github.com/tenstorrent/pytorch2.0_ttnn/)) designed to benchmark the performance of various machine learning models using the [TTNN compiler](https://github.com/tenstorrent/pytorch2.0_ttnn). The app supports five tasks: **Question Answering with BERT**, **Text Generation with GPT-2**, **Image Classification with ResNet18**, **MNIST Classification**, and **Code Generation with CodeGen**. It measures metrics like execution time, tokens per second (for text-based models), and speedup (TTNN vs. CPU).

## Table of Contents
- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [How to Launch the App](#how-to-launch-the-app)
- [How to use the app](#how-to-use-the-app)
- [Model Information](#model-information)
- [Troubleshooting](#troubleshooting)

## Overview
The [Streamlit](https://docs.streamlit.io) app ([demo.py](https://github.com/tenstorrent/pytorch2.0_ttnn/)) provides a user-friendly interface to benchmark the performance of five machine learning models:

- **BERT**: For question answering based on a given context ([SQuAD 2.0 dataset](https://rajpurkar.github.io/SQuAD-explorer/)).
- **GPT-2**: For autoregressive text generation, developed by [OpenAI](https://huggingface.co/openai-community/gpt2).
- **ResNet18**: For image classification on [CIFAR-10 images](https://www.cs.toronto.edu/~kriz/cifar.html).
- **MNIST Classification**: For digit classification using a custom CNN ([MNIST dataset](http://yann.lecun.com/exdb/mnist/)).
- **CodeGen**: For Python code generation, developed by [Salesforce](https://github.com/salesforce/CodeGen).

For each model, the app:
- Runs the model on [TTNN](https://tenstorrent.com/technology/) for a specified number of iterations, and optionally on CPU.
- Measures **execution time** and, for text-based models, **tokens per second**.
- Computes **speedup** (TTNN vs. CPU) to compare performance.
- Displays results in real-time, including model outputs, terminal logs, and performance metrics.

The app is designed for evaluating TTNN’s performance on various ML tasks. It includes interactive inputs (e.g., text prompts, image selection) and supports customizable configurations for benchmarking.

## Setup Instructions
**Install Dependencies**:
Install the required dependencies:
  ```bash
  pip install -r requirements-demo.txt
  ```
## How To Launch The App
**Run Using Streamlit**:
Run using streamlit to launch the API as a local web server:
  ```bash
  streamlit run demo.py
  ```
The process will run in the terminal, and it will display a URL to a local web server where you can access the API, press ```cmd + left click``` on the ```Local URL``` and it will open the app in your local web browser. 

<p align="center">
  <img src="img/streamlit.png" alt="config" width="500"/>
</p>

## How To Use The App
**Select Model To Test**:
There are five models available to run, choose the model and task from the drop down menu near the top of the page.

**Configure The Test**:
The test can be configured with a prompt or image to test, default values are already set for convenience. The test can also be configured with an option to measure CPU performance for comparison.  The test returns a latency value, and a tokens/sec measurement for language models. The latency is the time it takes to run a forward pass for BERT, MNIST, or ResNet. For GPT2 and CodeGen, the latency is the time it takes to run a full sequence generation.  This is with a configurable input and sequence generation length. These generative language models, along with BERT, also return a tokens/sec measurement. 

<p align="center">
  <img src="img/config.png" alt="config" width="500"/>
</p>

**Run The Test**:
The test will display a graph of execution time vs warmup iteration, it will return an execution time, terminal output, relative CPU speedup, and for text models, tokens/sec. 

<p align="center">
  <img src="img/output.png" alt="config" width="500"/>
</p>

## Model Information
**Question Answering With BERT**:
The version of BERT used in this demo is the "BERT-Large" variant, fine tuned on the [SQuAD 2.0 dataset](https://rajpurkar.github.io/SQuAD-explorer/).  This model is designed to answer questions by processing a question text and a context text together as one input. This context is a text which is expected to contain the exact answer to the question. The model finds a subset of this text and returns it as an answer to the question. It works by assigning a probability to each token in the context string of being the start and end of the returned answer. The amount of tensors getting processed by the model scale with the length of the question and context.  

In the actual test in this script, the sequences are padded (or truncated) to a prespecified length, configurable by adjusting the "sequence length" value below the question box.  The padding represents unlearned tokens from the model which are processed by its components, but are masked to not influence the output. This padding/truncation ensures a consistent tokens/sec measurement which doesn't depend on the specific question and context being processed by the model, since padding tokens are included in the computations of the model in the same way as regular tokens.  This means, in this script, tokens/sec is measured as ```sequence_length / execution_time```, ensuring consistent outputs. 



**GPT-2**
This is a generative language model from Open AI, specifically the GPT2-small variant with 125 million parameters.  It is a decoder only transformer which generates outputs autoregressively.  The input is padded (or truncated) to a configurable number of tokens just like BERT, by setting ```Input Sequence Length``` below the prompt. The generation length is also configurable with the ```New Tokens To Generate``` input.  This padding and truncation ensures consistent latency measurements for different inputs. 

<p align="center">
  <img src="img/gpt2.png" alt="config" width="500"/>
</p>


**MNIST**
This is a small image classification model which includes convolution and pooling operations. It is made to process 32x32x3 images of handwritten digits.  Only execution time is measured.

**CodeGen**
This, like GPT-2, is a transformer generative language model which is 350 million parameters trained on python code.  It is intended to complete code, and has the same input padding and generation length configuration as GPT-2.  

<p align="center">
  <img src="img/codegen.png" alt="config" width="500"/>
</p>


**ResNet18**
This is an image classification model incorporating convolutions and normalization ops heavily.  It can process 32x32x3 color images. Only execution time is measured.

## Troubleshooting
**Compilation Errors**
ResNet18 has been known to throw compilation errors, specifically after ```ConstantFoldingPass```.  This is due to issues in model specific integration for TTNN. 

Other compilation errors are unexpected, make sure you are using the latest version of TTNN and inspect the terminal output if you run into a compilation error.

**Hanging**
Tests are expected to take approximately 2-4 minutes or less for text models, less than one minute for MNIST and ResNet18. Long waits are possible if using especially long sequence lengths for text models.  In that case, it is likely to succeed if given enough time. 

Hanging has not been encountered in testing this app, and it's likely that it would be due to issues in the TTNN version being used if encountered. The progress bar not appearing points to an issue the TTNN compilation (i.e opening devices and calling torch.compile()). The progress bar appearing but never moving would mean the hanging happened after compilation.  A full progress bar and displayed execution time graph along with hanging would mean the model hung during generation/inference.  Be sure to inspect the terminal output for clues to source of the hanging. 

