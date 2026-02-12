# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from transformers import WhisperProcessor, WhisperForConditionalGeneration, AutoModelForSpeechSeq2Seq, AutoProcessor
from datasets import load_dataset
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch
import time


class ThisTester(ModelTester):
    def __init__(self, model_name, mode, batch_size=1, model_variant="openai/whisper-small"):
        self.model_variant = model_variant
        super().__init__(model_name, mode, batch_size)

    def _load_model(self):
        # load model and processor based on model variant
        if self.model_variant == "distil-large-v3":
            # Use distil-whisper/distil-large-v3 model
            model_id = "distil-whisper/distil-large-v3"
            self.processor = AutoProcessor.from_pretrained(model_id, torch_dtype=torch.bfloat16)
            model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_id, 
                torch_dtype=torch.bfloat16,
                low_cpu_mem_usage=True,
                use_safetensors=True
            )
        else:
            # Default to whisper-small for backward compatibility
            self.processor = WhisperProcessor.from_pretrained("openai/whisper-small", torch_dtype=torch.bfloat16)
            model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small", torch_dtype=torch.bfloat16)
        
        model.config.forced_decoder_ids = None
        return model.generate

    def _load_inputs(self, batch_size):
        # load dummy dataset and read audio files
        ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        sample = ds[0]["audio"]
        
        # For distil-large-v3, we need to ensure correct sampling rate (16000)
        if self.model_variant == "distil-large-v3":
            input_features = self.processor(
                sample["array"], 
                sampling_rate=16000,  # distil-large-v3 expects 16kHz
                return_tensors="pt"
            ).input_features
        else:
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
@pytest.mark.compilation_xfail
def test_whisper(record_property, mode):
    """Original whisper-small test for backward compatibility."""
    model_name = "Whisper"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_whisper_distil_large_v3(record_property, mode):
    """Test for distil-whisper/distil-large-v3 model support.
    
    This test validates the distil-large-v3 variant of Whisper as specified in:
    https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1044
    
    Target performance metrics (from tt-metal v0.58.0-rc22):
    - Hardware: n150
    - Batch: 1
    - ttft (time to first token): 244 ms
    - t/s/u (tokens per second per user): 54.7
    - Target t/s/u: 45
    - t/s (total tokens per second): 54.7
    
    Implementation based on tt-metal whisper demo:
    https://github.com/tenstorrent/tt-metal/tree/main/models/demos/whisper
    """
    model_name = "Whisper-distil-large-v3"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode, model_variant="distil-large-v3")
    
    # Measure baseline performance
    start_time = time.perf_counter()
    results = tester.test_model()
    end_time = time.perf_counter()
    
    # Calculate metrics
    elapsed_time_ms = (end_time - start_time) * 1000
    
    # Log performance metrics
    print(f"\n{'='*60}")
    print(f"Whisper distil-large-v3 Performance Metrics:")
    print(f"{'='*60}")
    print(f"Model: distil-whisper/distil-large-v3")
    print(f"Batch size: 1")
    print(f"Total time: {elapsed_time_ms:.2f} ms")
    print(f"\nTarget Metrics (from tt-metal v0.58.0-rc22):")
    print(f"  Hardware: n150")
    print(f"  ttft: 244 ms")
    print(f"  t/s/u: 54.7")
    print(f"  Target t/s/u: 45")
    print(f"{'='*60}\n")

    record_property("torch_ttnn", (tester, results))
    record_property("perf_elapsed_time_ms", elapsed_time_ms)
