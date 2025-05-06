import os
import sys
import subprocess
from setuptools import setup, Extension, find_namespace_packages
from setuptools.command.build_ext import build_ext
import sysconfig
import torch


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
            # f"-DCMAKE_BUILD_TYPE=Debug",
            f"-DTORCH_INSTALL_PREFIX={sysconfig.get_paths()['purelib']}",
            f"-DCMAKE_PREFIX_PATH={torch.utils.cmake_prefix_path}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DENABLE_LOCAL_TT_METAL_BUILD=ON",
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))}",
            f"-DOUTPUT_NAME={os.path.basename(self.get_ext_fullpath(ext.name))}",
            f"-G",
            f"Ninja",
        ]
        cmake_args.extend(ext.cmake_args)

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
            cmake_args=["-DCMAKE_CXX_COMPILER=clang++-17"],
        ),
    ],
    cmdclass={"build_ext": CMakeBuild},
    python_requires=">=3.8",
)
