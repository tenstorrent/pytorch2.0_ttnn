# Reference: https://github.com/tenstorrent/tt-buda-demos/blob/main/model_demos/cv_demos/linear_autoencoder/pytorch_linear_autoencoder.py

import torch
import torchvision.transforms as transforms
from datasets import load_dataset
import pytest
from tests.utils import ModelTester


class LinearAE(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # Encoder
        self.encoder_lin1 = torch.nn.Linear(784, 128)
        self.encoder_lin2 = torch.nn.Linear(128, 64)
        self.encoder_lin3 = torch.nn.Linear(64, 12)
        self.encoder_lin4 = torch.nn.Linear(12, 3)

        # Decoder
        self.decoder_lin1 = torch.nn.Linear(3, 12)
        self.decoder_lin2 = torch.nn.Linear(12, 64)
        self.decoder_lin3 = torch.nn.Linear(64, 128)
        self.decoder_lin4 = torch.nn.Linear(128, 784)

        # Activation Function
        self.act_fun = torch.nn.ReLU()

    def forward(self, x):
        # Encode
        act = self.encoder_lin1(x)
        act = self.act_fun(act)
        act = self.encoder_lin2(act)
        act = self.act_fun(act)
        act = self.encoder_lin3(act)
        act = self.act_fun(act)
        act = self.encoder_lin4(act)

        # Decode
        act = self.decoder_lin1(act)
        act = self.act_fun(act)
        act = self.decoder_lin2(act)
        act = self.act_fun(act)
        act = self.decoder_lin3(act)
        act = self.act_fun(act)
        act = self.decoder_lin4(act)

        return act


class ThisTester(ModelTester):
    def _load_model(self):
        # Instantiate model
        # NOTE: The model has not been pre-trained or fine-tuned.
        # This is for demonstration purposes only.
        model = LinearAE()
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
    ["train", "eval"],
)
@pytest.mark.compilation_xfail
def test_autoencoder_linear(record_property, mode):
    model_name = "Autoencoder (linear)"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    if mode == "eval":
        print("Output: ", results)

    record_property("torch_ttnn", (tester, results))
