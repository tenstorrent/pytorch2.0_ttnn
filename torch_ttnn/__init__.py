# The inferface of this backend

from .backend import ttnn_backend
from .backend import TenstorrentBackendOption
import torch as _torch

_torch._dynamo.backends.registry.register_backend(name="ttnn", compiler_fn=ttnn_backend)

# To wrap the ttnn ops
from .passes import target_wrappers

try:
    import ttnn
except ImportError as e:
    print(
        "ttnn is not installed. Run `python3 -m pip install -r requirements.txt` or `python3 -m pip install -r requirements-dev.txt` if you are developing the compiler"
    )
    raise e
