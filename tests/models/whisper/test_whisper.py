# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch


class ThisTester(ModelTester):
    def _load_model(self):
        # load model and processor
        # Using distil-whisper/distil-large-v3 as per issue #1044 requirements
        # This matches the version used in tt-metal demo
        self.processor = WhisperProcessor.from_pretrained("distil-whisper/distil-large-v3", torch_dtype=torch.bfloat16)
        model = WhisperForConditionalGeneration.from_pretrained("distil-whisper/distil-large-v3", torch_dtype=torch.bfloat16)
        model.config.forced_decoder_ids = None
        return model.generate

    def _load_inputs(self, batch_size):
        # load dummy dataset and read audio files
        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        sample = ds[0]["audio"]
        input_features = self.processor(
            sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt"
        ).input_features
        input_features = repeat_inputs(input_features, batch_size)
        return input_features.to(torch.bfloat16)

    def run_model(self, model, input_features):
        # generate token ids
        predicted_ids = model(input_features)
        # decode token ids to text
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail(reason="aten::clone() SymInt type casting issue - see to_tt_guard.py")
def test_whisper(record_property, mode):
    model_name = "Whisper"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
