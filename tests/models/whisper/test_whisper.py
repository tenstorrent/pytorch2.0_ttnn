# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from transformers import WhisperProcessor, WhisperForConditionalGeneration, AutoFeatureExtractor
from datasets import load_dataset
import pytest
from tests.utils import ModelTester, repeat_inputs
import torch


# Model ID matching tt-metal demo for Whisper distil-large-v3
MODEL_ID = "distil-whisper/distil-large-v3"


class WhisperEncoderTester(ModelTester):
    """
    Test only the encoder portion of Whisper for compilation.
    The encoder is a standard transformer that compiles well.
    """

    def _load_model(self):
        # Load the distil-large-v3 model to match tt-metal demo
        model = WhisperForConditionalGeneration.from_pretrained(
            MODEL_ID, torch_dtype=torch.bfloat16
        )
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_ID)
        # Return just the encoder for compilation testing
        return model.model.encoder

    def _load_inputs(self, batch_size):
        # Load dummy dataset and read audio files
        ds = load_dataset(
            "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
        )
        sample = ds[0]["audio"]
        input_features = self.feature_extractor(
            sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt"
        ).input_features
        input_features = repeat_inputs(input_features, batch_size)
        return input_features.to(torch.bfloat16)

    def run_model(self, model, input_features):
        # Run encoder only
        encoder_output = model(input_features)
        return encoder_output.last_hidden_state


class WhisperDecoderTester(ModelTester):
    """
    Test the decoder portion of Whisper for compilation.
    """

    def _load_model(self):
        # Load the distil-large-v3 model to match tt-metal demo
        model = WhisperForConditionalGeneration.from_pretrained(
            MODEL_ID, torch_dtype=torch.bfloat16
        )
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_ID)
        self.full_model = model
        # Return just the decoder for compilation testing
        return model.model.decoder

    def _load_inputs(self, batch_size):
        # Load dummy dataset and read audio files
        ds = load_dataset(
            "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
        )
        sample = ds[0]["audio"]
        input_features = self.feature_extractor(
            sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt"
        ).input_features
        input_features = repeat_inputs(input_features, batch_size)
        input_features = input_features.to(torch.bfloat16)

        # Pre-compute encoder outputs
        with torch.no_grad():
            self.encoder_outputs = self.full_model.model.encoder(input_features)

        # Create decoder input (start token)
        decoder_input_ids = torch.tensor([[50258]] * batch_size, dtype=torch.long)  # Start of transcript token
        return {"input_ids": decoder_input_ids, "encoder_hidden_states": self.encoder_outputs.last_hidden_state}

    def run_model(self, model, inputs):
        # Run decoder with encoder outputs
        decoder_output = model(
            input_ids=inputs["input_ids"],
            encoder_hidden_states=inputs["encoder_hidden_states"],
        )
        return decoder_output.last_hidden_state


class WhisperFullModelTester(ModelTester):
    """
    Test the full Whisper model (encoder + decoder) without generation loop.
    """

    def _load_model(self):
        # Load the distil-large-v3 model to match tt-metal demo
        self.processor = WhisperProcessor.from_pretrained(MODEL_ID)
        model = WhisperForConditionalGeneration.from_pretrained(
            MODEL_ID, torch_dtype=torch.bfloat16
        )
        model.config.forced_decoder_ids = None
        # Return the model's forward pass (not generate)
        return model

    def _load_inputs(self, batch_size):
        # Load dummy dataset and read audio files
        ds = load_dataset(
            "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
        )
        sample = ds[0]["audio"]
        input_features = self.processor(
            sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt"
        ).input_features
        input_features = repeat_inputs(input_features, batch_size)

        # Create decoder input (start token)
        decoder_input_ids = torch.tensor([[50258]] * batch_size, dtype=torch.long)

        return {
            "input_features": input_features.to(torch.bfloat16),
            "decoder_input_ids": decoder_input_ids,
        }

    def run_model(self, model, inputs):
        # Run full model forward pass
        outputs = model(**inputs)
        return outputs.logits


# Legacy tester using whisper-small for backward compatibility
class ThisTester(ModelTester):
    def _load_model(self):
        # load model and processor
        self.processor = WhisperProcessor.from_pretrained(
            "openai/whisper-small", torch_dtype=torch.bfloat16
        )
        model = WhisperForConditionalGeneration.from_pretrained(
            "openai/whisper-small", torch_dtype=torch.bfloat16
        )
        model.config.forced_decoder_ids = None
        return model.generate

    def _load_inputs(self, batch_size):
        # load dummy dataset and read audio files
        ds = load_dataset(
            "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
        )
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
        transcription = self.processor.batch_decode(
            predicted_ids, skip_special_tokens=True
        )
        return transcription

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_whisper_encoder(record_property, mode):
    """Test Whisper encoder (distil-large-v3) compilation."""
    model_name = "Whisper-Encoder"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = WhisperEncoderTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_whisper_decoder(record_property, mode):
    """Test Whisper decoder (distil-large-v3) compilation."""
    model_name = "Whisper-Decoder"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = WhisperDecoderTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_whisper_full_model(record_property, mode):
    """Test Whisper full model (distil-large-v3) forward pass compilation."""
    model_name = "Whisper"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = WhisperFullModelTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.compilation_xfail
def test_whisper(record_property, mode):
    """Legacy test using whisper-small with generate()."""
    model_name = "Whisper"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()

    record_property("torch_ttnn", (tester, results))
