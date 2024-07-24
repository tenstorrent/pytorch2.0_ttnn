import torch
import os
import pickle
import csv
from pathlib import Path
import pandas as pd
import numpy as np

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
    "torch_ops_total_unique_before": (
        "Torch Ops Before (Unique Ops)",
        "The total number of operations used by the model in the original Torch implementation. The number in parenthesis represents the total unique ops.",
    ),
    "torch_ops_total_unique_remain": (
        "Torch Ops Remain (Unique Ops)",
        "The total number of operations used after conversion to TTNN. The number in parenthesis represents the total unique ops.",
    ),
    "to_from_device_ops": (
        "To/From Device Ops",
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

model_link_mappings = {
    "BERT": "tests/models/bert",
    "Bloom": "tests/models/bloom",
    "Falcon": "tests/models/falcon",
    "GPT-2": "tests/models/gpt2",
    "Llama": "tests/models/llama",
    "Mnist (Eval)": "tests/models/mnist",
    "Mnist (Train)": "tests/models/mnist",
    "ResNet18": "tests/models/resnet",
    "YOLOS": "tests/models/yolos",
}

if __name__ == "__main__":
    # Holds the concatenation of all the metrics for each model
    all_metrics = []

    # Holds the concatenation of input variation metrics for all models
    all_input_var_metrics = {}

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
    if not os.path.isdir("metrics"):
        raise ValueError(
            "metrics directory not found. Please run models to generate metrics first."
        )
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
            else None
        )
        compiled_outputs = (
            torch.load(compiled_outputs_path)
            if os.path.isfile(compiled_outputs_path)
            else None
        )

        if isinstance(original_outputs, dict) and isinstance(compiled_outputs, dict):
            # Handle case where outputs can be converted to dictionaries
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
        elif original_outputs is not None or compiled_outputs is not None:
            accuracy = "N/A"
        else:
            raise ValueError(
                f"Output types for {model} not supported. Review these outputs:\n"
                f"original_outputs:\n"
                f"{original_outputs}\n"
                f"compiled_outputs:\n"
                f"{compiled_outputs}\n"
            )
        accuracy_metric = {
            "accuracy": (
                round(accuracy, 2) if not isinstance(accuracy, str) else accuracy
            )
        }

        # Add links that point to the directory of the model in the model name
        model_metric = {"model": f"[{model}]({model_link_mappings[model]})"}

        # Add new column that formats the total torch ops like: "total torch ops (total unique torch ops)""
        if "torch_ops_before" in compiled_ops_metrics:
            torch_ops_unique_before = (
                compiled_ops_metrics["torch_ops_unique_before"]
                if "torch_ops_unique_before" in compiled_ops_metrics
                else "N/A"
            )
            compiled_ops_metrics[
                "torch_ops_total_unique_before"
            ] = f'{compiled_ops_metrics["torch_ops_before"]} ({torch_ops_unique_before})'

        if "torch_ops_remain" in compiled_ops_metrics:
            torch_ops_unique_remain = (
                compiled_ops_metrics["torch_ops_unique_remain"]
                if "torch_ops_unique_remain" in compiled_ops_metrics
                else "N/A"
            )
            compiled_ops_metrics[
                "torch_ops_total_unique_remain"
            ] = f'{compiled_ops_metrics["torch_ops_remain"]} ({torch_ops_unique_remain})'

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

        # Process input variation metrics. Currently, this is not per model, but per op.
        input_var_metrics_path = model_path / "aten_ops_input_variations.pickle"
        input_var_metrics = (
            load_pickle(input_var_metrics_path)
            if os.path.isfile(input_var_metrics_path)
            else {}
        )

        for key, val in input_var_metrics.items():
            if key not in all_input_var_metrics:
                all_input_var_metrics[key] = val
            else:
                # Only append if shape and value combination have not been collected
                for shape, value in zip(val["input_shapes"], val["input_values"]):
                    if (
                        shape not in all_input_var_metrics[key]["input_shapes"]
                        and value not in all_input_var_metrics[key]["input_values"]
                    ):
                        all_input_var_metrics[key]["input_shapes"].append(shape)
                        all_input_var_metrics[key]["input_values"].append(value)

    # Write input variation metrics to csv
    if all_input_var_metrics:
        # Holds the rows to generate csv
        input_var_list_for_csv = {}
        # turn input_shapes and input_values into individual columns
        for val in list(all_input_var_metrics.values()):
            # holds the variations of input string
            input_var_list = []
            for shapes, values in zip(val["input_shapes"], val["input_values"]):
                # holds each individual input to be joined to a string
                input_string_list = []
                for i, (shape, value) in enumerate(zip(shapes, values)):
                    # This instance is a kwarg
                    if isinstance(value, tuple):
                        arg_name = value[0]
                        arg_type = val["schema"]["kwargs"][arg_name]
                        arg_val = f" = {value[1]}"
                    else:
                        arg_type = val["schema"]["args"][i][0]
                        arg_name = val["schema"]["args"][i][1]
                        arg_val = f" = {value}" if value else ""

                    arg_shape = f"<{shape}>" if shape else ""

                    input_string_list.append(
                        f"{arg_type}{arg_shape} {arg_name}{arg_val}"
                    )
                input_var_list.append(", ".join(input_string_list))
            input_var_list_for_csv[val["opname"]] = input_var_list

        df = pd.DataFrame(
            {key: pd.Series(value) for key, value in input_var_list_for_csv.items()}
        )
        df.to_csv("input_variations.csv", encoding="utf-8", index=False)
        print(f"Data written to input_variations.csv")

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
    # FIXME: Remove this once metrics generation and collection work for multiple graphs
    explanations_md += "\n***\n**NOTE:** The total number of ops currently reflect only the first graph of a model. This will be fixed in a future update to include all graphs.  "

    # Load README.in as an f-string and substitute the variables
    with open("docs/README.md.in", "r") as text_file:
        readme_in = text_file.read()

    readme_comment = (
        "[comment]: <> (This README.md was generated by tools/collect_metrics.py.)\n"
        "[comment]: <> (Please modify docs/README.md.in and/or collect_metrics.py to make permanent changes.)\n"
    )
    readme_md = readme_comment + readme_in.format(
        metrics_md=metrics_md, explanations_md=explanations_md
    )

    with open("README.md", "w") as text_file:
        print(readme_md, file=text_file)

    print("Data written to README.md")
