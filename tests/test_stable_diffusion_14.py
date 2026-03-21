import pytest
import torch
import ttnn
from PIL import Image
import numpy as np
from typing import Optional, Dict, Any


class StableDiffusion14Test:
    """Test harness for Stable Diffusion 1.4 model"""

    def __init__(self):
        self.model = None
        self.device = None
        self.tokenizer = None
        self.text_encoder = None
        self.unet = None
        self.vae = None

    def setup_model(self, device_id: int = 0):
        """Initialize the Stable Diffusion 1.4 model components"""
        try:
            # Setup TTNN device
            self.device = ttnn.open_device(device_id=device_id)

            # Load model components (assuming they exist in the repo)
            # This would need to be adapted based on actual model structure
            from models.stable_diffusion_14 import (
                StableDiffusion14Model,
                get_tokenizer,
                get_text_encoder,
                get_unet,
                get_vae
            )

            self.model = StableDiffusion14Model()
            self.tokenizer = get_tokenizer()
            self.text_encoder = get_text_encoder()
            self.unet = get_unet()
            self.vae = get_vae()

            # Move to device
            self.text_encoder = self.text_encoder.to(self.device)
            self.unet = self.unet.to(self.device)
            self.vae = self.vae.to(self.device)

            return True
        except Exception as e:
            print(f"Failed to setup model: {e}")
            return False

    def cleanup(self):
        """Clean up resources"""
        if self.device is not None:
            ttnn.close_device(self.device)
            self.device = None
        self.model = None
        self.tokenizer = None
        self.text_encoder = None
        self.unet = None
        self.vae = None


@pytest.fixture(scope="module")
def sd14_model():
    """Fixture for loading Stable Diffusion 1.4 model"""
    test_harness = StableDiffusion14Test()
    success = test_harness.setup_model()

    if not success:
        pytest.skip("Could not initialize Stable Diffusion 1.4 model")

    yield test_harness
    test_harness.cleanup()


@pytest.fixture
def sample_prompts():
    """Sample prompts for testing"""
    return [
        "a beautiful sunset over mountains",
        "a red cat sitting on a table",
        "abstract art with blue and green colors",
        "a spaceship flying through clouds"
    ]


def test_model_initialization(sd14_model):
    """Test that the model initializes correctly"""
    assert sd14_model.model is not None, "Model should be initialized"
    assert sd14_model.device is not None, "Device should be initialized"
    assert sd14_model.tokenizer is not None, "Tokenizer should be loaded"
    assert sd14_model.text_encoder is not None, "Text encoder should be loaded"
    assert sd14_model.unet is not None, "UNet should be loaded"
    assert sd14_model.vae is not None, "VAE should be loaded"


def test_text_encoding(sd14_model, sample_prompts):
    """Test CLIP text encoder with sample prompts"""
    for prompt in sample_prompts:
        # Tokenize text
        text_inputs = sd14_model.tokenizer(
            prompt,
            padding="max_length",
            max_length=77,
            truncation=True,
            return_tensors="pt"
        )

        # Encode text
        with torch.no_grad():
            text_embeddings = sd14_model.text_encoder(
                ttnn.from_torch(text_inputs.input_ids, device=sd14_model.device)
            )

        # Verify output shape and type
        assert text_embeddings is not None, f"Text encoding failed for prompt: {prompt}"

        # Convert back to torch for shape checking
        text_emb_torch = ttnn.to_torch(text_embeddings)
        assert text_emb_torch.shape[0] == 1, "Batch size should be 1"
        assert text_emb_torch.shape[1] == 77, "Sequence length should be 77"
        assert text_emb_torch.shape[2] == 768, "Hidden dimension should be 768"


def test_unet_forward(sd14_model):
    """Test UNet denoising step"""
    batch_size = 1
    channels = 4
    height = 64  # 512/8 for latent space
    width = 64

    # Create dummy latent tensor
    latents = torch.randn(batch_size, channels, height, width)
    timestep = torch.tensor([50])

    # Create dummy text embeddings
    text_embeddings = torch.randn(batch_size, 77, 768)

    # Convert to TTNN tensors
    latents_ttnn = ttnn.from_torch(latents, device=sd14_model.device)
    timestep_ttnn = ttnn.from_torch(timestep, device=sd14_model.device)
    text_emb_ttnn = ttnn.from_torch(text_embeddings, device=sd14_model.device)

    # Forward pass through UNet
    with torch.no_grad():
        noise_pred = sd14_model.unet(latents_ttnn, timestep_ttnn, text_emb_ttnn)

    # Verify output
    assert noise_pred is not None, "UNet forward pass failed"

    noise_pred_torch = ttnn.to_torch(noise_pred)
    assert noise_pred_torch.shape == latents.shape, "UNet output shape mismatch"
    assert not torch.isnan(noise_pred_torch).any(), "UNet output contains NaN values"


def test_vae_decode(sd14_model):
    """Test VAE decoder output"""
    batch_size = 1
    channels = 4
    height = 64
    width = 64

    # Create dummy latent tensor
    latents = torch.randn(batch_size, channels, height, width)
    latents_ttnn = ttnn.from_torch(latents, device=sd14_model.device)

    # Decode latents to image
    with torch.no_grad():
        images = sd14_model.vae.decode(latents_ttnn)

    # Verify output
    assert images is not None, "VAE decode failed"

    images_torch = ttnn.to_torch(images)
    expected_shape = (batch_size, 3, 512, 512)  # RGB image at 512x512
    assert images_torch.shape == expected_shape, f"VAE output shape {images_torch.shape} != {expected_shape}"
    assert not torch.isnan(images_torch).any(), "VAE output contains NaN values"


def test_end_to_end_generation(sd14_model):
    """Test full pipeline with simple prompt"""
    prompt = "a simple red circle"
    num_inference_steps = 20
    guidance_scale = 7.5

    # Generate image
    try:
        with torch.no_grad():
            image = sd14_model.model.generate(
                prompt=prompt,
                height=512,
                width=512,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                device=sd14_model.device
            )

        assert image is not None, "Image generation returned None"

        # Convert to numpy for validation
        if hasattr(image, 'cpu'):
            image_np = image.cpu().numpy()
        else:
            image_np = ttnn.to_torch(image).cpu().numpy()

        assert image_np.shape[-2:] == (512, 512), "Generated image size incorrect"
        assert image_np.dtype in [np.float32, np.float64, np.uint8], "Invalid image data type"

    except Exception as e:
        pytest.fail(f"End-to-end generation failed: {e}")


def test_output_shape_validation(sd14_model):
    """Verify 512x512 output dimensions for various prompts"""
    test_prompts = [
        "landscape photo",
        "portrait of a person",
        "abstract geometric shapes"
    ]

    for prompt in test_prompts:
        with torch.no_grad():
            try:
                image = sd14_model.model.generate(
                    prompt=prompt,
                    height=512,
                    width=512,
                    num_inference_steps=10,  # Fewer steps for faster testing
                    device=sd14_model.device
                )

                if hasattr(image, 'shape'):
                    height, width = image.shape[-2:]
                else:
                    image_torch = ttnn.to_torch(image)
                    height, width = image_torch.shape[-2:]

                assert height == 512, f"Output height {height} != 512 for prompt '{prompt}'"
                assert width == 512, f"Output width {width} != 512 for prompt '{prompt}'"

            except Exception as e:
                pytest.fail(f"Shape validation failed for prompt '{prompt}': {e}")


def test_device_compatibility(sd14_model):
    """Test model works on available devices"""
    # Test that the model is properly loaded on the device
    assert sd14_model.device is not None, "No device available"

    # Test basic tensor operations on device
    test_tensor = torch.randn(2, 3, 4, 4)
    device_tensor = ttnn.from_torch(test_tensor, device=sd14_model.device)

    assert device_tensor is not None, "Failed to create tensor on device"

    # Test tensor can be moved back to CPU
    cpu_tensor = ttnn.to_torch(device_tensor)
    assert torch.allclose(test_tensor, cpu_tensor, atol=1e-5), "Device tensor transfer failed"

    # Test that model components are on the correct device
    # This would need to be adapted based on how device checking works in TTNN
    try:
        sample_input = ttnn.from_torch(torch.randn(1, 4, 64, 64), device=sd14_model.device)
        timestep = ttnn.from_torch(torch.tensor([10]), device=sd14_model.device)
        text_emb = ttnn.from_torch(torch.randn(1, 77, 768), device=sd14_model.device)

        # Quick forward pass to ensure device compatibility
        with torch.no_grad():
            output = sd14_model.unet(sample_input, timestep, text_emb)

        assert output is not None, "Device compatibility test failed"

    except Exception as e:
        pytest.fail(f"Device compatibility test failed: {e}")


@pytest.mark.slow
def test_multiple_generation_consistency():
    """Test that multiple generations work consistently"""
    test_harness = StableDiffusion14Test()

    if not test_harness.setup_model():
        pytest.skip("Could not initialize model for consistency test")

    try:
        prompt = "a blue flower"
        images = []

        for i in range(3):
            with torch.no_grad():
                image = test_harness.model.generate(
                    prompt=prompt,
                    height=512,
                    width=512,
                    num_inference_steps=15,
                    device=test_harness.device
                )
            images.append(image)

        # Verify all images have correct shape
        for i, img in enumerate(images):
            if hasattr(img, 'shape'):
                shape = img.shape[-2:]
            else:
                shape = ttnn.to_torch(img).shape[-2:]

            assert shape == (512, 512), f"Image {i} has incorrect shape: {shape}"

    finally:
        test_harness.cleanup()


def test_memory_cleanup(sd14_model):
    """Test that memory is properly managed during generation"""
    prompt = "memory test image"

    # Generate multiple images to test memory handling
    for i in range(5):
        with torch.no_grad():
            image = sd14_model.model.generate(
                prompt=f"{prompt} {i}",
                height=512,
                width=512,
                num_inference_steps=10,
                device=sd14_model.device
            )

        assert image is not None, f"Generation {i} failed"

        # Force cleanup (if supported by TTNN)
        del image
