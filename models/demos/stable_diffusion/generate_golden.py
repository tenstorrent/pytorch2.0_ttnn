from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "CompVis/stable-diffusion-v1-4"
PROMPT = "a photo of an astronaut riding a horse on mars"
SEED = 42
NUM_INFERENCE_STEPS = 20
OUTPUT_PATH = Path(__file__).resolve().parents[3] / "tests/models/stable_diffusion/golden_cpu_seed42.png"


def main() -> None:
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")
    pipe.set_progress_bar_config(disable=True)

    generator = torch.Generator(device="cpu").manual_seed(SEED)

    with torch.no_grad():
        result = pipe(
            prompt=PROMPT,
            num_inference_steps=NUM_INFERENCE_STEPS,
            guidance_scale=7.5,
            height=512,
            width=512,
            generator=generator,
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    result.images[0].save(OUTPUT_PATH)
    print(f"Saved CPU golden image to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
