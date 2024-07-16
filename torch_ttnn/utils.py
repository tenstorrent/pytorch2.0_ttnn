import torch
import time
import os
from pathlib import Path
import pickle


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
        runtime_metrics = {"success": "✔️", "run_time": round(end - start, 2)}

        torch.save(ret, pt_out_path)
    except:
        runtime_metrics = {"success": "✘"}
        ret = None

    with open(pickle_out_path, "wb") as f:
        pickle.dump(runtime_metrics, f)

    return ret


# Ttnn globals added with torch.fx._register_custom_builtin
class TtnnDevice:
    def __repr__(self):
        return f"ttnn_Specified_Device"


class TtnnRowMajorLayout:
    def __repr__(self):
        return f"ttnn_ROW_MAJOR_LAYOUT"


class TtnnTileLayout:
    def __repr__(self):
        return f"ttnn_TILE_LAYOUT"


class TtnnUint32:
    def __repr__(self):
        return f"ttnn_uint32"


class TtnnBfloat16:
    def __repr__(self):
        return f"ttnn_bfloat16"


class TtnnDramMemoryConfig:
    def __repr__(self):
        return f"ttnn_DRAM_MEMORY_CONFIG"


class TtnnL1MemoryConfig:
    def __repr__(self):
        return f"ttnn_L1_MEMORY_CONFIG"
