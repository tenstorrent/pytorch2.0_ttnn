import hashlib

import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "CompVis/stable-diffusion-v1-4"
UNET_PARAM_RANGE = (859_000_000, 861_000_000)
VAE_PARAM_RANGE = (83_000_000, 85_000_000)
EXPECTED_CONV_IN_SHA256 = "7bf03b261c92b2ed03e7f7d426e8c852468dcfdc98b350259ca56a4edf173980"


def _count_parameters(module: torch.nn.Module) -> int:
    return sum(parameter.numel() for parameter in module.parameters())


def _sha256_tensor(tensor: torch.Tensor) -> str:
    tensor_bytes = tensor.detach().cpu().contiguous().numpy().tobytes()
    return hashlib.sha256(tensor_bytes).hexdigest()


def main() -> None:
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float32)

    unet_params = _count_parameters(pipe.unet)
    vae_params = _count_parameters(pipe.vae)

    assert UNET_PARAM_RANGE[0] <= unet_params <= UNET_PARAM_RANGE[1], (
        f"UNet parameter count {unet_params} outside range {UNET_PARAM_RANGE}"
    )
    assert VAE_PARAM_RANGE[0] <= vae_params <= VAE_PARAM_RANGE[1], (
        f"VAE parameter count {vae_params} outside range {VAE_PARAM_RANGE}"
    )

    conv_in_sha256 = _sha256_tensor(pipe.unet.conv_in.weight)
    assert conv_in_sha256 == EXPECTED_CONV_IN_SHA256, (
        "UNet conv_in.weight SHA256 mismatch: "
        f"expected {EXPECTED_CONV_IN_SHA256}, got {conv_in_sha256}"
    )

    print("Stable Diffusion v1.4 weights verified successfully.")
    print(f"UNet parameters: {unet_params}")
    print(f"VAE parameters: {vae_params}")
    print(f"UNet conv_in.weight SHA256: {conv_in_sha256}")


if __name__ == "__main__":
    main()
