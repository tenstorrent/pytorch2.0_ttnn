import torch
from diffusers import StableDiffusionPipeline


MODEL_ID = "CompVis/stable-diffusion-v1-4"


def load_compiled_sd14_pipeline(torch_dtype: torch.dtype = torch.float32) -> StableDiffusionPipeline:
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch_dtype)
    pipe.unet = torch.compile(pipe.unet, backend="ttnn", fullgraph=False, dynamic=False)
    pipe.vae = torch.compile(pipe.vae, backend="ttnn", fullgraph=False, dynamic=False)
    pipe.text_encoder = torch.compile(pipe.text_encoder, backend="ttnn", fullgraph=False, dynamic=False)
    return pipe
