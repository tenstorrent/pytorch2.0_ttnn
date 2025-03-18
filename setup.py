# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from setuptools import setup


def version_scheme(version):
    with open("VERSION") as f:
        version = f.read().strip()
    return version


setup(
    name="torch-ttnn",
    description="PyTorch dynamo backend for Tenstorrent TT-NN framework",
    url="https://github.com/tenstorrent/pytorch2.0_ttnn",
    use_scm_version={
        "version_scheme": version_scheme,
        "local_scheme": "node-and-date",
    },
    packages=["torch_ttnn"],
)
