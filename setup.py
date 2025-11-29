# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import os
from setuptools import setup, find_packages


def read_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


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
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.10",
    install_requires=[
        "torch==2.7.1+cpu",
        "torchvision==0.22.1+cpu",
        "tabulate==0.9.0",
        "networkx==3.1",
        "graphviz",
        "matplotlib==3.7.1",
        "paramiko==3.5.1",
        "ttnn==0.62.0rc36.dev2326",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.3",
        ],
    },
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
