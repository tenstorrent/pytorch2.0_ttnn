# Reference: https://huggingface.co/microsoft/speecht5_tts

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import pytest


@pytest.mark.compilation_xfail
def test_speecht5_tts(record_property):
    record_property("model_name", "speecht5-tts")

    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

    inputs = processor(text="Hello, my dog is cute.", return_tensors="pt")

    # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    arguments = {"input_ids": inputs["input_ids"], "speaker_embeddings": speaker_embeddings, "vocoder": vocoder}
    speech = model.generate_speech(**arguments)

    # Uncomment below if you really want to hear the result.
    # import soundfile as sf
    # sf.write("speech.wav", speech.numpy(), samplerate=16000)

    record_property("torch_ttnn", (model.generate_speech, arguments, speech))
