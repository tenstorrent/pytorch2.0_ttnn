import torch
from diffusers import StableDiffusionPipeline, UNet2DConditionModel, LMSDiscreteScheduler
from transformers import CLIPTextModel, CLIPTokenizer
import pytest


@pytest.mark.compilation_xfail
def test_stable_diffusion_v2(record_property):
    record_property("model_name", "Stable Diffusion")

    # Load the pre-trained model and tokenizer
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
    text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")
    unet = UNet2DConditionModel.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="unet")
    scheduler = LMSDiscreteScheduler.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="scheduler")

    # Prepare the text prompt
    prompt = "A fantasy landscape with mountains and rivers"
    text_input = tokenizer(prompt, return_tensors="pt")
    text_embeddings = text_encoder(text_input.input_ids)[0]

    # Generate noise
    batch_size = text_embeddings.shape[0]
    height, width = 512, 512  # Output image size
    latents = torch.randn((batch_size, unet.in_channels, height // 8, width // 8))

    # Set number of diffusion steps
    num_inference_steps = 1
    scheduler.set_timesteps(num_inference_steps)

    # Scale the latent noise to match the model's expected input
    latents = latents * scheduler.init_noise_sigma

    # Get the model's predicted noise
    latent_model_input = scheduler.scale_model_input(latents, 0)
    arguments = {"sample": latent_model_input, "timestep": 0, "encoder_hidden_states": text_embeddings}
    output = unet(**arguments)

    noise_pred = output.sample

    record_property("torch_ttnn", (unet, arguments, output))
