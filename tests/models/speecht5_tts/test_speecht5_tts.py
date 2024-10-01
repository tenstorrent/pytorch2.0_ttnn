# Reference: https://huggingface.co/microsoft/speecht5_tts

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import pytest
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
        model = model.to(torch.bfloat16)
        return model

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

    def run_model(self, model, inputs):
        speech = model.generate_speech(**inputs)
        return speech

    def set_inputs_train(self, inputs):
        inputs["speaker_embeddings"] = inputs["speaker_embeddings"].requires_grad_(True)
        return inputs

    def get_results_train(self, model, inputs, outputs):
        return inputs["speaker_embeddings"].grad


@pytest.mark.parametrize(
    "mode",
    ["train", "eval"],
)
@pytest.mark.compilation_xfail
def test_speecht5_tts(record_property, mode):
    model_name = "speecht5-tts"
    record_property("model_name", f"{model_name} {mode}")

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    # if mode == "eval":
    #     # Uncomment below if you really want to hear the result.
    #     # import soundfile as sf
    #     sf.write("speech.wav", speech.numpy(), samplerate=16000)

    record_property("torch_ttnn", (tester, results))
