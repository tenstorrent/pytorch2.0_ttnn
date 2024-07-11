import torch
import os
import pickle
import csv
from pathlib import Path

from tests.utils import comp_pcc


def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)


# Map dictionary keys from metrics to header descriptions
csv_header_mappings = {
    "model": "Model",
    "success": "Run Success",
    "torch_ops_before": "Torch Ops (Before)",
    "torch_ops_remain": "Torch Ops (Remain)",
    "to_from_device_ops": "To/From_Device Ops",
    "original_run_time": "Original Run Time (s)",
    "compiled_run_time": "Compiled Run Time(s)",
    "accuracy": "Accuracy",
}

if __name__ == "__main__":
    # Holds the concatenation of all the metrics for each model
    all_metrics = []

    # Assumed directory structure example. Some files will not exist if test failed.
    """
    pytorch2.0_ttnn
    ├── metrics
        ├── BERT
        │   ├── compiled-op_metrics.pickle
        │   ├── compiled-outputs.pt
        │   ├── compiled-runtime_metrics.pickle
        │   ├── original-outputs.pt
        │   └── original-runtime_metrics.pickle
        └── ResNet18
            ├── compiled-runtime_metrics.pickle
            └── original-runtime_metrics.pickle
    """
    for model in os.listdir("metrics"):
        model_path = Path("metrics") / Path(model)

        # read pickle files
        original_runtime_metrics_path = model_path / "original-runtime_metrics.pickle"
        compiled_runtime_metrics_path = model_path / "compiled-runtime_metrics.pickle"
        # Both runtime files should exist
        assert os.path.isfile(
            original_runtime_metrics_path
        ), f"{original_runtime_metrics_path} file not found"
        assert os.path.isfile(
            compiled_runtime_metrics_path
        ), f"{compiled_runtime_metrics_path} file not found"
        original_runtime_metrics = load_pickle(original_runtime_metrics_path)
        compiled_runtime_metrics = load_pickle(compiled_runtime_metrics_path)

        # Rename run_time keys to match original or compiled
        if "run_time" in original_runtime_metrics:
            original_runtime_metrics[
                "original_run_time"
            ] = original_runtime_metrics.pop("run_time")
        if "run_time" in compiled_runtime_metrics:
            compiled_runtime_metrics[
                "compiled_run_time"
            ] = compiled_runtime_metrics.pop("run_time")

        # Metric containing op counts. Will not exist if test failed.
        compiled_ops_metrics_path = model_path / "compiled-op_metrics.pickle"
        compiled_ops_metrics = (
            load_pickle(compiled_ops_metrics_path)
            if os.path.isfile(compiled_ops_metrics_path)
            else {}
        )

        # Read outputs and compute accuracy. Will not exist if test failed.
        # Some models have multiple outputs. Collect them all and compute the average pcc.
        original_outputs_path = model_path / "original-outputs.pt"
        compiled_outputs_path = model_path / "compiled-outputs.pt"

        original_outputs = (
            torch.load(original_outputs_path)
            if os.path.isfile(original_outputs_path)
            else {}
        )
        compiled_outputs = (
            torch.load(compiled_outputs_path)
            if os.path.isfile(compiled_outputs_path)
            else {}
        )

        if isinstance(original_outputs, dict) and isinstance(compiled_outputs, dict):
            # Handle case where outputs can be converted to dictionaries
            if not original_outputs or not compiled_outputs:
                accuracy = "N/A"
            else:
                original_outputs = dict(original_outputs)
                compiled_outputs = dict(compiled_outputs)
                output_pccs = []
                for key in original_outputs.keys() & compiled_outputs.keys():
                    _, pcc = comp_pcc(original_outputs[key], compiled_outputs[key])
                    output_pccs.append(pcc)
                accuracy = torch.mean(torch.tensor(output_pccs)).item()
        elif isinstance(original_outputs, torch.Tensor) and isinstance(
            compiled_outputs, torch.Tensor
        ):
            # Handle case where outputs are Pytorch Tensors
            _, accuracy = comp_pcc(original_outputs, compiled_outputs)
        else:
            raise ValueError(
                f"Output types not supported. Review these outputs:\n"
                f"original_outputs:\n"
                f"{original_outputs}\n"
                f"compiled_outputs:\n"
                f"{compiled_outputs}\n",
            )
        accuracy_metric = {"accuracy": accuracy}
        model_metric = {"model": model}

        # Concatenate all the metrics together
        cat_metrics = {
            **original_runtime_metrics,
            **compiled_runtime_metrics,
            **compiled_ops_metrics,
            **accuracy_metric,
            **model_metric,
        }
        # Remap original keys with header descriptions to prepare for exporting to csv
        cat_metrics_remapped = {}
        for key, val in csv_header_mappings.items():
            if key in cat_metrics:
                cat_metrics_remapped[val] = cat_metrics[key]
            else:
                cat_metrics_remapped[val] = "N/A"

        all_metrics.append(cat_metrics_remapped)

    # Write to csv
    if all_metrics:
        with open(f"metrics.csv", "w", newline="") as f:
            w = csv.DictWriter(f, all_metrics[0].keys())
            w.writeheader()
            print(all_metrics[0].keys())
            for row in all_metrics:
                print(row)
                w.writerow(row)
            print(f"Data written to metrics.csv")
