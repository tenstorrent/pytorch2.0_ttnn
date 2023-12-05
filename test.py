import torch
import torch_ttnn

# Simple module for demonstration
class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.nn.Parameter(torch.rand(3, 4))
        self.linear = torch.nn.Linear(4, 5)

    def forward(self, x):
        return self.linear(x + self.param).clamp(min=0.0, max=1.0)

def main():
    # Create a sample module
    m = MyModule()
    input = torch.rand(4)
    print('Before conversion', type(m))
    print(m.forward(input))

    m = torch_ttnn.transform_ttnn(m)
    print('After conversion', type(m))
    print(m.forward(input))
    
if __name__ == '__main__':
    main()