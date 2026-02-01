# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from transformers import AutoProcessor, WhisperForConditionalGeneration
from tests.utils import ModelTester, repeat_inputs

class WhisperDistilTester(ModelTester):
    def _load_model(self):
        model_name = "distil-whisper/distil-large-v3"
        self.processor = AutoProcessor.from_pretrained(model_name)
        m = WhisperForConditionalGeneration.from_pretrained(model_name, torch_dtype=torch.float16)
        m.eval()
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        # 1 second of silence at 16kHz
        sampling_rate = 16000
        dummy_audio = torch.zeros(sampling_rate)
        inputs = self.processor(dummy_audio, sampling_rate=sampling_rate, return_tensors="pt")
        inputs = {k: repeat_inputs(v, batch_size) for k, v in inputs.items()}
        return inputs

@pytest.mark.parametrize("mode", ["eval"])
def test_whisper_distil(record_property, mode):
    model_name = "Whisper-Distil-Large-V3"
    record_property("model_name", model_name)
    tester = WhisperDistilTester(model_name, mode)
    results = tester.test_model()
    record_property("torch_ttnn", (tester, results))
