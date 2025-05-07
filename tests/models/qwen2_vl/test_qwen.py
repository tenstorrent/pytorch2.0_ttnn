import torch
import pytest
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from PIL import Image
import requests
from torchvision import io
from typing import Dict
from tests.utils import ModelTester


class ThisTester(ModelTester):
    def _load_model(self):
        model_name = "Qwen/Qwen2-VL-2B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, padding_side="left", torch_dtype=torch.bfloat16
        )
        model = Qwen2VLForConditionalGeneration.from_pretrained(
            "Qwen/Qwen2-VL-2B-Instruct", torch_dtype=torch.bfloat16
        )
        self.processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

        return model.generate

    def _load_inputs(self):
        # Image
        url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
        image = Image.open(requests.get(url, stream=True).raw)
        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ]
        text_prompt = self.processor.apply_chat_template(conversation, add_generation_prompt=True)
        inputs = self.processor(
            text=[text_prompt], images=[image], padding=True, return_tensors="pt"
        )

        arguments = inputs.update({
            "do_sample": True,
            "temperature": 0.9,
            "max_new_tokens": 10,
        })
        return arguments

    def set_model_eval(self, model):
        return model


@pytest.mark.parametrize("mode", ["eval"])
@pytest.mark.skip(reason="This test requires transformers>=4.45.0")
def test_qwen(record_property, mode):
    model_name = "Qwen2-VL-2B"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        gen_text = tester.processor.batch_decode(results, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        print(f"Generated Text:\n{gen_text}")

    record_property("torch_ttnn", (tester, results))
