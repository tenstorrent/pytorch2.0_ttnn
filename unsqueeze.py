import torch
import torch_ttnn
import ttnn

import torch._dynamo

torch._dynamo.config.suppress_errors = True


class UnsqueezeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.unsqueeze(x, y)

    # RuntimeError: TT_THROW @ ../ttnn/cpp/ttnn/operations/core.hpp:81: tt::exception
    # info:
    # Unable to reshape a tensor in TILE_LAYOUT to non-tile height and width!
    # Please convert the tensor to ROW_MAJOR_LAYOUT first.
    def input_shapes(self):
        return [(3, 2), 1]


def torch_compile(inputs):
    out = mod.forward(*inputs)
    print(f"in tensor shape: {inputs[0].shape}")
    print(f"out tensor shape: {out.shape}")
    return out


def ttnn_compile(inputs):
    device = ttnn.open_device(device_id=0)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True

    ttnn_mod = torch.compile(mod, backend=torch_ttnn.backend, options=option)
    out = ttnn_mod.forward(*inputs)
    print(f"in tensor shape: {inputs[0].shape}")
    print(f"out tensor shape: {out.shape}")

    ttnn.close_device(device)
    return out


if __name__ == "__main__":
    mod = UnsqueezeModule()
    input_shapes = mod.input_shapes()
    tensor = torch.rand(input_shapes[0], dtype=torch.bfloat16)
    dim = input_shapes[1]
    inputs = [tensor, dim]

    result_before = torch_compile(inputs)
    result_after = ttnn_compile(inputs)
    print(f"result_before: {result_before}")
    print(f"result_after: {result_after}")
    assert torch.allclose(result_before, result_after), "Output NOT matching!"
