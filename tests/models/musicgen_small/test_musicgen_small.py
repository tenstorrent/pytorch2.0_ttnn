# Reference: https://huggingface.co/facebook/musicgen-small

from transformers import AutoProcessor, MusicgenForConditionalGeneration
import pytest


@pytest.mark.compilation_xfail
def test_musicgen_small(record_property):
    record_property("model_name", "musicgen_small")

    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    inputs = processor(
        text=["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"],
        padding=True,
        return_tensors="pt",
    )

    inputs["max_new_tokens"] = 256
    audio_values = model.generate(**inputs)

    record_property("torch_ttnn", (model.generate, inputs, audio_values))
