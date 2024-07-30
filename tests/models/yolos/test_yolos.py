import torch
import pytest
from PIL import Image
import requests

# Load model directly
from transformers import AutoImageProcessor, AutoModelForObjectDetection


@pytest.mark.xfail
def test_yolos(record_property):
    record_property("model_name", "YOLOS")

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

    # Run inference with the original model
    with torch.no_grad():
        outputs = m(**inputs)

    # Helper function to decode output to human-readable text
    def decode_output(outputs):
        target_sizes = torch.tensor([image.size[::-1]])
        results = image_processor.post_process_object_detection(
            outputs, threshold=0.9, target_sizes=target_sizes
        )[0]
        return results

    decoded_output = decode_output(outputs)

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

    print(
        f"""
    model_name: {model_name}
    input_url: {test_input}
    answer before: {interpret_results(decoded_output)}
    """
    )

    record_property("torch_ttnn", (m, inputs, outputs))
