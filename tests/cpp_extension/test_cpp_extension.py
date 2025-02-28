import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import ttnn
import torch_ttnn
from torch_ttnn.cpp_extension.custom_device_mode import ttnn_module, enable_ttnn_device
import pytest

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

import logging
import sys

@pytest.mark.parametrize(
    "input_shape",
    ((32, 1, 3, 3), (32,)),
)
def test_cpp_extension(device, input_shape):
    torch.utils.rename_privateuse1_backend('ttnn')

    # in pytest the device has already been initialized before this call
    # so instead we can wrap this around the custom device
    ttnn_device = ttnn_module.custom_device_from_ttnn(device)

    logging.info("Creating bfloat tensor from -1 to 1")
    torch_tensor = torch.empty(input_shape, dtype = torch.bfloat16).uniform_(-1, 1)
    print(torch_tensor)
    torch_tensor_abs = torch.abs(torch_tensor)
    print(torch_tensor_abs)

    logging.info("Transferring to ttnn")
    torch_ttnn_tensor = torch_tensor.to(ttnn_device)

    logging.info("get underlying ttnn tensor")
    ttnn_tensor = ttnn_module.get_ttnn_tensor(torch_ttnn_tensor)

    logging.info("Running abs on ttnn")
    ttnn_tensor = ttnn.abs(ttnn_tensor)

    logging.info("calling to_torch")
    ttnn_to_torch = ttnn.to_torch(ttnn_tensor)
    print(ttnn_to_torch)
    
    
    assert torch.allclose(torch_tensor_abs, ttnn_to_torch, rtol=0.1, atol=0.1)

    # logging.info("Closing device")
    # ttnn_module.close_custom_device(ttnn_device)

def test_bert_with_cpp_extension(device):
    model_name = "phiyodr/bert-large-finetuned-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left", torch_dtype=torch.bfloat16)
    m = AutoModelForQuestionAnswering.from_pretrained(model_name, torch_dtype=torch.bfloat16)
    context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
    question = "What discipline did Winkelmann create?"
    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=256,
        padding="max_length",
        truncation=True,
    )

    option = torch_ttnn.TorchTtnnOption(
                    device=device,
                    gen_graphviz=False,
                    run_mem_analysis=False,
                    metrics_path=model_name,
                    verbose=True,
                )

    # custom device
    torch.utils.rename_privateuse1_backend('ttnn')
    ttnn_device = ttnn_module.custom_device_from_ttnn(device)
    
    # clone input_ids on cpu since this the data transfer is somehow inplace?
    input_ids = inputs.input_ids.clone()
    
    inputs = inputs.to(ttnn_device)
    # modules are inplace, tensors are not
    m.to(ttnn_device)

    model = torch.compile(m, backend=torch_ttnn.backend, options=option)
    outputs = model(**inputs)
    
    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        response_start = torch.argmax(outputs.start_logits)
        response_end = torch.argmax(outputs.end_logits) + 1
        response_tokens = input_ids[0, response_start:response_end]
        return tokenizer.decode(response_tokens)

    print("finished:")
    print(outputs)
    answer = decode_output(outputs)

    print(
        f"""
    model_name: {model_name}
    input:
        context: {context}
        question: {question}
    answer: {answer}
    """
    )

# adapted from https://github.com/pytorch/examples/blob/main/mnist/main.py
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
        x = F.log_softmax(x, dim=1)
        return x
    
def test_mnist_with_cpp_extension(device):   
    model_name = "Mnist"
    transform = transforms.Compose([transforms.ToTensor()])
    test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)
    dataloader = DataLoader(test_dataset, batch_size=1)
    test_input, _ = next(iter(dataloader))
    test_input = test_input.to(torch.bfloat16)

    # Copy weights and biases to ttnn
    torch.utils.rename_privateuse1_backend('ttnn')
    ttnn_device = ttnn_module.custom_device_from_ttnn(device)
    

    
    option = torch_ttnn.TorchTtnnOption(
                    device=device,
                    gen_graphviz=False,
                    run_mem_analysis=False,
                    metrics_path=model_name,
                    verbose=True,
                )

    model = MnistModel()
    model = model.to(torch.bfloat16)
    test_input = test_input.to(ttnn_device)
    model.to(ttnn_device)
            
    model = torch.compile(model, backend=torch_ttnn.backend, options=option)
    results = model(test_input)