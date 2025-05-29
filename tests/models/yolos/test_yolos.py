# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
from PIL import Image
import requests

# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection
from tests.utils import ModelTester, repeat_inputs


class ThisTester(ModelTester):
    def _load_model(self):
        # Download model from cloud
        model_name = "hustvl/yolos-tiny"
        self.image_processor = AutoImageProcessor.from_pretrained(
            model_name,
        )
        m = AutoModelForObjectDetection.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        return m

    def _load_inputs(self, batch_size):
        # Set up sample input
        self.test_input = "http://images.cocodataset.org/val2017/000000039769.jpg"
        self.image = Image.open(requests.get(self.test_input, stream=True).raw)
        inputs = self.image_processor(images=self.image, return_tensors="pt")
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        inputs = repeat_inputs(inputs, batch_size)
        return inputs


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)

# @pytest.mark.xfail
def test_yolos(record_property, mode):
    model_name = "YOLOS"
    record_property("model_name", model_name)
    record_property("mode", mode)

    tester = ThisTester(model_name, mode)
    results = tester.test_model()
    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            target_sizes = torch.tensor([tester.image.size[::-1]])
            results = tester.image_processor.post_process_object_detection(
                outputs, threshold=0.9, target_sizes=target_sizes
            )[0]
            return results

        decoded_output = decode_output(results)

        def interpret_results(decoded_output):
            for score, label, box in zip(
                decoded_output["scores"],
                decoded_output["labels"],
                decoded_output["boxes"],
            ):
                box = [round(i, 2) for i in box.tolist()]
                string = (
                    f"Detected {tester.model.config.id2label[label.item()]} with confidence "
                    f"{round(score.item(), 3)} at location {box}"
                )
                return string

        print(
            f"""
        model_name: {model_name}
        input_url: {tester.test_input}
        answer before: {interpret_results(decoded_output)}
        """
        )

    record_property("torch_ttnn", (tester, results))
