# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
"""
Test for Stable Diffusion 1.4 (512x512)
GitHub Issue #1041: Add model: Stable Diffusion 1.4 (512x512)

Target: 0.3 FPS on batch 1
Baseline: 0.117 FPS on batch 1
"""

# Constants
BASELINE_FPS = 0.117
from diffusers import StableDiffusionPipeline
import torch
import pytest
import time

try:
    import psutil
except ImportError:
    psutil = None
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        model_id = "CompVis/stable-diffusion-v1-4"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            use_safetensors=True,
            safety_checker=None,
            requires_safety_checker=False,
        )
        return pipe

    def _load_inputs(self, batch_size):
        prompt = "a photo of an astronaut riding a horse on mars"
        return [prompt] * batch_size


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_stable_diffusion(record_property, mode):
    """Test Stable Diffusion 1.4 model performance."""
    model_name = "Stable Diffusion 1.4"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)

    # Measure memory before
    if psutil:
        process = psutil.Process()
        mem_before = process.memory_info().rss / 1024 / 1024  # in MB
    else:
        mem_before = None

    # Performance measurement
    start = time.time()
    results = tester.test_model()
    end = time.time()

    if mode == "eval":
        image = results.images[0]
        record_property("image_generated", True)

    # Measure memory after
    if psutil:
        mem_after = process.memory_info().rss / 1024 / 1024  # in MB
    else:
        mem_after = None

    elapsed = end - start
    fps = 1.0 / elapsed if elapsed > 0 else 0.0

    # Record performance metrics
    record_property("inference_time_sec", elapsed)
    record_property("fps", fps)
    record_property("target_fps", 0.3)
    record_property("baseline_fps", BASELINE_FPS)
    record_property("performance_improvement", fps / BASELINE_FPS if fps > 0 else 0)

    if mem_before is not None and mem_after is not None:
        record_property("memory_usage_mb", mem_after - mem_before)

    record_property("torch_ttnn", (tester, results))

    # Performance validation
    if fps >= 0.3:
        record_property("target_achieved", True)
        print(f"✅ TARGET ACHIEVED: {fps:.3f} FPS >= 0.3 FPS target")
    else:
        record_property("target_achieved", False)
        print(f"⚠️ TARGET NOT MET: {fps:.3f} FPS < 0.3 FPS target")
