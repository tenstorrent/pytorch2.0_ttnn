import torch
import torch_ttnn
from torch_ttnn import ttnn


# Inner module for demonstration, verify nested modules work
class InnerModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4, dtype=torch.bfloat16)

    def forward(self, x):
        return self.linear(x) * x


# Simple module for demonstration
class ComplicatedModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.nn.Parameter(torch.rand((3, 4), dtype=torch.bfloat16))
        self.inner = InnerModule()

    def forward(self, x):
        return self.inner(x + x + self.param).clamp(min=-3.0, max=3.0)


class AddModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x


class MatmulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.matmul(x, x)


def main():
    # Open device 0 and set it as torch_ttnn global variable
    device: ttnn.Device = ttnn.open(0)
    torch_ttnn.set_device(device)
    # Create a sample module
    m = MatmulModule()
    input = torch.rand((4, 4), dtype=torch.bfloat16)
    # Run it
    print("Before conversion", type(m))
    result_before = m.forward(input)
    # Convert it
    m = torch.compile(m, backend=torch_ttnn.backend)
    # TODO(yoco) Check the graph has be rewritten and contain ttnn ops
    # Run it again
    print("After conversion", type(m))
    result_after = m.forward(input)
    # Verify the results are the same
    print(result_before)
    print(result_after)
    allclose = torch.allclose(result_before, result_after)
    assert allclose
    if allclose:
        print("All close!")
    # Close the device
    ttnn.close(device)


if __name__ == "__main__":
    main()
