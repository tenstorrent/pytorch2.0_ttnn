import torch
import torch.utils.cpp_extension
from torch.overrides import TorchFunctionMode
import os
from pathlib import Path
import glob
import logging
from pprint import pprint

# TODO: We need to swtich to cmake and use find script to find the include paths and libraries
ttnn_include_paths = [
    "/usr/include/tt-metal",
    "/usr/include/tt-metal/tt_stl",
    "/usr/include/tt-metal/ttnn",
    "/usr/include/tt-metal/ttnn/cpp",
    "/usr/include/tt-metal/tt_metal",
    "/usr/include/tt-metal/tt_metal/api",
    "/usr/include/tt-metal/tt_metal/third_party/umd/device/api",
    "/usr/include/tt-metal/tt_metal/third_party/tracy/public",
    "/usr/include/tt-metal/tt_metal/hostdevcommon/api",
    "/usr/include/tt-metal/third-party/",
]

# Load the C++ extension containing your custom kernels.
tt_metal_lib_paths = ["/usr/lib"]  # ttnn_module_dir / Path("build/lib"),
tt_metal_lib_paths = ["-L" + str(p) + " -Wl,-rpath=" + str(p) for p in tt_metal_lib_paths]
tt_metal_libs = [
    "tt_metal",
    ":_ttnn.so",
    "device",
]
tt_metal_libs = ["-l" + p for p in tt_metal_libs]

# Use clang to match ttnn build
os.environ["CXX"] = "clang++-17"

working_file_path = Path(os.path.realpath(__file__))
working_directory = working_file_path.parents[0]
src_directory = working_directory / Path("src")

# Automatically compile all .cpp files in this same directory
source_file_pattern = Path("*.cpp")
source_files = list(glob.glob(str(src_directory / source_file_pattern), recursive=False))
source_files += list(glob.glob(str(src_directory / "core" / source_file_pattern), recursive=False))
source_files += list(glob.glob(str(src_directory / "ops" / source_file_pattern), recursive=False))
source_files += list(glob.glob(str(src_directory / "utils" / source_file_pattern), recursive=False))

extra_cflags = ["-g", "-DFMT_HEADER_ONLY", "-std=c++20"]
# Undefine the following problematic macros https://github.com/tenstorrent/tt-metal/issues/20361
extra_cflags += ["-UPYBIND11_COMPILER_TYPE", "-UPYBIND11_BUILD_ABI"]

ttnn_module = torch.utils.cpp_extension.load(
    name="ttnn_device_extension",
    sources=source_files,
    extra_include_paths=[str(working_directory / "include")] + ttnn_include_paths,
    extra_cflags=extra_cflags,
    extra_ldflags=tt_metal_lib_paths + tt_metal_libs,
    verbose=True,
)

logging.info("Loaded custom extension.")
torch.utils.rename_privateuse1_backend("ttnn")


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
                kwargs["device"] = ttnn_module.custom_device()
            else:
                # Case 2: The user specified a device index.
                device_idx = int(device_and_idx[1])
                kwargs["device"] = ttnn_module.custom_device(device_idx)
        with torch._C.DisableTorchFunction():
            return func(*args, **kwargs)
