# Reference: https://github.com/arief25ramadhan/carvana-unet-segmentation

import os
import subprocess
import sys
from pathlib import Path
import tempfile
import torch
import pytest

from tests.models.unet_carvana.carvana_unet_segmentation.model import UNET


@pytest.mark.compilation_xfail
def test_unet_carvana(record_property):
    record_property("model_name", "Unet-carvana")

    model = UNET(in_channels=3, out_channels=1)

    input_batch = torch.rand((1, 3, 224, 224))
    output = model(input_batch)

    record_property("torch_ttnn", (model, input_batch, output))
