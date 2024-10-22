# Reference: https://github.com/arief25ramadhan/carvana-unet-segmentation

import os
import subprocess
import sys
from pathlib import Path
import tempfile
import torch
import pytest

from tests.models.unet_carvana.carvana_unet_segmentation.model import UNET
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        model = UNET(in_channels=3, out_channels=1)
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self):
        input_batch = torch.rand((1, 3, 224, 224))
        input_batch = input_batch.to(torch.bfloat16)
        return input_batch


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
def test_unet_carvana(record_property, mode):
    model_name = "Unet-carvana"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
