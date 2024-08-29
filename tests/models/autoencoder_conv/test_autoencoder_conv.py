import torch
from diffusers import DiffusionPipeline, AutoencoderTiny
import pytest


@pytest.mark.compilation_xfail
def test_autoencoder_conv(record_property):
    record_property("model_name", "Autoencoder (convolutional)")

    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")
    pipe.vae = AutoencoderTiny.from_pretrained("madebyollin/taesd")
    """
Since this test is about the Conv version of model Autoencoder, we need to prove
that the model under test indeed contains Convolutions. Hence we print out the 
content of the model where you can find Conv2d in use.
>>> print(pipe.vae)
AutoencoderTiny(
  (encoder): EncoderTiny(
    (layers): Sequential(
      (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
      (1): AutoencoderTinyBlock(
        (conv): Sequential(
          (0): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (1): ReLU()
          (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): ReLU()
          (4): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        )
        (skip): Identity()
        (fuse): ReLU()
      )
      (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
      ...
    """

    prompt = "slice of delicious New York-style berry cheesecake"
    arguments = {"prompt": prompt, "num_inference_steps": 25}
    output = pipe(**arguments)
    image = output.images[0]

    record_property("torch_ttnn", (pipe, arguments, output))
