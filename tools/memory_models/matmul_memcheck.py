import torch
import torch_ttnn
import ttnn
import tt_lib

class MatmulModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return torch.matmul(x, y)

    def input_shapes(self):
        return [(5, 3), (3, 4)]

if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)
    # For AutoFormat
    tt_lib.device.SetDefaultDevice(device)

    m = MatmulModule()
    input_shapes = m.input_shapes()
    x = torch.rand(input_shapes[0], dtype=torch.bfloat16)
    y = torch.rand(input_shapes[1], dtype=torch.bfloat16)

    result_before = m.forward(x, y)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    option.run_mem_analysis = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(x, y)

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)

    # Close the device
    ttnn.close_device(device)