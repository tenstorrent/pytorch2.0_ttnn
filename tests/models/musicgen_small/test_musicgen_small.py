# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Reference: https://huggingface.co/facebook/musicgen-small

from transformers import AutoProcessor, MusicgenForConditionalGeneration
import pytest
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
        model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
        return model.generate

    def _load_inputs(self, batch_size):
        inputs = self.processor(
            text=["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"],
            padding=True,
            return_tensors="pt",
        )

        inputs["max_new_tokens"] = 256
        inputs = repeat_inputs(inputs, batch_size)
        return inputs

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.skip("torch run with bypass compilation is stalling")
def test_musicgen_small(record_property, mode):
    model_name = "musicgen_small"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
