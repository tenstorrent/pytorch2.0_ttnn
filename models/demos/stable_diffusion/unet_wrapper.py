import torch
from diffusers import UNet2DConditionModel


MODEL_ID = "CompVis/stable-diffusion-v1-4"


def load_compiled_unet(torch_dtype: torch.dtype = torch.float32):
    unet = UNet2DConditionModel.from_pretrained(MODEL_ID, subfolder="unet", torch_dtype=torch_dtype)
    return torch.compile(unet, backend="ttnn", fullgraph=False, dynamic=False)


def run_unet_boundary_test(compiled_unet, batch: int = 1, seed: int = 42):
    torch.manual_seed(seed)
    parameter = next(compiled_unet.parameters())
    device = parameter.device
    dtype = parameter.dtype

    sample = torch.randn(batch, 4, 64, 64, device=device, dtype=dtype)
    timestep = torch.tensor(0, device=device, dtype=torch.int64)
    encoder_hidden_states = torch.randn(batch, 77, 768, device=device, dtype=dtype)
    return compiled_unet(sample=sample, timestep=timestep, encoder_hidden_states=encoder_hidden_states)
