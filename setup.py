# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import os
from setuptools import setup, find_packages


def read_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#') and not line.startswith('-r')]


setup(
    name="torch-ttnn",
    description="PyTorch 2.0 TTNN Compiler",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tenstorrent/pytorch2.0_ttnn",
    author="Tenstorrent",
    author_email="info@tenstorrent.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Ubuntu",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.10",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "ttnn": [
            "ttnn @ https://github.com/tenstorrent/tt-metal/releases/download/v0.59.0-rc31/ttnn-0.59.0rc31-cp310-cp310-linux_x86_64.whl ; python_version=='3.10' and platform_system=='Linux' and platform_machine=='x86_64'",
        ],
        "dev": read_requirements("requirements-dev.txt"),
    },
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
