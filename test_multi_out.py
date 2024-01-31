import torch
import torch_ttnn
from torch_ttnn import ttnn


# Inner module for demonstration, verify nested modules work
class M(torch.nn.Module):
    def forward(self, x):
        a = torch.ops.aten.split_with_sizes(x, [1, 2, 1], dim=0)
        return a


def main():
    # Open device 0 and set it as torch_ttnn global variable
    device: ttnn.Device = ttnn.open(7)
    # Create a sample module
    m = M()
    input = torch.rand((4, 4), dtype=torch.bfloat16)
    # Run it
    print("Before conversion", type(m))
    result_before = m.forward(input)
    # Create a Torch2TNN option
    option = torch_ttnn.TorchTtnnOption(device=device)
    # Convert it
    m = torch.compile(m, backend=torch_ttnn.backend(option))
    # Run it again
    print("After conversion", type(m))
    result_after = m.forward(input)
    # Verify the results are the same
    option._out_fx_graphs[0].print_tabular()
    allclose = True
    for rb, ra in zip(result_before, result_after):
        print(rb, ra)
        if not torch.allclose(rb, ra):
            allclose = False
    if allclose:
        print("All result are close!")
    # Close the device
    ttnn.close(device)


if __name__ == "__main__":
    main()
