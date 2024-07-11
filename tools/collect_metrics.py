import torch
import os
import pickle
import csv
from pathlib import Path
import pandas as pd

from tests.utils import comp_pcc


def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)


# Map dictionary keys from metrics to header descriptions
csv_header_mappings = {
    "model": ("Model", "Name of the model."),
    "success": (
        "Run Success",
        "Indicates whether the model runs successfully after conversion.",
    ),
    "torch_ops_before": (
        "Torch Ops (Before)",
        "The number of operations used by the model in the original Torch implementation.",
    ),
    "torch_ops_remain": (
        "Torch Ops (Remain)",
        "The number of operations used after conversion to TTNN.",
    ),
    "to_from_device_ops": (
        "To/From_Device Ops",
        "The number of `to/from_device` operations (data transfer to/from the device).",
    ),
    "original_run_time": (
        "Original Run Time (s)",
        "Execution time (in seconds) of the model before conversion.",
    ),
    "compiled_run_time": (
        "Compiled Run Time(s)",
        "Execution time (in seconds) of the model after conversion.",
    ),
    "accuracy": (
        "Accuracy",
        "Model accuracy on a predefined test dataset after conversion.",
    ),
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
                cat_metrics_remapped[val[0]] = cat_metrics[key]
            else:
                cat_metrics_remapped[val[0]] = "N/A"

        all_metrics.append(cat_metrics_remapped)

    # Write metrics to csv
    if all_metrics:
        with open(f"metrics.csv", "w", newline="") as f:
            w = csv.DictWriter(f, all_metrics[0].keys())
            w.writeheader()
            for row in all_metrics:
                w.writerow(row)
            print(f"Data written to metrics.csv")

    # Convert metrics to markdown table
    metrics_md = pd.DataFrame(all_metrics).to_markdown(index=False)

    # Create an explanation section for the headers
    explanations_md = "\n".join(
        [f"**{val[0]}**: {val[1]}  " for val in csv_header_mappings.values()]
    )

    # Load README.in as an f-string and substitute the variables
    with open("README.in", "r") as text_file:
        readme_in = text_file.read()

    readme_comment = "<!--- This README.md was generated by tools/collect_metrics.py. Please modify README.in and/or collect_metrics.py to make permanent changes. --->\n"
    readme_md = readme_comment + readme_in.format(
        metrics_md=metrics_md, explanations_md=explanations_md
    )

    with open("README.md", "w") as text_file:
        print(readme_md, file=text_file)
    print("Data written to README.md")
