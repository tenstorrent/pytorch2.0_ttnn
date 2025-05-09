import os
import sys
import subprocess
from setuptools import setup, Extension, find_namespace_packages
from setuptools.command.build_ext import build_ext
import sysconfig
import torch
from pprint import pprint
import re


def get_torch_abi_related_compiler_flags():
    """Extract compiler flags relaed to abi from torch.__config__.show()"""
    config_str = torch.__config__.show()

    # Extract C++ flags
    cxx_flags = []

    # Look for C++ standard
    std_match = re.search(r"-std=c\+\+\d+", config_str)
    if std_match:
        cxx_flags.append(std_match.group(0))

    # Look for ABI flag, critical for compatibility
    abi_match = re.search(r"-D_GLIBCXX_USE_CXX11_ABI=(\d)", config_str)
    if abi_match:
        cxx_flags.append(f"-D_GLIBCXX_USE_CXX11_ABI={abi_match.group(1)}")

    fabi_match = re.search(r"-fabi-version=(\d+)", config_str)
    if fabi_match:
        cxx_flags.append(f"-fabi-version={fabi_match.group(1)}")

    return cxx_flags


class CMakeExtension(Extension):
    def __init__(self, name, source_dir=".", cmake_args=None, **kwargs):
        Extension.__init__(self, name, sources=[])
        self.source_dir = os.path.abspath(source_dir)
        self.cmake_args = cmake_args or []


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        if not isinstance(ext, CMakeExtension):
            super().build_extension(ext)
            return

        build_dir = os.path.join(self.build_temp, ext.name)
        os.makedirs(build_dir, exist_ok=True)

        # Configure CMake
        cmake_args = [
            f"-DCMAKE_BUILD_TYPE=Release",
            f"-DTORCH_INSTALL_PREFIX={sysconfig.get_paths()['purelib']}",
            f"-DCMAKE_PREFIX_PATH={torch.utils.cmake_prefix_path}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DENABLE_LOCAL_TT_METAL_BUILD=ON",
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))}",
            f"-DOUTPUT_NAME={os.path.basename(self.get_ext_fullpath(ext.name))}",
            f"-G",
            f"Ninja",
        ]
        extra_cmake_flags = os.environ.get("CMAKE_FLAGS", "")
        extra_cmake_flags = extra_cmake_flags.split(";")
        if "-DENABLE_SUBMODULE_TT_METAL_BUILD=ON" in extra_cmake_flags:
            extra_cmake_flags.append("-DENABLE_LOCAL_TT_METAL_BUILD=OFF")
            torch_cxx_flags = get_torch_abi_related_compiler_flags()
            if torch_cxx_flags:
                flags_str = " ".join(torch_cxx_flags)
                extra_cmake_flags.append(f'-DCMAKE_CXX_FLAGS="{flags_str}"')
            # Torch is built with gcc
            extra_cmake_flags.append("-DCMAKE_CXX_COMPILER=/usr/bin/g++")  # TODO: test different g++ versions

        else:
            cmake_args.append("-DCMAKE_CXX_COMPILER=clang++-17")
        if extra_cmake_flags:
            cmake_args.extend(extra_cmake_flags)

        cmake_args.extend(ext.cmake_args)
        pprint(cmake_args)

        # Build the extension
        subprocess.check_call(["cmake", ext.source_dir] + cmake_args, cwd=build_dir)
        subprocess.check_call(["cmake", "--build", ".", "--parallel"], cwd=build_dir)

        # Copy the extension to the correct location
        ext_path = self.get_ext_fullpath(ext.name)
        os.makedirs(os.path.dirname(ext_path), exist_ok=True)


setup(
    name="torch_ttnn_cpp_extension",
    version="0.1.0",
    packages=find_namespace_packages(include=["torch_ttnn*"]),
    ext_modules=[
        CMakeExtension(
            name="ttnn_device_extension",
            source_dir=".",
        ),
    ],
    cmdclass={"build_ext": CMakeBuild},
    python_requires=">=3.8",
)
