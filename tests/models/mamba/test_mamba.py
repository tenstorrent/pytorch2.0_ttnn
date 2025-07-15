# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

import pytest
import torch
from transformers import AutoTokenizer

from tests.models.mamba.mamba_ssm.model import Mamba
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
        model = Mamba.from_pretrained("state-spaces/mamba-2.8b-slimpj")
        model = model.to(torch.bfloat16)
        return model

    def _load_inputs(self, batch_size):
        prompt = "Climate change refers to long-term shifts in temperatures and weather patterns. Such shifts can be natural due to changes in the sun's activity or volcanic eruptions."
        input_ids = self.tokenizer(prompt, return_tensors="pt")["input_ids"]
        return input_ids


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_mamba(record_property, mode):
    model_name = "Mamba"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
