import torch


############################################################
# Device related functions
############################################################
class Device:
    def __init__(self, device_id):
        self.device_id: int = device_id

    #  def __repr__(self):
    #      """
    #      This function is necessary for torch.fx.graph._register_custom_builtin.
    #      The generated code will use this function to generate the code.
    #      The compiler must use `torch.fx.graph._register_custom_builtin`
    #      to register the custom builtin.
    #
    #      However, the ttnn module's Device does not provide a __repr__ function.
    #      So the mock here can not provide a __repr__ function either.
    #      We have to find other way. See `torch_ttnn.py` for details.
    #      """
    #      return f"Device({self.device_id})"


def open(device_id):
    print(f"Device {device_id} is opened")
    return Device(device_id)


def close(device):
    print(f"Device {device.device_id} is closed")
    pass


def from_torch(tensor):
    return tensor


def to_torch(tensor):
    return tensor


def from_device(tensor):
    return tensor


def to_device(tensor, device):
    print(f"Tensor {tensor} is moved to device {device.device_id}")
    return tensor


############################################################
# Operations
############################################################


def add(x, y):
    z = x + y
    return z


def matmul(x, y):
    mm = torch.ops.aten.mm(x, y)
    return mm
