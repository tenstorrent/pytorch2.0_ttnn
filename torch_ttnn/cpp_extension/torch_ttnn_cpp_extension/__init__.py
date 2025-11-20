"""Torch TTNN C++ Extension Package

This package contains the compiled C++ extension library for PyTorch TTNN.
"""

__version__ = "0.1.0"

# Import the compiled extension module
# In editable installs, the module is installed in site-packages but we need to make it available
import sys
import os
from pathlib import Path

# Try to import ttnn_device_extension from various possible locations
_extension_imported = False

# First, try direct import (works for regular installs)
try:
    import ttnn_device_extension

    _extension_imported = True
except ImportError:
    pass

# If not found, try to import from site-packages (for editable installs)
if not _extension_imported:
    try:
        import site

        for site_dir in site.getsitepackages():
            ext_path = Path(site_dir) / "torch_ttnn_cpp_extension" / "ttnn_device_extension"
            if ext_path.exists():
                # Add the directory to sys.path temporarily
                sys.path.insert(0, str(ext_path.parent))
                import ttnn_device_extension

                sys.path.pop(0)
                _extension_imported = True
                break
    except (ImportError, Exception):
        pass

# If still not found, try from build directory (for development)
if not _extension_imported:
    try:
        # Get the package directory
        package_dir = Path(__file__).parent.parent
        # Look for build directories
        for build_dir in package_dir.glob("**/build/**/torch_ttnn_cpp_extension"):
            ext_path = build_dir / "ttnn_device_extension"
            if ext_path.exists():
                sys.path.insert(0, str(build_dir))
                import ttnn_device_extension

                sys.path.pop(0)
                _extension_imported = True
                break
    except (ImportError, Exception):
        pass

if not _extension_imported:
    raise ImportError(
        "Could not import ttnn_device_extension. " "Please ensure the C++ extension is built and installed correctly."
    )
