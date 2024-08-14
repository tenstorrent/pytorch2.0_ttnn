import torch
import torch_ttnn
import ttnn
import tt_lib

class TransposeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, dim0, dim1):
        return torch.transpose(x, dim0, dim1)

    # Constraint: Last dim of input should be even.
    # If not, this runtime error will be thrown:
    # RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:41: page_size % sizeof(uint32_t) == 0
    def input_shapes(self):
        return [(5, 3, 2), 0, 2]

if __name__ == "__main__":
    # Open device 0
    device: ttnn.Device = ttnn.open_device(device_id=0)
    # For AutoFormat
    tt_lib.device.SetDefaultDevice(device)

    m = TransposeModule()
    input_shapes = m.input_shapes()
    input = torch.rand(input_shapes[0], dtype=torch.bfloat16)
    dim0 = input_shapes[1]
    dim1 = input_shapes[2]
    result_before = m.forward(input, dim0, dim1)
    option = torch_ttnn.TorchTtnnOption(device=device)
    option.gen_graphviz = True
    option.run_mem_analysis = True
    m = torch.compile(m, backend=torch_ttnn.backend, options=option)
    result_after = m.forward(input, dim0, dim1)

    # Check the graph has be rewritten and contain ttnn ops
    nodes = list(option._out_fx_graphs[0].nodes)

    # Close the device
    ttnn.close_device(device)