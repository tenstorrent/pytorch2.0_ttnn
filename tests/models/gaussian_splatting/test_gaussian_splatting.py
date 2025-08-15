# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://github.com/hbb1/torch-splatting

import numpy as np
import os
import pytest
import requests
import subprocess
import sys
import torch
import zipfile

from tests.utils import ModelTester

# Path to patched gaussian splatting implementation that is compatible with TT
github_url = "https://github.com/kevinwuTT/torch-splatting/archive/refs/heads/tt-compat.zip"
# Full path of this Python script
test_path = os.path.dirname(os.path.realpath(__file__))
# Path of gaussian splatting module after extraction
gs_module_path = f"{test_path}/torch-splatting-tt-compat"


# Download the zip from github, extract, and load directory as a Python module
def setup_gs_module():
    try:
        response = requests.get(github_url)
    except Exception as e:
        print(f"Error downloading URL: {github_url}")
        raise e

    assert response.status_code == 200

    # Write to disk and extract
    zip_path = f"{test_path}/tt-compat.zip"
    open(zip_path, "wb").write(response.content)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(path=test_path)

    # Load module into PYTHONPATH
    sys.path.append(gs_module_path)

    # Extract dataset from reference repo:
    # https://github.com/hbb1/torch-splatting/blob/main/B075X65R3X.zip
    # These are images with depth, rgb, and other point information.
    with zipfile.ZipFile(f"{gs_module_path}/B075X65R3X.zip", "r") as zip_ref:
        zip_ref.extractall(path=gs_module_path)

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "imageio", "accelerate", "einops", "numpy>=1.24.4,<2"]
    )


class ThisTester(ModelTester):
    def __init__(self, model_name, mode, batch_size, steps, fp16):
        self.steps = steps
        self.fp16 = fp16
        super().__init__(model_name, mode, batch_size)

    def _load_model(self):
        # set up model
        from gaussian_splatting.gauss_model import GaussModel

        gaussModel = GaussModel(
            sh_degree=4,
            debug=False,
        )

        return gaussModel

    def _load_inputs(self, batch_size):
        # input data processing
        from gaussian_splatting.utils.data_utils import read_all

        dtype = torch.float16 if self.fp16 else torch.float

        folder = f"{gs_module_path}/B075X65R3X"
        data = read_all(folder, resize_factor=0.5)
        data = {k: v.to(dtype) for k, v in data.items()}
        data["depth_range"] = torch.Tensor([[1, 3]] * len(data["rgb"])).to(dtype)

        return data

    def setup_gsstrainer(self, as_ttnn=False, option=None):
        from train import GSSTrainer
        from gaussian_splatting.utils.point_utils import get_point_clouds
        from gaussian_splatting.gauss_render import GaussRenderer

        gaussModel = self.model
        data = self.inputs
        points = get_point_clouds(data["camera"], data["depth"], data["alpha"], data["rgb"])
        raw_points = points.random_sample(2**14)

        gaussModel.create_from_pcd(pcd=raw_points)
        render_kwargs = {
            "white_bkgd": True,
        }
        gaussRenderer = GaussRenderer(**render_kwargs)

        if as_ttnn == True:
            gaussRenderer = self.compile_model(gaussRenderer, option)

        trainer = GSSTrainer(
            model=gaussModel,
            data=data,
            train_batch_size=self.batch_size,
            train_num_steps=self.steps,
            i_image=100,
            train_lr=1e-3,
            amp=False,
            fp16=self.fp16,
            results_folder="result/test",
            gauss_render_model=gaussRenderer,
            render_kwargs=render_kwargs,
        )

        return trainer

    def test_model_eval(self, as_ttnn=False, option=None):
        trainer = self.setup_gsstrainer(as_ttnn, option)
        trainer.on_evaluate_step()
        out = trainer.eval_results
        return out

    def test_model_train(self, as_ttnn=False, option=None):
        trainer = self.setup_gsstrainer(as_ttnn, option)
        trainer.on_evaluate_step()
        trainer.train()
        out = trainer.train_results
        return out


@pytest.mark.parametrize(
    "mode",
    ["eval", "train"],
)
@pytest.mark.parametrize(
    "batch_size",
    [1],
)
@pytest.mark.parametrize(
    "steps",
    [1],
)
@pytest.mark.parametrize(
    "fp16",
    [True],
)
def test_gaussian_splatting(record_property, mode, batch_size, steps, fp16):
    torch.manual_seed(99)
    np.random.seed(99)

    setup_gs_module()

    model_name = "GaussianSplatting"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, batch_size, steps, fp16)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
