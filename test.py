import torch
import torch_ttnn


# Inner module for demonstration, verify nested modules work
class InnerModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x):
        return self.linear(x) * x


# Simple module for demonstration
class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.nn.Parameter(torch.rand(3, 4))
        self.inner = InnerModule()

    def forward(self, x):
        return self.inner(x + x + self.param).clamp(min=-3.0, max=3.0)


def main():
    # Create a sample module
    m = MyModule()
    input = torch.rand(4)
    # Run it
    print('Before conversion', type(m))
    result_before = m.forward(input)
    # Convert it
    m = torch.compile(m, backend=torch_ttnn.backend)
    # Run it again
    print('After conversion', type(m))
    result_after = m.forward(input)
    # Verify the results are the same
    print(result_before)
    print(result_after)
    allclose = torch.allclose(result_before, result_after)
    assert allclose
    if allclose:
        print('All close!')
    
if __name__ == '__main__':
    main()
