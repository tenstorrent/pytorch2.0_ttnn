import torch

def func_logger(func):
    def wrapper(*args, **kwargs):
        print(f"'ttnn.{func.__name__}' is called")
        return func(*args, **kwargs)
    return wrapper

############################################################
# Device related functions
############################################################
class Device:
    def __init__(self, device_id):
        self.device_id : int = device_id
    def __repr__(self):
        """
        This function is necessary for torch.fx.graph._register_custom_builtin.
        The generated code will use this function to generate the code.
        The compiler must use `torch.fx.graph._register_custom_builtin`
        to register the custom builtin.
        """
        return f"Device({self.device_id})"

def open(device_id):
    print(f"Device {device_id} is opened")
    return Device(device_id)

def close(device):
    print(f"Device {device.device_id} is closed")
    pass

@func_logger
def from_torch(tensor):
    return tensor

@func_logger
def to_torch(tensor):
    return tensor

@func_logger
def from_device(tensor, device):
    return tensor

@func_logger
def to_device(tensor, device):
    return tensor

############################################################
# Operations
############################################################

@func_logger
def add(x, y):
    z = torch.ops.aten.add.Tensor(x, y)
    return x + y

@func_logger
def matmul(x, y):
    return torch.ops.aten.mul.Tensor(x, y)
