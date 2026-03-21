# SPDX-License-Identifier: MIT

import torch
import numpy as np
from typing import Union, Dict, Optional, List, Tuple
import ttnn


def preprocess_image(image: torch.Tensor) -> torch.Tensor:
    """Preprocess input image for stable diffusion pipeline."""
    # Normalize from [0, 1] to [-1, 1]
    if image.max() > 1.0:
        image = image / 255.0
    image = (image - 0.5) * 2.0
    return image


def postprocess_image(image: torch.Tensor) -> torch.Tensor:
    """Postprocess output image from stable diffusion pipeline."""
    # Denormalize from [-1, 1] to [0, 1]
    image = (image + 1.0) / 2.0
    image = torch.clamp(image, 0.0, 1.0)
    return image


def encode_image_to_latents(image: torch.Tensor, vae_encoder) -> torch.Tensor:
    """Encode image to latent space using VAE encoder."""
    with torch.no_grad():
        latents = vae_encoder(image)
        latents = latents * 0.18215  # VAE scaling factor
    return latents


def decode_latents_to_image(latents: torch.Tensor, vae_decoder) -> torch.Tensor:
    """Decode latents to image using VAE decoder."""
    latents = latents / 0.18215  # VAE scaling factor
    with torch.no_grad():
        image = vae_decoder(latents)
    return image


class DDIMScheduler:
    """DDIM scheduler for noise scheduling in stable diffusion."""

    def __init__(self, num_train_timesteps: int = 1000, beta_start: float = 0.00085, beta_end: float = 0.012):
        self.num_train_timesteps = num_train_timesteps
        self.beta_start = beta_start
        self.beta_end = beta_end

        # Create beta schedule
        self.betas = torch.linspace(beta_start, beta_end, num_train_timesteps)
        self.alphas = 1.0 - self.betas
        self.alphas_cumprod = torch.cumprod(self.alphas, dim=0)

        self.timesteps = None

    def set_timesteps(self, num_inference_steps: int):
        """Set timesteps for inference."""
        step_ratio = self.num_train_timesteps // num_inference_steps
        timesteps = (np.arange(0, num_inference_steps) * step_ratio).round()[::-1].copy().astype(np.int64)
        self.timesteps = torch.from_numpy(timesteps)

    def scale_model_input(self, sample: torch.Tensor, timestep: int) -> torch.Tensor:
        """Scale model input for DDIM."""
        return sample

    def step(self, model_output: torch.Tensor, timestep: int, sample: torch.Tensor,
             eta: float = 0.0) -> torch.Tensor:
        """Perform one step of DDIM denoising."""
        prev_timestep = timestep - self.num_train_timesteps // len(self.timesteps)

        alpha_prod_t = self.alphas_cumprod[timestep]
        alpha_prod_t_prev = self.alphas_cumprod[prev_timestep] if prev_timestep >= 0 else torch.tensor(1.0)

        beta_prod_t = 1 - alpha_prod_t

        # Compute predicted original sample
        pred_original_sample = (sample - beta_prod_t ** 0.5 * model_output) / alpha_prod_t ** 0.5

        # Compute variance
        variance = (1 - alpha_prod_t_prev) / (1 - alpha_prod_t) * (1 - alpha_prod_t / alpha_prod_t_prev)
        std_dev_t = eta * variance ** 0.5

        # Compute predicted sample
        pred_sample_direction = (1 - alpha_prod_t_prev - std_dev_t**2) ** 0.5 * model_output

        prev_sample = alpha_prod_t_prev ** 0.5 * pred_original_sample + pred_sample_direction

        if eta > 0:
            noise = torch.randn_like(model_output)
            prev_sample = prev_sample + std_dev_t * noise

        return prev_sample


def torch_to_ttnn(tensor: torch.Tensor, device: ttnn.Device, layout: ttnn.Layout = ttnn.ROW_MAJOR_LAYOUT) -> ttnn.Tensor:
    """Convert PyTorch tensor to TTNN tensor."""
    ttnn_tensor = ttnn.from_torch(tensor, dtype=ttnn.bfloat16, layout=layout)
    ttnn_tensor = ttnn.to_device(ttnn_tensor, device)
    return ttnn_tensor


def ttnn_to_torch(tensor: ttnn.Tensor) -> torch.Tensor:
    """Convert TTNN tensor to PyTorch tensor."""
    tensor = ttnn.to_torch(tensor)
    return tensor


def prepare_text_embeddings(prompt: str, tokenizer, text_encoder, max_length: int = 77) -> torch.Tensor:
    """Prepare text embeddings from prompt string."""
    # Tokenize text
    text_inputs = tokenizer(
        prompt,
        padding="max_length",
        max_length=max_length,
        truncation=True,
        return_tensors="pt"
    )

    # Get text embeddings
    with torch.no_grad():
        text_embeddings = text_encoder(text_inputs.input_ids)[0]

    # Prepare unconditional embeddings for classifier-free guidance
    uncond_tokens = [""]
    uncond_inputs = tokenizer(
        uncond_tokens,
        padding="max_length",
        max_length=max_length,
        return_tensors="pt"
    )

    with torch.no_grad():
        uncond_embeddings = text_encoder(uncond_inputs.input_ids)[0]

    # Concatenate embeddings
    text_embeddings = torch.cat([uncond_embeddings, text_embeddings])

    return text_embeddings


def prepare_latent_noise(batch_size: int, height: int, width: int, device: str = "cpu") -> torch.Tensor:
    """Prepare initial latent noise tensor."""
    latent_height = height // 8
    latent_width = width // 8
    latents = torch.randn(
        batch_size, 4, latent_height, latent_width,
        device=device, dtype=torch.float32
    )
    return latents


def load_model_weights(model, checkpoint_path: str, device: str = "cpu") -> None:
    """Load model weights from checkpoint."""
    checkpoint = torch.load(checkpoint_path, map_location=device)
    if "state_dict" in checkpoint:
        state_dict = checkpoint["state_dict"]
    else:
        state_dict = checkpoint

    # Remove module prefix if present
    new_state_dict = {}
    for key, value in state_dict.items():
        if key.startswith("module."):
            new_key = key[7:]
        else:
            new_key = key
        new_state_dict[new_key] = value

    model.load_state_dict(new_state_dict, strict=False)


def setup_ttnn_device(device_id: int = 0) -> ttnn.Device:
    """Setup TTNN device for inference."""
    device = ttnn.open_device(device_id=device_id)
    return device


def close_ttnn_device(device: ttnn.Device) -> None:
    """Close TTNN device."""
    ttnn.close_device(device)


def pad_tensor_to_multiple(tensor: torch.Tensor, multiple: int, dim: int = -1) -> torch.Tensor:
    """Pad tensor to make dimension divisible by multiple."""
    size = tensor.size(dim)
    remainder = size % multiple
    if remainder != 0:
        pad_size = multiple - remainder
        pad_shape = [0] * (tensor.ndim * 2)
        pad_shape[-(dim * 2 + 1)] = pad_size
        tensor = torch.nn.functional.pad(tensor, pad_shape)
    return tensor


def create_attention_mask(seq_length: int, device: str = "cpu") -> torch.Tensor:
    """Create causal attention mask for text encoder."""
    mask = torch.tril(torch.ones(seq_length, seq_length, device=device))
    mask = mask.unsqueeze(0).unsqueeze(0)
    return mask


def interpolate_embeddings(embeddings: torch.Tensor, target_length: int) -> torch.Tensor:
    """Interpolate embeddings to target length."""
    if embeddings.size(1) == target_length:
        return embeddings

    embeddings = embeddings.transpose(1, 2)
    embeddings = torch.nn.functional.interpolate(
        embeddings, size=target_length, mode="linear", align_corners=False
    )
    embeddings = embeddings.transpose(1, 2)
    return embeddings


def get_guidance_scale_embeddings(prompt_embeds: torch.Tensor, negative_embeds: torch.Tensor,
                                guidance_scale: float) -> torch.Tensor:
    """Apply classifier-free guidance scaling to embeddings."""
    guidance_embeds = negative_embeds + guidance_scale * (prompt_embeds - negative_embeds)
    return guidance_embeds
