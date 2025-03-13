import torch
import ttnn
from torch_ttnn.cpp_extension.ttnn_device_mode import ttnn_module
import pytest

import logging


@pytest.mark.parametrize(
    "input_shape",
    ((32, 1, 3, 3), (1, 32), (4,)),
)
@pytest.mark.parametrize(
    "dtype",
    (torch.bfloat16, torch.int, torch.long),
)
def test_cpp_extension(device, input_shape, dtype):
    # in pytest the device has already been initialized before this call
    # so instead we can wrap this around the custom device
    ttnn_device = ttnn_module.as_torch_device(device)

    logging.info("Creating bfloat tensor from -1 to 1")
    if dtype == torch.bfloat16:
        torch_tensor = torch.empty(input_shape, dtype=dtype).uniform_(-1, 1)
    elif dtype == torch.int or dtype == torch.long:
        torch_tensor = torch.randint(-1000, 1000, input_shape)
        torch_tensor = torch_tensor.to(dtype)
    else:
        raise Exception(f"{dtype} not being tested at this time")

    logging.info("Transferring to ttnn")
    torch_ttnn_tensor = torch_tensor.to(ttnn_device)

    logging.info("Get underlying ttnn tensor")
    ttnn_tensor = ttnn_module.get_ttnn_tensor(torch_ttnn_tensor)

    # Compare output of abs op for bfloat16 dtype since ttnn.abs does not support int
    if dtype == torch.bfloat16:
        torch_out = torch.abs(torch_tensor)
        logging.info("Running abs on ttnn")
        ttnn_tensor = ttnn.abs(ttnn_tensor)
    elif dtype == torch.int or dtype == torch.long:
        torch_out = torch_tensor
    else:
        raise Exception(f"{dtype} not being tested at this time")

    logging.info("calling to_torch")
    ttnn_to_torch = ttnn.to_torch(ttnn_tensor)
    # cast back to dtype because ttnn always return uint32_t for integers
    if dtype == torch.long:
        assert ttnn_to_torch.dtype == torch.int32
        ttnn_to_torch = ttnn_to_torch.to(dtype)

    assert torch.allclose(torch_out, ttnn_to_torch, rtol=0.1, atol=0.1)


def test_empty(device):
    # Sometimes nnModule.to(device) will directly allocate an empty tensor on device
    # and with not performa a copy.

    ttnn_device = ttnn_module.as_torch_device(device)

    logging.info("Creating bfloat tensor from -1 to 1")
    torch_tensor = torch.empty((32, 1, 3, 3), dtype=torch.bfloat16, device=ttnn_device)

    logging.info("Get underlying ttnn tensor")
    ttnn_tensor = ttnn_module.get_ttnn_tensor(torch_tensor)

    logging.info("calling to_torch")
    ttnn_to_torch = ttnn.to_torch(ttnn_tensor)

    # assert torch.allclose(torch_tensor, ttnn_to_torch, rtol=0.1, atol=0.1)
