import torch
import os
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from collections import Counter
import glob
from tests.utils import comp_pcc
from tools.data_collection import pydantic_models


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
        "Original Run Time (ms)",
        "Execution time (in seconds) of the model before conversion.",
    ),
    "compiled_run_time": (
        "Compiled Run Time (ms)",
        "Execution time (in seconds) of the model after conversion.",
    ),
    "accuracy": (
        "Accuracy (%)",
        "Model accuracy on a predefined test dataset after conversion.",
    ),
}


# Load a pickle file from path and return an object or None
def load_pickle(path: str):
    if os.path.isfile(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    else:
        return None


# Load a pt file from path and return a Torch tensor object or None
def load_pt(path: str):
    if os.path.isfile(path):
        return torch.load(path)
    else:
        return None


def collect_input_variations_from_nodes(schemas: list):
    """Creates a dictionary of unique nodes with their schema and input variations.

    Returns:
        ```
        {
            <opname>:
            {
                'opname': str,
                'schema': {"args": list(tuple), "kwargs": list(tuple)}
                'input_shapes': list(str),
                'input_values': list(str|tuple),
            },
            <opname2>: {...},
        }
        ```

    """
    collection = {}
    for node in schemas:
        if "schema" in node:
            opname = node["opname"]
            input_shapes = node["input_shapes"]
            input_values = node["input_values"]
            # Create a new entry if opname has not been registered
            if opname not in collection:
                entry = {
                    "opname": opname,
                    "schema": node["schema"],
                    "input_shapes": [input_shapes],
                    "input_values": [input_values],
                }
                collection[opname] = entry
            else:
                if (
                    input_shapes not in collection[opname]["input_shapes"]
                    and input_values not in collection[opname]["input_values"]
                ):
                    collection[opname]["input_shapes"].append(input_shapes)
                    collection[opname]["input_values"].append(input_values)
    return collection


def serialize_schema_metrics_to_string(schema, shapes, values):
    """Combine schema types, shapes, names, and values to a single string."""
    # holds each individual input
    input_string_list = []
    for i, (shape, value) in enumerate(zip(shapes, values)):
        # This instance is a kwarg
        if isinstance(value, tuple):
            arg_name = value[0]
            arg_type = schema["kwargs"][arg_name]
            arg_val = f" = {value[1]}"
        else:
            arg_type = schema["args"][i][0]
            arg_name = schema["args"][i][1]
            arg_val = f" = {value}" if value else ""
        arg_shape = f"<{shape}>" if shape else ""
        input_string_list.append(f"{arg_type}{arg_shape} {arg_name}{arg_val}")
    string = ", ".join(input_string_list)
    return string


def serialize_schema_metrics_to_operations(metrics):
    """Transform schema information to a list of `class Operation` pydantic models."""
    operations = []
    for node in metrics:
        op_schema_string = serialize_schema_metrics_to_string(
            node["schema"], node["input_shapes"], node["input_values"]
        )
        operations.append(pydantic_models.Operation(op_name=node["opname"], op_schema=op_schema_string))
    return operations


def create_aten_op_dict(aten_ops_before_list, aten_ops_remain_list):
    """Take a before and after list of ops and return a table of information

    Returns:
        Dictionary with the keys: ["aten ops", "status", "count"]
    """
    original_aten_ops_set = set(aten_ops_before_list)
    remaining_aten_ops_set = original_aten_ops_set.intersection(aten_ops_remain_list)

    original_aten_ops_count = Counter(aten_ops_before_list)
    aten_ops_dict = {"aten ops": [], "status": [], "count": []}
    for op in sorted(list(original_aten_ops_set)):
        aten_ops_dict["aten ops"].append(op)
        aten_ops_dict["count"].append(original_aten_ops_count[op])
        if op in remaining_aten_ops_set:
            aten_ops_dict["status"].append("✘")
        else:
            aten_ops_dict["status"].append("✅")
    return aten_ops_dict


def write_input_variation_metrics_to_csv(all_input_var_metrics):
    """Write a csv that contains input variations of each aten op."""
    # Holds the rows to generate csv
    input_var_list_for_csv = {}
    # turn input_shapes and input_values into individual columns
    for val in list(all_input_var_metrics.values()):
        # holds the variations of input string
        input_var_list = []
        for shapes, values in zip(val["input_shapes"], val["input_values"]):
            input_string_list = serialize_schema_metrics_to_string(val["schema"], shapes, values)
            input_var_list.append(", ".join(input_string_list))

        input_var_list_for_csv[val["opname"]] = input_var_list

    df = pd.DataFrame({key: pd.Series(value) for key, value in input_var_list_for_csv.items()})
    df.to_csv("input_variations.csv", encoding="utf-8", index=False)
    print(f"Data written to input_variations.csv")


def write_to_readme(all_metrics, aten_ops_per_model):
    """Write collected metrics to sections of the README.

    Current process:
    * Writes a table that contains a summary of currently tested models.
    * Writes a series of tables of each model containing the statuses of ops used.
    """
    # Create an explanation section for the headers
    explanations_md = "\n".join([f"**{val[0]}**: {val[1]}  " for val in csv_header_mappings.values()])
    # FIXME: Remove this once metrics generation and collection work for multiple graphs
    explanations_md += "\n***\n**NOTE:** The total number of ops currently reflect only the first graph of a model. This will be fixed in a future update to include all graphs.  "

    # Create a series of tables showing the status of converted ops per model
    aten_ops_md = ""
    for key, val in aten_ops_per_model.items():
        aten_ops_md += f"#### {key}\n"
        aten_ops_md += pd.DataFrame(val).to_markdown(index=False) + "\n"

    # Load README.in as an f-string and substitute the variables
    with open("docs/README.md.in", "r") as text_file:
        readme_in = text_file.read()

    readme_comment = (
        "[comment]: <> (This README.md was generated by tools/collect_metrics.py.)\n"
        "[comment]: <> (Please modify docs/README.md.in and/or collect_metrics.py to make permanent changes.)\n"
    )

    # Convert metrics to markdown table
    metrics_md = pd.DataFrame(all_metrics).to_markdown(index=False)

    # Write to README file
    readme_md = readme_comment + readme_in.format(
        metrics_md=metrics_md, explanations_md=explanations_md, aten_ops_md=aten_ops_md
    )
    with open("README.md", "w") as text_file:
        print(readme_md, file=text_file)
    print("Data written to README.md")


if __name__ == "__main__":
    # Holds the concatenation of all the metrics for each model
    all_metrics = []

    # Holds the concatenation of input variation metrics for all models
    all_input_var_metrics = {}

    # Hold aten ops per model
    aten_ops_per_model = {}

    # Assumed directory structure example. Some files will not exist if test failed.
    """
    pytorch2.0_ttnn
    ├── metrics
        ├── BERT
        │   ├── compiled-run_time_metrics.pickle
        │   ├── compiled-schema_list.pickle
        │   ├── original-runtime_metrics.pickle
        │   └── original-schema_list.pickle
        └── ResNet18
            ├── compiled-run_time_metrics.pickle
            └── compiled-schema_list.pickle
    """
    if not os.path.isdir("metrics"):
        raise ValueError("metrics directory not found. Please run models to generate metrics first.")
    for model in os.listdir("metrics"):
        model_path = Path("metrics") / Path(model)

        if not model_path.is_dir():
            continue

        # Load run time metrics
        original_runtime_metrics_path = model_path / "original-run_time_metrics.pickle"
        compiled_runtime_metrics_path = model_path / "compiled-run_time_metrics.pickle"
        original_runtime_metrics = load_pickle(original_runtime_metrics_path)
        compiled_runtime_metrics = load_pickle(compiled_runtime_metrics_path)
        # Both run time files should exist
        assert original_runtime_metrics, f"{original_runtime_metrics_path} file not found"
        assert compiled_runtime_metrics, f"{compiled_runtime_metrics_path} file not found"

        # Add links that point to the directory of the model in the model name
        assert "model_path" in original_runtime_metrics, "model_path key not in original_runtime_metrics"
        path_in_repo = original_runtime_metrics["model_path"]
        model_metric = {"model": f"[{model}]({path_in_repo})"}

        # Initialize the Pydantic model
        pydantic_model = pydantic_models.ModelRun(name=model, path_in_repo=path_in_repo)

        # Rename run_time keys to distinguish between original or compiled
        if "run_time" in original_runtime_metrics:
            run_time = original_runtime_metrics.pop("run_time")
            original_runtime_metrics["original_run_time"] = run_time
            pydantic_model.original_run_time = float(run_time)
        if "run_time" in compiled_runtime_metrics:
            run_time = compiled_runtime_metrics.pop("run_time")
            compiled_runtime_metrics["compiled_run_time"] = run_time
            pydantic_model.compiled_run_time = float(run_time)

        # Load op schema metrics
        original_schema_metrics_path = model_path / "original-schema_list.pickle"
        original_schema_metrics = load_pickle(original_schema_metrics_path) or {}

        compiled_schema_metrics_path = model_path / "compiled-schema_list.pickle"
        compiled_schema_metrics = load_pickle(compiled_schema_metrics_path) or {}

        # Count total number of original aten ops and unique aten ops
        ops_metrics = {
            "torch_ops_total_unique_before": "N/A",
            "torch_ops_total_unique_remain": "N/A",
            "to_from_device_ops": "N/A",
        }
        if original_schema_metrics:
            aten_ops_before_list = [
                node["opname"] for node in original_schema_metrics if node["opname"].startswith("aten.")
            ]
            aten_ops_before, aten_ops_unique_before = len(aten_ops_before_list), len(set(aten_ops_before_list))
            ops_metrics["torch_ops_total_unique_before"] = f"{aten_ops_before} ({aten_ops_unique_before})"

            # Populate schemas for each op for original graph
            pydantic_model.ops_original = serialize_schema_metrics_to_operations(original_schema_metrics)

            # Populate schemas for each op for compiled graph
            pydantic_model.ops_compiled = serialize_schema_metrics_to_operations(compiled_schema_metrics)

            # Count numer of aten ops remaning after conversion
            if compiled_schema_metrics:
                aten_ops_remain_list = [
                    node["opname"] for node in compiled_schema_metrics if node["opname"].startswith("aten.")
                ]
                aten_ops_remain, aten_ops_unique_remain = len(aten_ops_remain_list), len(set(aten_ops_remain_list))
                ops_metrics["torch_ops_total_unique_remain"] = f"{aten_ops_remain} ({aten_ops_unique_remain})"

                device_op_list = [
                    node["opname"]
                    for node in compiled_schema_metrics
                    if node["opname"].startswith("ttnn.to") or node["opname"].startswith("ttnn.from")
                ]
                ops_metrics["to_from_device_ops"] = f"{len(device_op_list)}"

                # Compile list of aten ops per model used for README
                aten_ops_per_model[model] = create_aten_op_dict(aten_ops_before_list, aten_ops_remain_list)

        # Get accuracy metric. Will not exist if test failed.
        if "accuracy" in compiled_runtime_metrics and compiled_runtime_metrics["accuracy"] is not None:
            acc = round(compiled_runtime_metrics["accuracy"] * 100, 2)
            accuracy_metric = {"accuracy": acc}
            pydantic_model.accuracy = acc
        else:
            accuracy_metric = {"accuracy": "N/A"}

        # Save run_success status before changing it
        pydantic_model.run_success = compiled_runtime_metrics["success"]
        # Remap bool to emoji
        emoji_map = {True: "✅", False: "✘"}
        compiled_runtime_metrics["success"] = emoji_map[compiled_runtime_metrics["success"]]

        # Concatenate all the metrics together
        cat_metrics = {
            **original_runtime_metrics,
            **compiled_runtime_metrics,
            **ops_metrics,
            **accuracy_metric,
            **model_metric,
        }
        # Remap original keys with header descriptions to prepare for markdown table
        cat_metrics_remapped = {}
        for key, val in csv_header_mappings.items():
            if key in cat_metrics:
                cat_metrics_remapped[val[0]] = cat_metrics[key]
            else:
                cat_metrics_remapped[val[0]] = "N/A"

        all_metrics.append(cat_metrics_remapped)

        # Process input variation metrics. Currently, this is not per model, but per op.
        input_var_metrics = collect_input_variations_from_nodes(original_schema_metrics)
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

        # Links to graphs
        if os.path.isfile(f"metrics/{model}/00.origin.dot.svg"):
            pydantic_model.graph_before = f"metrics/{model}/00.origin.dot.svg"
        # Search for the last graph available
        svg_list = sorted(glob.glob(f"metrics/{model}/*.svg"))
        if len(svg_list) > 1:
            pydantic_model.graph_after = svg_list[-1]

        # Generate JSON using Pydantic
        model_run_json = pydantic_model.model_dump_json(indent=2)
        model_run_filename = f"metrics/{model}/model_run.json"
        with open(model_run_filename, "w") as text_file:
            print(model_run_json, file=text_file)

        print(f"Data written to {model_run_filename}")

    # Write input variation metrics to csv
    if all_input_var_metrics:
        write_input_variation_metrics_to_csv(all_input_var_metrics)

    # Write collected metrics to README
    write_to_readme(all_metrics, aten_ops_per_model)
