from .backend import backend
from .backend import TenstorrentBackendOption

try:
    import ttnn
except ImportError:
    print("ttnn is not installed, use mock_ttnn instead")
    from . import mock_ttnn as ttnn
