import ttnn
import torch

# from ttnn_cpp_extension import ttnn_device_extension as ttnn_module
from ttnn_device_mode import ttnn_module, enable_ttnn_device


if __name__ == "__main__":
    # Enable the ttnn device mode
    # enable_ttnn_device()

    ttnn_device = ttnn.open_device(
        device_id=0,
        l1_small_size=16384,
        dispatch_core_config=ttnn.device.DispatchCoreConfig(ttnn.device.DispatchCoreType.ETH),
    )
    device = ttnn_module.as_torch_device(ttnn_device)

    dtype = torch.bfloat16
    a = torch.rand((3, 3), dtype=dtype)
    b = torch.ones_like(a, dtype=dtype)
    print(f"a: \n{a}")
    print(f"b: \n{b}")
    a = a.to(device)
    b = b.to(device)
    # a = a.to("ttnn")
    # b = b.to("ttnn")
    c = torch.add(a, b, alpha=1)  # dispatched to our kernel
    c = c.to("cpu")
    print(f"c: \n{c}")
