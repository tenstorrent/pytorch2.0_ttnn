# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import math
import torch
import numpy as np
import re
import requests
import ttnn
from os import path, makedirs
from collections.abc import Mapping, Sequence
from typing import List, Dict, Tuple, Union


class ModelTester:
    def __init__(self, model_name, mode, batch_size=1):
        if mode not in ["train", "eval"]:
            raise ValueError(f"Current mode is not supported: {mode}")
        self.model_name = model_name
        self.mode = mode
        self.model = self._load_model()
        self.batch_size = batch_size
        self.inputs = self._load_inputs(self.batch_size)

    def _load_model(self):
        raise NotImplementedError("This method should be implemented in the derived class")

    def _load_inputs(self, batch_size):
        raise NotImplementedError("This method should be implemented in the derived class")

    def set_model_train(self, model):
        model.train()
        model.zero_grad()

        # Eliminating randomness from Dropout to ensure consistent results.
        #
        # This is necessary for comparing the two training rounds:
        # one using PyTorch native code and the other using the PyTorch Dynamo TT backend.
        # Without this, the results would differ, making it impossible to compare the two implementations.
        for layer in model.modules():
            if isinstance(layer, torch.nn.Dropout):
                layer.p = 0  # Set dropout probability to 0
        return model

    def set_model_eval(self, model):
        model.eval()
        return model

    def set_inputs_train(self, inputs):
        if type(inputs) == torch.Tensor:
            # Setting input tensor's `requires_grad` attribute to true.
            #
            # This allows us to use the gradient of the input as the golden result for the training process.
            # For further details, refer to the file `conftest.py` regarding the rationale behind.
            inputs.requires_grad_(True)
        else:
            raise ValueError(f"set_inputs_train: Current inputs type is not supported: {type(inputs)}")
        return inputs

    def set_inputs_eval(self, inputs):
        return inputs

    def compile_model(self, model, option):
        import torch_ttnn

        # Compile model with ttnn backend
        model = torch.compile(model, backend=torch_ttnn.backend, options=option)
        return model

    def run_model(self, model, inputs):
        if isinstance(inputs, Mapping):
            return model(**inputs)
        elif isinstance(inputs, Sequence):
            return model(*inputs)
        else:
            return model(inputs)

    def append_fake_loss_function(self, outputs):
        # Using `torch.mean` as the loss function for testing purposes.
        #
        # Loss functions typically produce a scalar loss, and `torch.mean`
        # is one valid option in this category. While it may not be the best
        # choice for training effective models, it simplifies our testing process.
        #
        # Since our goal is to verify gradient computation rather than to
        # train a high-performing model, applying `torch.mean` uniformly
        # across all models under test eases the testing procedure.
        if str(type(outputs)) in ["<class 'torch.Tensor'>", "<class 'core.TorchTensor'>"]:
            return torch.mean(outputs)
        else:
            raise ValueError(f"append_fake_loss_function: Current outputs type is not supported: {type(outputs)}")

    def get_results_train(self, model, inputs, outputs):
        # Why `inputs.requires_grad`?
        #
        # Backward pass computes gradients for all trainable weight tensors.
        # However, verifying every gradient can be costly, especially for
        # large models with many parameters.
        #
        # Instead of checking each gradient, we check the gradient
        # of the "model input" tensor only. Computing the input gradient
        # serves as an indicator for the health of all other gradients.
        # Based on the "chain rule", the input gradient depends on all other
        # gradients, so any incorrect gradient computation should reflect here.
        if type(inputs) == torch.Tensor:
            results = inputs.grad
        elif type(inputs) == dict:
            results = {k: v.grad for k, v in inputs.items()}
        else:
            raise ValueError(f"get_results_train: Current inputs type is not supported: {type(inputs)}")
        return results

    def get_results_eval(self, model, inputs, outputs):
        return outputs

    def test_model_train(self, as_ttnn=False, option=None):
        # Fixing the random seed for reproducibility to ease debugging.
        #
        # Training processes involve more randomness compared to evaluation,
        # such as random initialization of weights.
        # Setting a fixed random seed is crucial for consistent testing
        # and debugging during the training process.
        torch.manual_seed(99)
        model = self.set_model_train(self.model)
        inputs = self.set_inputs_train(self.inputs)
        if as_ttnn == True:
            model = self.compile_model(model, option)
        outputs = self.run_model(model, inputs)
        loss = self.append_fake_loss_function(outputs)
        loss.backward()
        # Again, use the gradient of the input (`test_input.grad`) as the golden result for the training process.
        results = self.get_results_train(model, inputs, outputs)
        return results

    @torch.no_grad()
    def test_model_eval(self, as_ttnn=False, option=None):
        torch.manual_seed(0)
        model = self.set_model_eval(self.model)
        inputs = self.set_inputs_eval(self.inputs)
        if as_ttnn == True:
            model = self.compile_model(model, option)
        outputs = self.run_model(model, inputs)
        results = self.get_results_eval(model, inputs, outputs)
        return results

    def test_model(self, as_ttnn=False, option=None):
        if self.mode == "train":
            return self.test_model_train(as_ttnn, option)
        elif self.mode == "eval":
            return self.test_model_eval(as_ttnn, option)
        else:
            raise ValueError(f"Current mode is not supported: {self.mode}")


def repeat_inputs(inputs, batch_size):
    if batch_size is None:
        return None
    if hasattr(inputs, "keys"):
        for key in inputs.keys():
            if isinstance(inputs[key], torch.Tensor):
                repeat_size = [batch_size] + ([1] * (inputs[key].dim() - 1))
                inputs[key] = inputs[key].repeat(*repeat_size)
        return inputs
    elif isinstance(inputs, torch.Tensor):
        repeat_size = [batch_size] + ([1] * (inputs.dim() - 1))
        inputs = inputs.repeat(*repeat_size)
        return inputs
    else:
        raise TypeError(f"Inputs type not supported for batching: {type(inputs)}")


def get_absolute_cache_path(path_relative_to_cache):
    # convenience method to use NFS if available
    nfs_cache_base = "/mnt/tt-metal-pytorch-cache/.cache"
    if path.exists(nfs_cache_base):
        return path.join(nfs_cache_base, path_relative_to_cache)
    else:
        absolute_cache_base = path.expanduser("~/.cache")
        return path.join(absolute_cache_base, path_relative_to_cache)


def get_cached_image_or_reload(relative_cache_path, url):
    absolute_cache_path = get_absolute_cache_path(relative_cache_path)

    if path.exists(absolute_cache_path):
        return absolute_cache_path

    dir, _ = path.split(absolute_cache_path)
    makedirs(dir, exist_ok=True)

    image_file = requests.get(url, stream=True)
    with open(absolute_cache_path, "wb") as file:
        for chunk in image_file.iter_content(chunk_size=8192):
            file.write(chunk)

    return absolute_cache_path


# Testing utils copied from tt-metal/tests/ttnn/utils_for_testing.py and tt-metal/models/common/utility_functions.py
def comp_pcc(golden, calculated, pcc=0.99):
    golden = torch.Tensor(golden)
    calculated = torch.Tensor(calculated)

    if golden.dtype != calculated.dtype:
        calculated = calculated.type(golden.dtype)

    if torch.all(torch.isnan(golden)) and torch.all(torch.isnan(calculated)):
        # logger.warning("Both tensors are 'nan'")
        return True, 1.0

    if torch.all(torch.isnan(golden)) or torch.all(torch.isnan(calculated)):
        # logger.error("One tensor is all nan, the other is not.")
        return False, 0.0

    # Test if either is completely zero
    if torch.any(golden.bool()) != torch.any(calculated.bool()):
        # logger.error("One tensor is all zero")
        return False, 0.0

    # For now, mask all infs and nans so that we check the rest... TODO
    golden = golden.clone()
    golden[
        torch.logical_or(
            torch.isnan(golden),
            torch.logical_or(torch.isinf(golden), torch.isneginf(golden)),
        )
    ] = 0
    calculated = calculated.clone()
    calculated[
        torch.logical_or(
            torch.isnan(calculated),
            torch.logical_or(torch.isinf(calculated), torch.isneginf(calculated)),
        )
    ] = 0

    if torch.equal(golden, calculated):
        return True, 1.0

    if golden.dtype == torch.bfloat16:
        golden = golden.type(torch.float32)
        calculated = calculated.type(torch.float32)
    cal_pcc = np.min(
        np.ma.corrcoef(
            np.ma.masked_invalid(torch.squeeze(golden).detach().numpy()).flatten(),
            np.ma.masked_invalid(torch.squeeze(calculated).detach().numpy()).flatten(),
        )
    )

    if isinstance(cal_pcc, np.ma.core.MaskedConstant):
        return True, 1.0

    return cal_pcc >= pcc, cal_pcc


def construct_pcc_assert_message(message, expected_pytorch_result, actual_pytorch_result):
    messages = []
    messages.append(message)
    # messages.append("Expected")
    # messages.append(str(expected_pytorch_result))
    # messages.append("Actual")
    # messages.append(str(actual_pytorch_result))
    messages = [str(m) for m in messages]
    return "\n".join(messages)


def assert_with_pcc(expected_pytorch_result, actual_pytorch_result, pcc=0.999):
    assert list(expected_pytorch_result.shape) == list(
        actual_pytorch_result.shape
    ), f"list(expected_pytorch_result.shape)={list(expected_pytorch_result.shape)} vs list(actual_pytorch_result.shape)={list(actual_pytorch_result.shape)}"
    pcc_passed, pcc_message = comp_pcc(expected_pytorch_result, actual_pytorch_result, pcc)
    assert pcc_passed, construct_pcc_assert_message(pcc_message, expected_pytorch_result, actual_pytorch_result)
    return pcc_passed, pcc_message


def check_with_pcc(expected_pytorch_result, actual_pytorch_result, pcc=0.999):
    if expected_pytorch_result.shape != actual_pytorch_result.shape:
        return (
            False,
            f"list(expected_pytorch_result.shape)={list(expected_pytorch_result.shape)} vs list(actual_pytorch_result.shape)={list(actual_pytorch_result.shape)}",
        )
    pcc_passed, pcc_message = comp_pcc(expected_pytorch_result, actual_pytorch_result, pcc)
    return pcc_passed, construct_pcc_assert_message(pcc_message, expected_pytorch_result, actual_pytorch_result)


def _comp_nonfinite(golden, calculated):
    """
    Returns True if tensors contain the same non-finite values (nan, inf, -inf) at the same positions. Also returns True if all elements are finite.
    Returns False if non-finite values differ between both tensors.
    """

    # torch.equal(['nan'], ['nan']] => False
    # For this reason, we check for nan and inf separately
    if torch.not_equal(torch.isnan(golden), torch.isnan(calculated)).any():
        return False

    golden_inf_mask = torch.isinf(golden)
    calculated_inf_mask = torch.isinf(calculated)

    if torch.not_equal(golden_inf_mask, calculated_inf_mask).any():
        return False

    golden_inf = golden[golden_inf_mask]
    calculated_inf = calculated[calculated_inf_mask]
    return torch.equal(golden_inf, calculated_inf)


def ulp(x: Union[ttnn.Tensor, torch.Tensor]) -> Union[ttnn.Tensor, torch.Tensor]:
    "Return Unit of Least Precision for each element of a given tensor"

    received_ttnn_input = False
    if isinstance(x, ttnn.Tensor):
        x = ttnn.to_torch(x)
        received_ttnn_input = True

    # Notes:
    # - This should be identical to the definition of ULP by Goldberg
    #   "What every computer scientist should know about floating-point arithmetic"
    #   https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
    # - We use torch.abs(x) to ensure symmetry ULP(-x) == ULP(x)
    # - For x powers of 2, x + ULP(x) is not closest number but second closest (previous number is 2x closer)
    #   However, this avoids rounding-to-nearest-tie-to-even issues on addition (i.e. x + ULP(x) != x)
    abs_x = torch.abs(x)
    next = torch.nextafter(
        abs_x, torch.tensor(math.inf, dtype=x.dtype)
    )  # 1 ULP ~ Difference between two consecutive floating point numbers
    ulp_value = next - abs_x

    # Special case: if abs_x == torch.finfo(x.dtype).max, then next == math.inf, which leads to ULP(x) == inf rather than finite number
    # We fix this problem by manually calculating ULP at max value, and masking tensor when input == max
    dtype_max = torch.finfo(x.dtype).max
    max_epsilon = dtype_max - torch.nextafter(
        torch.tensor(dtype_max, dtype=x.dtype), torch.tensor(-math.inf, dtype=x.dtype)
    )
    ulp_value = torch.where(abs_x == dtype_max, max_epsilon, ulp_value)

    if received_ttnn_input:  # Ensures that type(input) == type(output)
        ulp_value = ttnn.from_torch(ulp_value)

    return ulp_value


def comp_ulp(golden, calculated, ulp_threshold, allow_nonfinite=False):
    """
    Compute absolute error between two tensors in Units of Least Precision (ULP)
    """

    # If both tensors are empty, then we can return True
    if torch.numel(golden) == 0 and torch.numel(calculated) == 0:
        return True, "Both tensors are empty"

    if not allow_nonfinite and not torch.all(torch.isfinite(calculated)):
        return False, "Calculated tensor contains non-finite values"

    if not _comp_nonfinite(golden, calculated):
        return False, "Tensors are not finite at the same positions"
    # nonfinite elments can intefere with ULP error calculation
    # To avoid this, replace nan, +inf, -inf with 0
    # (we have already checked that both tensors have the same nonfinite elements)
    mask_finite = ~torch.isfinite(golden)
    golden = golden.clone()
    calculated = calculated.clone()
    golden[mask_finite] = 0
    calculated[mask_finite] = 0

    # ULP is measured according to the golden tensor
    # In most cases, data type of golden tensor should be the same as calculated tensor.
    # However, in some cases, we may want to measure < 1 ULP differences, which requires golden tensor
    # to have higher precision than calculated tensor.
    # If we passed golden tensor to ulp() as is, we would get ULP of higher precision.
    # e.g. ulp of float32 rather bfloat16 calculation, which would give us a wrong value.
    ulp_value = ulp(golden.type(calculated.dtype))

    if golden.dtype != calculated.dtype:  # Note: assumes that golden has higher precision than calculated tensor
        calculated = calculated.type(golden.dtype)
        ulp_value = ulp_value.type(golden.dtype)  # Convert ULP to higher precision (for sub-1 ULP measurements)

    ulp_delta = torch.max(torch.abs(calculated - golden) / ulp_value)

    return (ulp_delta <= ulp_threshold, f"Max ULP Delta: {ulp_delta}")


# Dictionaries for converting dtypes
tt_dtype_to_torch_dtype = {
    ttnn.uint8: torch.uint8,
    ttnn.uint16: torch.int16,
    ttnn.uint32: torch.int32,
    ttnn.int32: torch.int32,
    ttnn.float32: torch.float,
    ttnn.bfloat16: torch.bfloat16,
    ttnn.bfloat8_b: torch.float,
    ttnn.bfloat4_b: torch.float,
}


def assert_with_ulp(
    expected_result: Union[ttnn.Tensor, torch.Tensor],
    actual_result: Union[ttnn.Tensor, torch.Tensor],
    ulp_threshold=10,
    allow_nonfinite=False,
):
    def tt_dtype_to_torch_dtype_for_ulp(tt_dtype):
        # By default, ttnn converts ttnn.bfloat8_b to torch.float
        # However, the resolution of a bfloat8_b value is the same as bfloat16
        # (assuming all elements within the block share the same exponent)
        # Thus, for ULP measurement, we convert bfloat8_b to bfloat16 instead of float32
        if tt_dtype == ttnn.bfloat8_b:
            return torch.bfloat16
        if tt_dtype not in tt_dtype_to_torch_dtype:
            raise ValueError(f"Trying to measure ULP on unknown dtype: {tt_dtype}")
        return tt_dtype_to_torch_dtype[tt_dtype]

    if isinstance(expected_result, ttnn.Tensor):
        expected_result = ttnn.to_torch(expected_result, dtype=tt_dtype_to_torch_dtype_for_ulp(expected_result.dtype))
    if isinstance(actual_result, ttnn.Tensor):
        actual_result = ttnn.to_torch(actual_result, dtype=tt_dtype_to_torch_dtype_for_ulp(actual_result.dtype))

    assert list(expected_result.shape) == list(
        actual_result.shape
    ), f"list(expected_result.shape)={list(expected_result.shape)} vs list(actual_result.shape)={list(actual_result.shape)}"

    maximum_meaningful_ulp_thresholds = {
        torch.float64: 2**52,
        torch.float32: 2**23,
        torch.float16: 2**10,
        torch.bfloat16: 2**7,
    }
    maximum_meaningful_ulp_threshold = (
        maximum_meaningful_ulp_thresholds[torch.float32]
        if expected_result.dtype in maximum_meaningful_ulp_thresholds
        else maximum_meaningful_ulp_thresholds[expected_result.dtype]
    )

    # if ulp_threshold > maximum_meaningful_ulp_threshold:
    #     logger.warning(
    #         f"ULP threshold {ulp_threshold} is greater than the maximum meaningful ULP threshold of {maximum_meaningful_ulp_threshold} for dtype {expected_result.dtype}"
    #     )

    ulp_passed, ulp_message = comp_ulp(expected_result, actual_result, ulp_threshold, allow_nonfinite)
    assert ulp_passed, ulp_message
    return ulp_passed, ulp_message


def comp_allclose(golden, calculated, rtol=1e-05, atol=1e-08):
    if golden.dtype != calculated.dtype:
        calculated = calculated.type(golden.dtype)

    atol_delta = torch.max(torch.abs(golden - calculated)).item()
    rtol_delta = torch.max(torch.abs(golden - calculated) / torch.abs(calculated)).item()
    return (
        torch.allclose(golden, calculated, rtol, atol, True),
        f"Max ATOL Delta: {atol_delta}, Max RTOL Delta: {rtol_delta}",
    )


def assert_allclose(
    expected_result: Union[ttnn.Tensor, torch.Tensor],
    actual_result: Union[ttnn.Tensor, torch.Tensor],
    rtol=1e-05,
    atol=1e-08,
):
    if isinstance(expected_result, ttnn.Tensor):
        expected_result = ttnn.to_torch(expected_result)
    if isinstance(actual_result, ttnn.Tensor):
        actual_result = ttnn.to_torch(actual_result)

    assert list(expected_result.shape) == list(
        actual_result.shape
    ), f"list(expected_pytorch_result.shape)={list(expected_result.shape)} vs list(actual_pytorch_result.shape)={list(actual_result.shape)}"
    allclose_passed, allclose_message = comp_allclose(expected_result, actual_result, rtol, atol)
    assert allclose_passed, allclose_message
    return allclose_passed, allclose_message


# Outputs can be a mix of nested Lists/Dicts of Torch Tensors.
# This function will recursively process them.
def calculate_accuracy(original_outputs, compiled_outputs) -> float:
    if isinstance(original_outputs, torch.Tensor) and isinstance(compiled_outputs, torch.Tensor):
        # Base case: Outputs are Torch tensors
        _, accuracy = comp_pcc(original_outputs, compiled_outputs)
        return accuracy
    elif (isinstance(original_outputs, list) and isinstance(compiled_outputs, list)) or (
        isinstance(original_outputs, tuple) and isinstance(compiled_outputs, tuple)
    ):
        # Outputs are lists or tuples
        assert len(original_outputs) == len(compiled_outputs), (
            f"Original and compiled output do not have the same length."
            f"original length: {len(original_outputs)}\ncompiled length: {len(compiled_outputs)}"
        )
        accuracies = []
        for original_output, compiled_output in zip(original_outputs, compiled_outputs):
            accuracies.append(calculate_accuracy(original_output, compiled_output))
        return np.mean(accuracies)
    elif isinstance(original_outputs, dict) and isinstance(compiled_outputs, dict):
        # Outputs are dicts
        original_outputs = dict(original_outputs)
        compiled_outputs = dict(compiled_outputs)
        accuracies = []
        assert original_outputs.keys() == compiled_outputs.keys(), (
            f"Original and compiled output do not have the same set of keys."
            f"original keys:\n{original_outputs.keys()}\ncompiled keys:\n{compiled_outputs.keys()}"
        )
        for key in original_outputs.keys():
            original_output = original_outputs[key]
            compiled_output = compiled_outputs[key]
            accuracies.append(calculate_accuracy(original_output, compiled_output))
        return np.mean(accuracies)
    else:
        raise ValueError(
            f"Output types are not comparable:\noriginal_outputs:\n{type(original_outputs)}\ncompiled_outputs:\n{type(compiled_outputs)}"
        )


class MetricStrRenderer:
    def __init__(self, op_name: str, input_str: str):
        self.op_name = op_name
        self.input_str = input_str
        self.render_val_by_type = {
            "Tensor": self._by_tensor,
            "bool": self._by_basic,
            "int": self._by_basic,
            "float": self._by_basic,
            "number": self._by_basic,
            "Optional[Tensor]": self._by_optionalTensor,
            "Optional[bool]": self._by_optionalBasic,
            "Optional[int]": self._by_optionalBasic,
            "Optional[float]": self._by_optionalBasic,
            "Optional[number]": self._by_optionalBasic,
            "List[Tensor]": self._by_listTensor,
            "List[bool]": self._by_listBasic,
            "List[int]": self._by_listBasic,
            "List[float]": self._by_listBasic,
            "List[number]": self._by_listBasic,
            "List[Optional[Tensor]]": self._by_listOptionalTensor,
            "List[Optional[bool]]": self._by_listOptionalBasic,
            "List[Optional[int]]": self._by_listOptionalBasic,
            "List[Optional[float]]": self._by_listOptionalBasic,
            "List[Optional[number]]": self._by_listOptionalBasic,
            "Optional[List[Tensor]]": self._by_optionalListTensor,
            "Optional[List[bool]]": self._by_optionalListBasic,
            "Optional[List[int]]": self._by_optionalListBasic,
            "Optional[List[float]]": self._by_optionalListBasic,
            "Optional[List[number]]": self._by_optionalListBasic,
            "Device": self._by_device,
            "Optional[Device]": self._by_OptionalDevice,
        }

    def _by_tensor(self, parsed):
        if parsed["shape"] == "":
            return self._by_basic(parsed)
        else:
            if parsed["raw_val"] != "None":
                # TODO: adapt raw_val in shape tensor
                return None, False
            try:
                shape = eval(parsed["shape"])
                val = torch.randn(shape).type(torch.bfloat16)
                return val, True
            except Exception as e:
                print("Error in MetricStrRenderer._by_tensor:", e)
                return None, False

    def _by_basic(self, parsed):
        if parsed["raw_val"] == "inf" or parsed["raw_val"] == "-inf":
            parsed["raw_val"] = f"float('{parsed['raw_val']}')"
        try:
            val = eval(parsed["raw_val"])
            return val, True
        except Exception as e:
            print("Error in MetricStrRenderer._by_basic:", e)
            return None, False

    def _by_optionalTensor(self, parsed):
        return self._by_tensor(parsed)

    def _by_optionalBasic(self, parsed):
        return self._by_basic(parsed)

    def _by_listTensor(self, parsed):
        def parse_list_tensor_raw_val(raw_val):
            # '[None, None, <[12, 1]>, <[16]>]' to [None, None, [12, 1], [16]]
            raw_val = raw_val.replace("<", "").replace(">", "")
            return eval(raw_val)

        try:
            val = []
            raw_list = parse_list_tensor_raw_val(parsed["raw_val"])
            for r in raw_list:
                if r == None:
                    val.append(None)
                else:
                    shape = r
                    val.append(torch.randn(shape).type(torch.bfloat16))
            return val, True
        except Exception as e:
            print("Error in MetricStrRenderer._by_listTensor:", e)
            return None, False

    def _by_listBasic(self, parsed):
        return self._by_basic(parsed)

    def _by_listOptionalTensor(self, parsed):
        return self._by_listTensor(parsed)

    def _by_listOptionalBasic(self, parsed):
        return self._by_basic(parsed)

    def _by_optionalListTensor(self, parsed):
        return self._by_listTensor(parsed)

    def _by_optionalListBasic(self, parsed):
        return self._by_listBasic(parsed)

    def _by_device(self, parsed):
        parsed["raw_val"] = f"'{parsed['raw_val']}'"
        return self._by_basic(parsed)

    def _by_OptionalDevice(self, parsed):
        return self._by_device(parsed)

    def _parse_input_str(self) -> Tuple[Dict, bool]:
        try:
            pattern = r"(?P<type>[\[\]\w]+)<?(?P<shape>[^>]*)>?\s+(?P<name>\w+)\s*=\s*(?P<raw_val>.*)"
            m = re.match(pattern, self.input_str)
            parsed = {
                "type": m.group("type"),
                "shape": m.group("shape"),
                "name": m.group("name"),
                "raw_val": m.group("raw_val"),
            }
            if parsed["raw_val"] == "" or parsed["raw_val"] == "?":
                parsed["raw_val"] = "None"
            return parsed, True
        except Exception as e:
            print("Error in MetricStrRenderer._parse_input_str:", e)
            return None, False

    def render_input_val(self):
        parsed, status = self._parse_input_str()
        if status == False:
            return None, False
        val, status = self.render_val_by_type[parsed["type"]](parsed)
        if status == False:
            return None, False
        input_val = {"name": parsed["name"], "val": val}
        return input_val, True


class MetricStringListHandler:
    def __init__(self, op_name: str, input_strings: List[str]):
        self.op_name = op_name
        self.input_strings = input_strings
        self.post_adjustment_ops = {
            "aten.bitwise_not.default": self._adjust_bitwise_not_default,
            "aten.masked_fill.Scalar": self._adjust_masked_fill_Scalar,
            "aten.where.self": self._adjust_where_self,
            "aten.embedding.default": self._adjust_embedding_default,
            "aten.embedding_dense_backward.default": self._adjust_embedding_dense_backward_default,
            "aten.index_select.default": self._adjust_index_select_default,
            "aten.index.Tensor": self._adjust_index_tensor,
            "aten.index_put.default": self._adjust_index_tensor,
            "aten._native_batch_norm_legit_no_training.default": self._adjust__native_batch_norm_legit_no_training_default,
            "aten._unsafe_index.Tensor": self._adjust_index_tensor,
        }

    def _adjust_bitwise_not_default(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "self":
                input_val["val"] = input_val["val"].type(torch.int)
                break
        return input_vals

    def _adjust_masked_fill_Scalar(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "mask":
                input_val["val"] = torch.randint(0, 2, input_val["val"].shape).type(torch.bool)
                break
        return input_vals

    def _adjust_where_self(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "condition":
                input_val["val"] = torch.randint(0, 2, input_val["val"].shape).type(torch.bool)
                break
        return input_vals

    def _adjust_embedding_default(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "weight":
                weight_shape0 = input_val["val"].shape[0]
                break
        for input_val in input_vals:
            if input_val["name"] == "indices":
                input_val["val"] = torch.randint(0, weight_shape0, input_val["val"].shape)
                break
        return input_vals

    def _adjust_embedding_dense_backward_default(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "grad_output":
                grad_output_shape0 = input_val["val"].shape[0]
                break
        for input_val in input_vals:
            if input_val["name"] == "indices":
                input_val["val"] = torch.randint(0, grad_output_shape0, input_val["val"].shape)
                break
        return input_vals

    def _adjust_index_select_default(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "self":
                self_shape = input_val["val"].shape
                break
        for input_val in input_vals:
            if input_val["name"] == "dim":
                dim = input_val["val"]
                break
        for input_val in input_vals:
            if input_val["name"] == "index":
                input_val["val"] = torch.randint(0, self_shape[dim], input_val["val"].shape)
                break
        return input_vals

    def _adjust__native_batch_norm_legit_no_training_default(self, input_vals):
        for input_val in input_vals:
            # Make sure the running_var >= 0
            if input_val["name"] == "running_var":
                input_val["val"] = input_val["val"] ** 2
                break
        return input_vals

    def _adjust_index_tensor(self, input_vals):
        for input_val in input_vals:
            if input_val["name"] == "self":
                self_shape = input_val["val"].shape
                break
        for input_val in input_vals:
            if input_val["name"] == "indices":
                indices = input_val["val"]
                new_indices = []
                for i in range(len(indices)):
                    indice = indices[i]
                    if indice is None:
                        new_indices.append(None)
                    else:
                        new_indices.append(torch.randint(0, self_shape[i], indice.shape))
                input_val["val"] = new_indices
                break
        return input_vals

    def build_input_args_kwargs(self, input_vals):
        input_args = []
        input_kwargs = {}
        has_self = any(input_val["name"] == "self" for input_val in input_vals)

        if not has_self:
            input_kwargs = {input_val["name"]: input_val["val"] for input_val in input_vals}
        else:
            before_self = True
            for input_val in input_vals:
                if before_self:
                    input_args.append(input_val["val"])
                else:
                    input_kwargs[input_val["name"]] = input_val["val"]
                if input_val["name"] == "self":
                    before_self = False

        return input_args, input_kwargs

    def render_input_args_kwargs(self) -> Tuple[List, Dict, bool]:
        input_vals = []
        for input_str in self.input_strings:
            renderer = MetricStrRenderer(self.op_name, input_str)
            input_val, status = renderer.render_input_val()
            if status == False:
                return None, None, False
            input_vals.append(input_val)
        if self.op_name in self.post_adjustment_ops:
            input_vals = self.post_adjustment_ops[self.op_name](input_vals)
        input_args, input_kwargs = self.build_input_args_kwargs(input_vals)
        return input_args, input_kwargs, True


def render_metric_string_list_to_input_args_kwargs(op_name, input_strings) -> Tuple[List, Dict, bool]:
    handler = MetricStringListHandler(op_name, input_strings)
    return handler.render_input_args_kwargs()
