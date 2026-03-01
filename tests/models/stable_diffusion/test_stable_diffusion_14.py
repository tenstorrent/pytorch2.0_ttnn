# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from pathlib import Path

import numpy as np
import pytest
import torch
from diffusers import UNet2DConditionModel
from PIL import Image
from scipy.stats import pearsonr

from models.demos.stable_diffusion.sd14_pipeline import load_compiled_sd14_pipeline
from models.demos.stable_diffusion.unet_wrapper import MODEL_ID, load_compiled_unet

PROMPT = "a photo of an astronaut riding a horse on mars"
SEED = 42
NUM_INFERENCE_STEPS = 20
GOLDEN_IMAGE_PATH = Path(__file__).resolve().parent / "golden_cpu_seed42.png"


def _extract_sample(unet_output):
    if hasattr(unet_output, "sample"):
        return unet_output.sample
    if isinstance(unet_output, (tuple, list)):
        return unet_output[0]
    return unet_output


def _make_unet_inputs(batch=1, seed=42, dtype=torch.float32, device="cpu"):
    torch.manual_seed(seed)
    sample = torch.randn(batch, 4, 64, 64, dtype=dtype, device=device)
    timestep = torch.tensor(0, dtype=torch.int64, device=device)
    encoder_hidden_states = torch.randn(batch, 77, 768, dtype=dtype, device=device)
    return sample, timestep, encoder_hidden_states


@pytest.fixture(scope="module")
def sd14_pipeline():
    pipe = load_compiled_sd14_pipeline(torch_dtype=torch.float32)
    pipe.set_progress_bar_config(disable=True)
    return pipe


@pytest.fixture(scope="module")
def compiled_unet():
    unet = load_compiled_unet(torch_dtype=torch.float32)
    unet.eval()
    return unet


@pytest.fixture(scope="module")
def cpu_unet():
    unet = UNet2DConditionModel.from_pretrained(MODEL_ID, subfolder="unet", torch_dtype=torch.float32)
    unet.eval()
    return unet


class TestSD14E2E:
    def test_pipeline_loads(self, sd14_pipeline):
        assert sd14_pipeline is not None
        assert sd14_pipeline.unet is not None
        assert sd14_pipeline.vae is not None
        assert sd14_pipeline.text_encoder is not None

    @torch.no_grad()
    def test_output_shape(self, sd14_pipeline):
        result = sd14_pipeline(
            prompt=PROMPT,
            num_inference_steps=1,
            guidance_scale=7.5,
            height=512,
            width=512,
        )
        assert len(result.images) > 0
        assert result.images[0].size == (512, 512)

    @torch.no_grad()
    def test_visual_parity(self, sd14_pipeline):
        assert GOLDEN_IMAGE_PATH.exists(), (
            f"Missing golden reference image at {GOLDEN_IMAGE_PATH}. "
            "Run models/demos/stable_diffusion/generate_golden.py first."
        )

        generator = torch.Generator(device="cpu").manual_seed(SEED)
        result = sd14_pipeline(
            prompt=PROMPT,
            num_inference_steps=NUM_INFERENCE_STEPS,
            guidance_scale=7.5,
            height=512,
            width=512,
            generator=generator,
        )

        output_image = np.asarray(result.images[0].convert("RGB"), dtype=np.float32).reshape(-1)
        golden_image = np.asarray(Image.open(GOLDEN_IMAGE_PATH).convert("RGB"), dtype=np.float32).reshape(-1)

        assert output_image.shape == golden_image.shape
        corr = pearsonr(output_image, golden_image)
        corr_value = corr.statistic if hasattr(corr, "statistic") else corr[0]
        assert corr_value > 0.80, f"Pearson correlation too low: {corr_value:.4f}"


class TestSD14UNetParity:
    @torch.no_grad()
    def test_unet_output_shape(self, compiled_unet):
        parameter = next(compiled_unet.parameters())
        sample, timestep, encoder_hidden_states = _make_unet_inputs(
            batch=1, seed=42, dtype=parameter.dtype, device=parameter.device
        )
        output = _extract_sample(
            compiled_unet(sample=sample, timestep=timestep, encoder_hidden_states=encoder_hidden_states)
        )
        assert tuple(output.shape) == (1, 4, 64, 64)

    @torch.no_grad()
    def test_unet_parity_vs_cpu(self, compiled_unet, cpu_unet):
        cpu_sample, cpu_timestep, cpu_encoder_hidden_states = _make_unet_inputs(batch=1, seed=42, dtype=torch.float32)
        cpu_output = _extract_sample(
            cpu_unet(sample=cpu_sample, timestep=cpu_timestep, encoder_hidden_states=cpu_encoder_hidden_states)
        )

        parameter = next(compiled_unet.parameters())
        compiled_sample = cpu_sample.to(device=parameter.device, dtype=parameter.dtype)
        compiled_timestep = cpu_timestep.to(device=parameter.device)
        compiled_encoder_hidden_states = cpu_encoder_hidden_states.to(device=parameter.device, dtype=parameter.dtype)

        compiled_output = _extract_sample(
            compiled_unet(
                sample=compiled_sample,
                timestep=compiled_timestep,
                encoder_hidden_states=compiled_encoder_hidden_states,
            )
        )

        compiled_output = compiled_output.detach().float().cpu()
        cpu_output = cpu_output.detach().float().cpu()

        diff = compiled_output - cpu_output
        rel_l2 = torch.linalg.vector_norm(diff) / (torch.linalg.vector_norm(cpu_output) + 1e-8)
        max_abs = diff.abs().max()

        assert rel_l2.item() < 0.05
        assert max_abs.item() < 0.5
