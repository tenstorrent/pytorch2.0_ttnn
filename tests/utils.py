import torch
import numpy as np
import collections


class ModelTester:
    def __init__(self, model_name, mode):
        if mode not in ["train", "eval"]:
            raise ValueError(f"Current mode is not supported: {mode}")
        self.model_name = model_name
        self.mode = mode
        self.model = self._load_model()
        self.inputs = self._load_inputs()

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
        if isinstance(inputs, collections.Mapping):
            return model(**inputs)
        elif isinstance(inputs, collections.Sequence):
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
    elif isinstance(original_outputs, torch.Tensor) and isinstance(compiled_outputs, torch.Tensor):
        # Handle case where outputs are Pytorch Tensors
        _, accuracy = comp_pcc(original_outputs, compiled_outputs)
    else:
        accuracy = None
    return accuracy
