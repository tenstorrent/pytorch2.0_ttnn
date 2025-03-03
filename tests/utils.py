import collections.abc
import torch
import numpy as np
import collections
import re
from typing import List, Dict, Tuple
import transformers


class ModelTester:
    def __init__(self, model_name, mode, batch_size=None):
        if mode not in ["train", "eval"]:
            raise ValueError(f"Current mode is not supported: {mode}")
        self.model_name = model_name
        self.mode = mode
        self.model = self._load_model()
        self.inputs = self._load_inputs()
        self.batch_size = batch_size
        self.validate_batch_size()
        self.batch_inputs()

    def _load_model(self):
        raise NotImplementedError("This method should be implemented in the derived class")

    def _load_inputs(self):
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
        if isinstance(inputs, collections.abc.Mapping):
            return model(**inputs)
        elif isinstance(inputs, collections.abc.Sequence):
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

    def batch_inputs(self):
        if self.batch_size is None:
            return
        if isinstance(self.inputs, dict) or isinstance(self.inputs, transformers.tokenization_utils_base.BatchEncoding):
            keys = self.inputs.keys()
            for key in keys:
                if isinstance(self.inputs[key], torch.Tensor):
                    self.inputs[key] = self.inputs[key].repeat(self.batch_size, 1)
        elif isinstance(self.inputs, torch.Tensor):
            if self.inputs.shape[0] == 0:
                self.inputs = self.inputs.squeeze(0)
            self.inputs = self.inputs.repeat(self.batch_size, *([1] * (self.inputs.dim())))
            self.inputs = self.inputs.squeeze(1)
        else:
            raise TypeError(f"Inputs type not supported for batching: {type(self.inputs)}")

    def validate_batch_size(self):
        if self.batch_size is None:
            return
        try:
            self.batch_size = int(self.batch_size)
        except Exception as e:
            raise TypeError(
                f"Failed to interpret batch size type {type(self.batch_size).__name__} (Must be an integer or None)"
            )


# Testing utils copied from tt-metal/tests/ttnn/utils_for_testing.py
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


def calculate_accuracy(original_outputs, compiled_outputs):
    if (
        isinstance(original_outputs, list) and len(original_outputs) == 1 and isinstance(original_outputs[0], dict)
    ) and (isinstance(compiled_outputs, list) and len(compiled_outputs) == 1 and isinstance(compiled_outputs[0], dict)):
        original_outputs = original_outputs[0]
        compiled_outputs = compiled_outputs[0]
    if isinstance(original_outputs, dict) and isinstance(compiled_outputs, dict):
        # Handle case where outputs can be converted to dictionaries
        original_outputs = dict(original_outputs)
        compiled_outputs = dict(compiled_outputs)
        output_pccs = []
        assert original_outputs.keys() == compiled_outputs.keys(), (
            f"Original and compiled output do not have the same set of keys."
            f"original keys:\n{original_outputs.keys()}\ncompiled keys:\n{compiled_outputs.keys()}"
        )
        for original_outputs, compiled_outputs in zip(original_outputs.values(), compiled_outputs.values()):
            # TODO: Support other sequence types
            if isinstance(original_outputs, torch.Tensor) and isinstance(compiled_outputs, torch.Tensor):
                _, pcc = comp_pcc(original_outputs, compiled_outputs)
                output_pccs.append(pcc)
        assert (
            output_pccs
        ), f"No comparable outputs:\noriginal_outputs:\n{original_outputs}\ncompiled_outputs:\n{compiled_outputs}"
        accuracy = torch.mean(torch.tensor(output_pccs)).item()
    elif (isinstance(original_outputs, list) and isinstance(compiled_outputs, list)) or (
        isinstance(original_outputs, tuple) and isinstance(compiled_outputs, tuple)
    ):
        # Handle case where outputs are lists
        output_pccs = []
        assert len(original_outputs) == len(compiled_outputs), (
            f"Original and compiled output do not have the same length."
            f"original length: {len(original_outputs)}\ncompiled length: {len(compiled_outputs)}"
        )
        for original_outputs, compiled_outputs in zip(original_outputs, compiled_outputs):
            if isinstance(original_outputs, torch.Tensor) and isinstance(compiled_outputs, torch.Tensor):
                _, pcc = comp_pcc(original_outputs, compiled_outputs)
                output_pccs.append(pcc)
        assert (
            output_pccs
        ), f"No comparable outputs:\noriginal_outputs:\n{original_outputs}\ncompiled_outputs:\n{compiled_outputs}"
        accuracy = torch.mean(torch.tensor(output_pccs)).item()
    elif isinstance(original_outputs, torch.Tensor) and isinstance(compiled_outputs, torch.Tensor):
        # Handle case where outputs are Pytorch Tensors
        _, accuracy = comp_pcc(original_outputs, compiled_outputs)
    else:
        accuracy = None
    return accuracy


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


def process_batched_logits(logits, batch_size):
    if batch_size is None:
        return logits
    else:
        if logits.dim() == 3:
            return logits[0, :, :].squeeze(0)
        elif logits.dim() == 2:
            return logits[0, :].squeeze(0)
        else:
            raise ValueError(f"Unrecognized logit dimension: {logits.shape.numel()} (not 2D or 3D including batch)")
