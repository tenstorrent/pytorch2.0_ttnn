import torch
import torch_ttnn
import unittest
import ttnn
from torch_ttnn.utils import RunTimeMetrics

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


class TestBert(unittest.TestCase):
    def setUp(self):
        # Open device 0
        self.device: ttnn.Device = ttnn.open_device(device_id=0)

    def tearDown(self):
        # Close the device
        ttnn.close_device(self.device)

    def test_bert(self):
        # Download model from cloud
        model_name = "phiyodr/bert-large-finetuned-squad2"
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, padding_side="left", torch_dtype=torch.bfloat16
        )
        m = AutoModelForQuestionAnswering.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        )
        m.eval()

        # Set up sample input
        context = 'Johann Joachim Winckelmann was a German art historian and archaeologist. He was a pioneering Hellenist who first articulated the difference between Greek, Greco-Roman and Roman art. "The prophet and founding hero of modern archaeology", Winckelmann was one of the founders of scientific archaeology and first applied the categories of style on a large, systematic basis to the history of art. '
        question = "What discipline did Winkelmann create?"

        inputs = tokenizer.encode_plus(
            question,
            context,
            add_special_tokens=True,
            return_tensors="pt",
            max_length=256,
            padding="max_length",
            truncation=True,
        )

        metrics_path = "BERT"
        # Run inference with the original model
        with torch.no_grad():
            outputs_before = RunTimeMetrics(
                metrics_path, "original", lambda: m(**inputs)
            )

        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            response_start = torch.argmax(outputs.start_logits)
            response_end = torch.argmax(outputs.end_logits) + 1
            response_tokens = inputs.input_ids[0, response_start:response_end]
            return tokenizer.decode(response_tokens)

        answer_before = decode_output(outputs_before)

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
        option._out_fx_graphs[0].print_tabular()

        answer_after = decode_output(outputs_after)

        print(
            f"""
        model_name: {model_name}
        input:
            context: {context}
            question: {question}
        answer before: {answer_before}
        answer after: {answer_after}
        """
        )

        # TODO: Add more checks for the compiled graph

        # Check inference result
        self.assertEqual(answer_before, answer_after)
