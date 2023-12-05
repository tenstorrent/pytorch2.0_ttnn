import torch

def add(x, y):
    print("'ttnn.add' is called")
    return x + y

def matmul(x, y):
    print("'ttnn.matmul' is called")
    return torch.matmul(x, y.t())
