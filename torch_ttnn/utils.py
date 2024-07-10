import torch
import numpy as np
import time
import os
from pathlib import Path
import pickle


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


def construct_pcc_assert_message(
    message, expected_pytorch_result, actual_pytorch_result
):
    messages = []
    messages.append(message)
    # messages.append("Expected")
    # messages.append(str(expected_pytorch_result))
    # messages.append("Actual")
    # messages.append(str(actual_pytorch_result))
    messages = [str(m) for m in messages]
    return "\n".join(messages)


def check_with_pcc(expected_pytorch_result, actual_pytorch_result, pcc=0.9999):
    if expected_pytorch_result.shape != actual_pytorch_result.shape:
        return (
            False,
            f"list(expected_pytorch_result.shape)={list(expected_pytorch_result.shape)} vs list(actual_pytorch_result.shape)={list(actual_pytorch_result.shape)}",
        )
    pcc_passed, pcc_message = comp_pcc(
        expected_pytorch_result, actual_pytorch_result, pcc
    )
    return pcc_passed, construct_pcc_assert_message(
        pcc_message, expected_pytorch_result, actual_pytorch_result
    )


def GraphCleanup(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()

    return gm


def RunTimeMetrics(path: str, prefix: str, f):
    """
    Measure the runtime of the model in seconds.
    * Exports a pickle file containing success and runtime data
    * Exports outputs in Pytorch tensor format

    Parameters:
        path (str): Typically the name of the model
        prefix (str): Either "original" or "compiled" is recommended
        f: lambda function of model run

    Example:
        output = RunTimeMetrics("BERT", "compiled", lambda: model(**inputs))

    Returns:
        Output from the model or None if model fails
    """
    p = Path(f"metrics/{path}")
    pt_out_path = p / f"{prefix}-outputs.pt"
    pickle_out_path = p / f"{prefix}-runtime_metrics.pickle"
    os.makedirs(p, exist_ok=True)
    try:
        start = time.perf_counter()
        ret = f()
        end = time.perf_counter()
        runtime_metrics = {"success": "Yes", "run_time": end - start}

        torch.save(ret, pt_out_path)
    except:
        runtime_metrics = {"success": "No"}
        ret = None

    with open(pickle_out_path, "wb") as f:
        pickle.dump(runtime_metrics, f)

    return ret


# See https://docs.google.com/document/d/1r2D4AagoeTRjEmXFnWzzafaWQkf-8hlIbX2ze-JAUFo/edit#heading=h.zad9rwqjv6cr
class DummyDevice:
    def __repr__(self):
        return f"ttnn_Specified_Device"


class DummyTtnnRowMajorLayout:
    def __repr__(self):
        return f"ttnn_ROW_MAJOR_LAYOUT"


class DummyTtnnTileLayout:
    def __repr__(self):
        return f"ttnn_TILE_LAYOUT"


class DummyTtnnUint32:
    def __repr__(self):
        return f"ttnn_uint32"


class DummyTtnnBfloat16:
    def __repr__(self):
        return f"ttnn_bfloat16"


class DummyTtlTensorTensorMemoryLayoutInterleaved:
    def __repr__(self):
        return f"ttl_tensor_TensorMemoryLayout_INTERLEAVED"


class DummyTtlTensorBufferTypeDram:
    def __repr__(self):
        return f"ttl_tensor_BufferType_DRAM"
