import torch
from torch.overrides import TorchFunctionMode
import logging
import sys
from pathlib import Path

# Import ttnn_device_extension module
# First try direct import (works for regular installs)
try:
    import ttnn_device_extension as ttnn_module
except ImportError:
    # For editable installs, the module is installed in site-packages/torch_ttnn_cpp_extension/ttnn_device_extension
    # but editable install overrides the package, so we need to load it manually
    import site
    import importlib.util
    from importlib.machinery import ExtensionFileLoader

    _imported = False

    for site_dir in site.getsitepackages():
        ext_dir = Path(site_dir) / "torch_ttnn_cpp_extension"

        # Try to find the extension file (with or without .so extension)
        ext_file = None
        for possible_name in ["ttnn_device_extension.so", "ttnn_device_extension"]:
            candidate = ext_dir / possible_name
            if candidate.exists() and candidate.is_file():
                ext_file = candidate
                break

        if ext_file and ext_file.exists():
            # Add directory to sys.path for import
            if str(ext_dir) not in sys.path:
                sys.path.insert(0, str(ext_dir))
            try:
                # Try direct import first
                import ttnn_device_extension as ttnn_module

                _imported = True
                break
            except ImportError:
                # Direct import failed, use ExtensionFileLoader to load the file
                try:
                    # ExtensionFileLoader can handle files with or without .so extension
                    # Python will automatically add the extension if needed
                    loader = ExtensionFileLoader("ttnn_device_extension", str(ext_file))
                    spec = importlib.util.spec_from_loader("ttnn_device_extension", loader)
                    if spec and spec.loader:
                        ttnn_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(ttnn_module)
                        _imported = True
                        break
                except Exception as e:
                    # Log the error for debugging
                    error_msg = str(e)
                    logging.debug(f"Failed to load via ExtensionFileLoader from {ext_file}: {error_msg}")
                    # If it's a library loading error, it might be LD_LIBRARY_PATH issue
                    if "cannot open shared object file" in error_msg or "undefined symbol" in error_msg:
                        logging.warning(f"Library loading error: {error_msg}")
                        logging.warning("This might be due to missing libraries in LD_LIBRARY_PATH")
                    # Try with explicit .so extension if file doesn't have it
                    if not str(ext_file).endswith(".so"):
                        try:
                            so_candidate = ext_dir / "ttnn_device_extension.so"
                            if so_candidate.exists():
                                loader = ExtensionFileLoader("ttnn_device_extension", str(so_candidate))
                                spec = importlib.util.spec_from_loader("ttnn_device_extension", loader)
                                if spec and spec.loader:
                                    ttnn_module = importlib.util.module_from_spec(spec)
                                    spec.loader.exec_module(ttnn_module)
                                    _imported = True
                                    break
                        except Exception as e2:
                            logging.debug(f"Failed to load with .so extension: {e2}")
                    pass
                # Remove from path if import failed
                if str(ext_dir) in sys.path:
                    sys.path.remove(str(ext_dir))

    if not _imported:
        raise ImportError(
            "Could not import ttnn_device_extension. "
            "Please ensure the C++ extension is built and installed correctly. "
            f"Searched in: {[str(Path(d) / 'torch_ttnn_cpp_extension') for d in site.getsitepackages()]}"
        )

logging.info("Using pre-built ttnn_device_extension")

# Register PrivateUse1 as "ttnn" backend
torch.utils.rename_privateuse1_backend("ttnn")

# Make the module available as torch.ttnn for PyTorch's custom backend system
# When PyTorch encounters a "ttnn" device, it tries to import torch.ttnn
# We provide the ttnn_device_extension module at this location
sys.modules["torch.ttnn"] = ttnn_module


# The user will globally enable the below mode when calling this API
def enable_ttnn_device():
    m = TtnnDeviceMode()
    m.__enter__()
    # If you want the mode to never be disabled, then this function shouldn't return anything.
    return m


# This is a simple TorchFunctionMode class that:
# (a) Intercepts all torch.* calls
# (b) Checks for kwargs of the form `device="ttnn:i"`
# (c) Turns those into custom device objects: `device=ttnn_module.custom_device(i)`
# (d) Forwards the call along into pytorch.
class TtnnDeviceMode(TorchFunctionMode):
    def __torch_function__(self, func, types, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        if "device" in kwargs and "ttnn" in kwargs["device"]:
            device_and_idx = kwargs["device"].split(":")
            if len(device_and_idx) == 1:
                # Case 1: No index specified
                kwargs["device"] = ttnn_module.open_torch_device()
            else:
                # Case 2: The user specified a device index.
                device_idx = int(device_and_idx[1])
                kwargs["device"] = ttnn_module.open_torch_device(device_idx)
        with torch._C.DisableTorchFunction():
            return func(*args, **kwargs)
