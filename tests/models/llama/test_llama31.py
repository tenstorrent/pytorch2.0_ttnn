# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
import pytest
import time

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from tests.utils import ModelTester, repeat_inputs


class Llama31Tester(ModelTester):
    """Tester for Llama 3.1 model family.
    
    Supports three model variants:
    - 1B: meta-llama/Llama-3.2-1B
    - 3B: meta-llama/Llama-3.2-3B  
    - 8B: meta-llama/Llama-3.1-8B
    """
    
    MODEL_VARIANTS = {
        "1B": "meta-llama/Llama-3.2-1B",
        "3B": "meta-llama/Llama-3.2-3B",
        "8B": "meta-llama/Llama-3.1-8B",
    }
    
    def __init__(self, model_name, mode, batch_size=1, model_variant="8B"):
        self.model_variant = model_variant
        self.model_id = self.MODEL_VARIANTS.get(model_variant, model_variant)
        super().__init__(model_name, mode, batch_size)

    def _load_model(self):
        # Download model from HuggingFace
        model_name = self.model_id
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, 
            padding_side="left", 
            torch_dtype=torch.bfloat16
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        m = AutoModelForCausalLM.from_pretrained(
            model_name, 
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
        )
        
        for param in m.parameters():
            param.requires_grad = False
        return m

    def _load_inputs(self, batch_size):
        # Set up sample input
        self.test_input = "This is a sample text from "
        inputs = self.tokenizer.encode_plus(
            self.test_input,
            return_tensors="pt",
            max_length=32,
            padding="max_length",
            add_special_tokens=True,
            truncation=True,
        )
        inputs = repeat_inputs(inputs, batch_size)
        return inputs


def run_llama_test(record_property, mode, model_variant, batch_size=32):
    """Run Llama model test with specified variant.
    
    Target performance metrics from tt-metal (n150 hardware):
    - 1B: ttft=23ms, t/s/u=67.6, target=160
    - 3B: ttft=53ms, t/s/u=43.5, target=60
    - 8B: ttft=104ms, t/s/u=24.6, target=23
    """
    model_name = f"Llama-3.1-{model_variant}"
    record_property("model_name", model_name)
    record_property("mode", mode)
    record_property("batch_size", batch_size)

    tester = Llama31Tester(model_name, mode, batch_size=batch_size, model_variant=model_variant)
    
    # Measure performance
    start_time = time.perf_counter()
    results = tester.test_model()
    end_time = time.perf_counter()
    
    # Calculate metrics
    elapsed_time_ms = (end_time - start_time) * 1000
    
    # Log performance metrics
    target_metrics = {
        "1B": {"ttft_ms": 23, "t_s_u": 67.6, "target_t_s_u": 160},
        "3B": {"ttft_ms": 53, "t_s_u": 43.5, "target_t_s_u": 60},
        "8B": {"ttft_ms": 104, "t_s/u": 24.6, "target_t_s_u": 23},
    }
    
    metrics = target_metrics.get(model_variant, {})
    
    print(f"\n{'='*60}")
    print(f"Llama {model_variant} Performance Metrics:")
    print(f"{'='*60}")
    print(f"Model: {tester.model_id}")
    print(f"Batch size: {batch_size}")
    print(f"Total time: {elapsed_time_ms:.2f} ms")
    if metrics:
        print(f"\nTarget Metrics (from tt-metal):")
        print(f"  Hardware: n150")
        for key, value in metrics.items():
            print(f"  {key}: {value}")
    print(f"{'='*60}\n")

    if mode == "eval":
        # Helper function to decode output to human-readable text
        def decode_output(outputs):
            next_token_logits = outputs.logits[:, -1]
            next_token = next_token_logits.softmax(dim=-1).argmax()
            return tester.tokenizer.decode([next_token])

        decoded_output = decode_output(results)

        print(
            f"""
        model_name: {model_name}
        input: {tester.test_input}
        output before: {decoded_output}
        """
        )

    record_property("torch_ttnn", (tester, results))
    record_property("perf_elapsed_time_ms", elapsed_time_ms)
    
    return tester, results


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_llama31_1b(record_property, mode):
    """Test Llama 3.2 1B model.
    
    This test validates the Llama 3.2 1B variant as specified in:
    https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1047
    
    Target performance metrics (from tt-metal v0.57.0-rc23):
    - Hardware: n150
    - Batch: 32
    - ttft (time to first token): 23 ms
    - t/s/u (tokens per second per user): 67.6
    - Target t/s/u: 160
    - t/s (total tokens per second): 2163.2
    """
    run_llama_test(record_property, mode, "1B", batch_size=32)


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_llama31_3b(record_property, mode):
    """Test Llama 3.2 3B model.
    
    This test validates the Llama 3.2 3B variant as specified in:
    https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1047
    
    Target performance metrics (from tt-metal v0.57.0-rc71):
    - Hardware: n150
    - Batch: 32
    - ttft (time to first token): 53 ms
    - t/s/u (tokens per second per user): 43.5
    - Target t/s/u: 60
    - t/s (total tokens per second): 1392.0
    """
    run_llama_test(record_property, mode, "3B", batch_size=32)


@pytest.mark.parametrize(
    "mode",
    ["eval"],
)
@pytest.mark.converted_end_to_end
def test_llama31_8b(record_property, mode):
    """Test Llama 3.1 8B model.
    
    This test validates the Llama 3.1 8B variant as specified in:
    https://github.com/tenstorrent/pytorch2.0_ttnn/issues/1047
    
    Target performance metrics (from tt-metal v0.57.0-rc71):
    - Hardware: n150
    - Batch: 32
    - ttft (time to first token): 104 ms
    - t/s/u (tokens per second per user): 24.6
    - Target t/s/u: 23
    - t/s (total tokens per second): 787.2
    """
    run_llama_test(record_property, mode, "8B", batch_size=32)
