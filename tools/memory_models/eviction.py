import torch
import torch_ttnn
import ttnn
import tt_lib

class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        t2 = torch.nn.functional.relu(t1)
        t3 = torch.nn.functional.silu(t2)
        t4 = torch.nn.functional.gelu(t2)
        t5 = torch.nn.functional.tanh(t4)
        t6 = t2 + t3 + t5
        return t6
    
    def input_shape(self):
        return [100, 3, 224, 224]

if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)
    # For AutoFormat
    tt_lib.device.SetDefaultDevice(device)

    m = Module()
    m = m.to(torch.bfloat16)
    input = torch.rand(m.input_shape(), dtype=torch.bfloat16)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    option.run_mem_analysis = True
    option.run_eviction_opt = True
    # The compilation is lazy, so we need to run forward once to trigger the compilation
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result = m.forward(input)

    # Close the device
    ttnn.close_device(device)

    
    