# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/linear_autoencoder/pytorch_linear_autoencoder.py

import torch
import torchvision.transforms as transforms
from datasets import load_dataset
import pytest
from tests.utils import ModelTester


class SimpleLinear(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # Encoder
        self.encoder_lin1 = torch.nn.Linear(784, 128)
        self.encoder_lin2 = torch.nn.Linear(128, 128)

        # Activation Function
        self.act_fun = torch.nn.ReLU()

        self.switch = torch.randn((1, 1))

    def forward(self, x):
        # Encode
        act = self.encoder_lin1(x)
        print("graph break")
        if self.switch > 0.5:
            return act + 2
        else:
            act = self.encoder_lin2(act) + 3
            return self.act_fun(act)


class ThisTester(ModelTester):
    def _load_model(self):
        # Instantiate model
        # NOTE: The model has not been pre-trained or fine-tuned.
        # This is for demonstration purposes only.
        model = SimpleLinear()
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        # Define transform to normalize data
        transform = transforms.Compose(
            [
                transforms.Resize((1, 784)),
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,)),
            ]
        )

        # Load sample from MNIST dataset
        dataset = load_dataset("mnist")
        sample = dataset["train"][0]["image"]
        sample_tensor = [transform(sample).squeeze(0)]
        batch_tensor = torch.cat(sample_tensor, dim=0)
        batch_tensor = batch_tensor.to(torch.bfloat16)
        return batch_tensor


@pytest.mark.parametrize(
    "mode",
    [pytest.param("eval", marks=pytest.mark.converted_end_to_end)],
)
def test_autoencoder_linear(record_property, mode):
    model_name = "Simple Linear"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        print("Output: ", results)

    record_property("torch_ttnn", (tester, results))
