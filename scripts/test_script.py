import sys
import torch

# Import the high-level package to ensure Python path/linking is OK
import torch_ttnn

# Import the cpp extension wrapper (this loads the C++ .so)
from torch_ttnn.cpp_extension import ttnn_module

print("Python:", sys.executable)
print("Torch version:", torch.__version__)
print("ttnn_module .so path:", getattr(ttnn_module, "__file__", "<no file>"))

# Check for key symbols without opening any device
for name in ["open_torch_device"]:
    print(f"hasattr(ttnn_module, {name!r}):", hasattr(ttnn_module, name))

print("Import OK. No device opened.")
