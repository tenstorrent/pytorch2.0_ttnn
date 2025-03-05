import torch
import ttnn
from torch_ttnn.cpp_extension.custom_device_mode import ttnn_module
import pytest

import logging


@pytest.mark.parametrize(
    "input_shape",
    ((32, 1, 3, 3), (1, 32)),
)
@pytest.mark.parametrize(
    "dtype",
    (torch.bfloat16, torch.int32),
)
def test_cpp_extension(device, input_shape, dtype):
    torch.utils.rename_privateuse1_backend("ttnn")

    # in pytest the device has already been initialized before this call
    # so instead we can wrap this around the custom device
    ttnn_device = ttnn_module.custom_device_from_ttnn(device)

    logging.info("Creating bfloat tensor from -1 to 1")
    if dtype == torch.bfloat16:
        torch_tensor = torch.empty(input_shape, dtype=dtype).uniform_(-1, 1)
    elif dtype == torch.int32:
        torch_tensor = torch.randint(-1000, 1000, input_shape)
        torch_tensor = torch_tensor.to(torch.int32)
    else:
        raise Exception(f"{dtype} not being tested at this time")
    print(torch_tensor)

    logging.info("Transferring to ttnn")
    torch_ttnn_tensor = torch_tensor.to(ttnn_device)

    logging.info("Get underlying ttnn tensor")
    ttnn_tensor = ttnn_module.get_ttnn_tensor(torch_ttnn_tensor)

    # Compare output of abs op for bfloat16 dtype since ttnn.abs does not support int
    if dtype == torch.bfloat16:
        torch_out = torch.abs(torch_tensor)
        print(torch_out)

        logging.info("Running abs on ttnn")
        ttnn_tensor = ttnn.abs(ttnn_tensor)
    elif dtype == torch.int32:
        torch_out = torch_tensor
    else:
        raise Exception(f"{dtype} not being tested at this time")

    logging.info("calling to_torch")
    ttnn_to_torch = ttnn.to_torch(ttnn_tensor)

    print(ttnn_to_torch)

    assert torch.allclose(torch_out, ttnn_to_torch, rtol=0.1, atol=0.1)
