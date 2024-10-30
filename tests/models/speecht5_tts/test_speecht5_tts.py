# Reference: https://huggingface.co/microsoft/speecht5_tts

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts", torch_dtype=torch.bfloat16)
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan", torch_dtype=torch.bfloat16)
        return model.generate_speech

    def _load_inputs(self):
        inputs = self.processor(text="Hello, my dog is cute.", return_tensors="pt")
        # load xvector containing speaker's voice characteristics from a dataset
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0).to(torch.bfloat16)
        arguments = {
            "input_ids": inputs["input_ids"],
            "speaker_embeddings": speaker_embeddings,
            "vocoder": self.vocoder,
        }
        return arguments

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
def test_speecht5_tts(record_property, mode):
    model_name = "speecht5-tts"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    # if mode == "eval":
    #     # Uncomment below if you really want to hear the result.
    #     # import soundfile as sf
    #     sf.write("speech.wav", speech.numpy(), samplerate=16000)

    record_property("torch_ttnn", (tester, results))
