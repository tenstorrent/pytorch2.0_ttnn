import torch
import torch_ttnn
import unittest
import ttnn
from torch_ttnn.metrics import RunTimeMetrics
from PIL import Image
import requests

# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection


class TestYolos(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_yolos(self):
        # Download model from cloud
        model_name = "hustvl/yolos-tiny"
        image_processor = AutoImageProcessor.from_pretrained(
            model_name,
        )
        m = AutoModelForObjectDetection.from_pretrained(
            model_name,
        )
        m.eval()

        # Set up sample input
        test_input = "http://images.cocodataset.org/val2017/000000039769.jpg"
        image = Image.open(requests.get(test_input, stream=True).raw)
        inputs = image_processor(images=image, return_tensors="pt")

        metrics_path = "YOLOS"
        # Run inference with the original model
        with torch.no_grad():
            outputs_before = RunTimeMetrics(
                metrics_path, "original", lambda: m(**inputs)
            )

        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            target_sizes = torch.tensor([image.size[::-1]])
            results = image_processor.post_process_object_detection(
                outputs, threshold=0.9, target_sizes=target_sizes
            )[0]
            return results

        decoded_output_before = decode_output(outputs_before)

        # Compile model with ttnn backend
        option = torch_ttnn.TorchTtnnOption(
            device=self.device, metrics_path=metrics_path
        )
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)

        # Run inference with the compiled model
        with torch.no_grad():
            outputs_after = RunTimeMetrics(
                metrics_path, "compiled", lambda: m(**inputs)
            )

        def interpret_results(decoded_output):
            for score, label, box in zip(
                decoded_output["scores"],
                decoded_output["labels"],
                decoded_output["boxes"],
            ):
                box = [round(i, 2) for i in box.tolist()]
                string = (
                    f"Detected {m.config.id2label[label.item()]} with confidence "
                    f"{round(score.item(), 3)} at location {box}"
                )
                return string

        if outputs_after:
            option._out_fx_graphs[0].print_tabular()

            decoded_output_after = decode_output(outputs_after)

            print(
                f"""
            model_name: {model_name}
            input_url: {test_input}
            answer before: {interpret_results(decoded_output_before)}
            answer after: {interpret_results(decoded_output_after)}
            """
            )

            # TODO: Add more checks for the compiled graph

            # TODO: Check inference result
        else:
            print(f"Compiled model: {model_name} failed to run.")
