import torch
import os
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from collections import Counter, defaultdict
import glob
from tests.utils import comp_pcc
from tools.data_collection import pydantic_models
from enum import Enum
import string

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
    "fits_in_memory": (
        "Fits in memory",
        "Whether a model is estimated to fit in SRAM memory.",
    ),
    "peak_sram_usage": (
        "Peak SRAM usage (in MB)",
        "What is the peak SRAM usage for a model during its execution phase.",
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


def join_str_list_with_delim(str_list: list, delim: str):
    return delim.join(str_list)


def join_br(str_list: list):
    return join_str_list_with_delim(str_list, ",<br>")


# This class labels the conversion status of an Op
class ConversionStatus(Enum):
    DONE = (1,)  # Conversion is successful
    FALLBACK = (2,)  # Only some are converted successfully
    BUG = (3,)  # Known issue with conversion
    NONE = (4,)  # No conversion at all
    UNKNOWN = (5,)  # Op was not processed, so status is unknown


def serialize_schema_metrics_to_operations(metrics):
    """Transform schema information to a list of `class Operation` pydantic models."""
    operations = []
    for node in metrics:
        if "original_inputs" in node:
            # This might not be right
            operations.append(
                pydantic_models.Operation(op_name=node["opname"], op_schema=join_br(node["original_inputs"]["inputs"]))
            )
        else:
            operations.append(pydantic_models.Operation(op_name=node["opname"], op_schema=join_br(node["inputs"])))
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


class InputVarStatus(defaultdict):
    def __init__(self):
        super(InputVarStatus, self).__init__(lambda: ConversionStatus.UNKNOWN)

    def get_conversion_status_count_for(self, status: ConversionStatus) -> int:
        count = 0
        for input in self.values():
            if input == status:
                count += 1
        return count

    def get_list_input_var_to_dict(self):
        sort_by_opname = dict(sorted(self.items()))
        """Convert list of InputVariations to markdown-compatible dict"""
        return {
            "ATen Input Variations": [x for x in sort_by_opname.keys()],
            "Status": [string.capwords(x.name) for x in sort_by_opname.values()],
        }


class InputVarPerOp(defaultdict):
    def __init__(self, original_schema_metrics={}, compiled_schema_metrics={}):
        super(InputVarPerOp, self).__init__(InputVarStatus)

        if original_schema_metrics and compiled_schema_metrics:
            self.classify_input_variation_per_op(original_schema_metrics)
            self.map_op_conversions(compiled_schema_metrics)

    def accumulate(self, other):
        for opname, input_var in other.items():
            for input, status in input_var.items():
                self[opname][input] = status

    def classify_input_variation_per_op(self, original_schema_metrics):
        for op in original_schema_metrics:
            opname = op["opname"]
            inputs = join_br(op["inputs"])
            self[opname][inputs]

    def map_op_conversions(self, compiled_schema_metrics):
        print(*self.items(), sep="\n")
        for op in compiled_schema_metrics:
            if "original_inputs" in op:
                original_opname = op["original_inputs"]["opname"]
                original_inputs = join_br(op["original_inputs"]["inputs"])
                self[original_opname][original_inputs] = ConversionStatus.DONE

    def generate_md_for_input_variations(self):
        """Generate markdown from a dict: `{opname: set(class InputVariation)}`."""
        # Create a high level table of each op first
        high_level_op_status = defaultdict(list)
        sort_by_opname = dict(sorted(self.items()))
        for opname, input_vars in sort_by_opname.items():
            high_level_op_status["Operations"].append(opname)
            high_level_op_status["Input Variations"].append(len(input_vars))
            high_level_op_status["Converted"].append(input_vars.get_conversion_status_count_for(ConversionStatus.DONE))

        md = ""
        md += f"# High Level Operations Status\n"
        md += pd.DataFrame(high_level_op_status).to_markdown(index=True) + "\n"

        md += "***\n"

        for opname, input_vars in sort_by_opname.items():
            input_vars_dict = input_vars.get_list_input_var_to_dict()
            md += f"### {opname}\n"
            md += pd.DataFrame(input_vars_dict).to_markdown(index=True) + "\n"

        return md

    def write_md_for_input_variations(self, basedir: Path, filename: Path):
        md = self.generate_md_for_input_variations()
        basedir.mkdir(parents=True, exist_ok=True)
        with open(basedir / filename, "w") as text_file:
            print(md, file=text_file)
        print(f"Data written to {basedir / filename}")


if __name__ == "__main__":
    # Holds the concatenation of all the metrics for each model
    all_metrics = []

    cumulative_input_vars = InputVarPerOp()

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

    # Support subdirectories
    all_model_paths = sorted([Path(dirpath) for dirpath, dirnames, filenames in os.walk("metrics") if not dirnames])

    for model_path in all_model_paths:
        # Remove the "metrics" root directory and convert to string
        model = str(Path(*model_path.parts[1:]))

        # Load run time metrics
        original_runtime_metrics_path = model_path / "original-run_time_metrics.pickle"
        compiled_runtime_metrics_path = model_path / "compiled-run_time_metrics.pickle"
        original_runtime_metrics = load_pickle(original_runtime_metrics_path)
        compiled_runtime_metrics = load_pickle(compiled_runtime_metrics_path)
        # Both run time files should exist
        assert original_runtime_metrics, f"{original_runtime_metrics_path} file not found"
        assert compiled_runtime_metrics, f"{compiled_runtime_metrics_path} file not found"

        # Initialize the Pydantic model
        pydantic_model = pydantic_models.ModelRun(name=model)

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

            # Count number of aten ops remaning after conversion
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

        pydantic_model.fit_in_memory = compiled_runtime_metrics["fits_in_memory"]
        pydantic_model.peak_sram_usage = compiled_runtime_metrics["peak_sram_usage"]

        # Process input variations per model
        input_var_per_op = InputVarPerOp(original_schema_metrics, compiled_schema_metrics)
        model_info_dir = Path("docs") / Path("models") / Path(model)
        input_var_per_op.write_md_for_input_variations(model_info_dir, Path("input_variations.md"))

        # Add links that point to the directory of the model info
        model_metric = {"model": f"[{model}](<{model_info_dir}>)"}
        pydantic_model.path_in_repo = str(model_info_dir)

        # Collect cumulative input variations
        cumulative_input_vars.accumulate(input_var_per_op)

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

    # Write cumulative input variations to file
    cumulative_input_vars.write_md_for_input_variations(Path("docs"), Path("cumulative_input_variations.md"))

    # Write collected metrics to README
    write_to_readme(all_metrics, aten_ops_per_model)
