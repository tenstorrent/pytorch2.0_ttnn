import json
import time
from pathlib import Path
from statistics import mean

import torch

from models.demos.stable_diffusion.sd14_pipeline import load_compiled_sd14_pipeline

PROMPT = "a photo of an astronaut riding a horse on mars"
RESULTS_PATH = Path("perf_results_sd14.json")


def _run_once(pipe, steps: int) -> float:
    start_time = time.perf_counter()
    with torch.inference_mode():
        pipe(
            prompt=PROMPT,
            num_inference_steps=steps,
            guidance_scale=7.5,
            height=512,
            width=512,
        )
    return time.perf_counter() - start_time


def run_perf_report(steps: int = 20, warmup: int = 2, trials: int = 5):
    if steps <= 0:
        raise ValueError("steps must be > 0")
    if warmup < 0:
        raise ValueError("warmup must be >= 0")
    if trials <= 0:
        raise ValueError("trials must be > 0")

    pipe = load_compiled_sd14_pipeline(torch_dtype=torch.float32)
    pipe.set_progress_bar_config(disable=True)

    for _ in range(warmup):
        _run_once(pipe, steps)

    latencies = [_run_once(pipe, steps) for _ in range(trials)]

    avg_latency_s = mean(latencies)
    best_latency_s = min(latencies)
    worst_latency_s = max(latencies)
    avg_fps = 1.0 / avg_latency_s
    best_fps = 1.0 / best_latency_s

    report = {
        "avg_latency_s": avg_latency_s,
        "best_latency_s": best_latency_s,
        "worst_latency_s": worst_latency_s,
        "avg_fps": avg_fps,
        "best_fps": best_fps,
    }

    report_json = json.dumps(report, indent=2)
    print(report_json)
    RESULTS_PATH.write_text(report_json + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    run_perf_report()
