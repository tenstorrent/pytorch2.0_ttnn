from torch_ttnn.backend import backend
from torch_ttnn.backend import TorchTtnnOption
from torch_ttnn.memory_backend import memory_backend

try:
    import ttnn
except ImportError as e:
    print(
        "ttnn is not installed. Run `python3 -m pip install -r requirements.txt` or `python3 -m pip install -r requirements-dev.txt` if you are developing the compiler"
    )
    raise e
