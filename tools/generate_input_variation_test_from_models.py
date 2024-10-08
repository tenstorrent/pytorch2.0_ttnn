import os
import sys
from pathlib import Path

tmp = Path(os.path.abspath(__file__))
sys.path.append(str(tmp.parent.parent))
from tools.collect_metrics import load_pickle, InputVarPerOp


class InputVarTestExporter(InputVarPerOp):
    def export_tests(self, basedir: Path, model_name: str):
        # undo _join_br
        def _unjoin_br(str_br: str):
            return str_br.split(",<br>")

        sort_by_opname = dict(sorted(self.items()))
        basedir.mkdir(parents=True, exist_ok=True)
        for opname, inputs_variations in sort_by_opname.items():
            inputs_strings = [_unjoin_br(input_variations) for input_variations in inputs_variations.keys()]
            opname_ = opname.replace(".", "_")
            metrics_dir = f"metrics-input-variations/{model_name}"
            metrics_filename = opname
            filename = f"test_{opname_}.py"
            text = f"""
import torch
import torch_ttnn
import pytest
import pickle
import ttnn
from pathlib import Path
from tests.utils import calculate_accuracy, get_input_vals_from_metric_str


class AtenModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.ops.{opname}(*args, **kwargs)


metrics = []


def save_pickle(obj, base_path, filename):
    p = Path(base_path)
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{{filename}}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def teardown_module(module):
    print(metrics)
    save_pickle(metrics, "{metrics_dir}", "{metrics_filename}")


@pytest.mark.parametrize("input_strings", {inputs_strings})
def test_aten(device, input_strings, input_var_only_native, input_var_check_accu, input_var_check_ttnn):
    metric = {{
            "opname": "{opname}",
            "input_strings": input_strings,
            "native_run": False,
            "run": False,
            "accuracy": False,
            "convert_to_ttnn": False,
        }}
    m = AtenModule()
    input_args, input_kwargs = get_input_vals_from_metric_str("{opname}", input_strings)
    if input_args is None and input_kwargs is None:
        pytest.skip("Invalid input strings:" + str(input_strings))
    try:
        result_before = m.forward(*input_args, **input_kwargs)
        metric["native_run"] = True
    except Exception as e:
        print(f"Failed to run native. Raised exception: {{e}}")
    if metric["native_run"] == True:
        option = torch_ttnn.TorchTtnnOption(device=device)
        # option.gen_graphviz = True
        # The compilation is lazy, so we need to run forward once to trigger the compilation
        m = torch.compile(m, backend=torch_ttnn.backend, options=option)
        try:
            result_after = m.forward(*input_args, **input_kwargs)
            # option._out_fx_graphs[0].print_tabular()
            metric["run"] = True
        except Exception as e:
            print(f"Failed to run. Raised exception: {{e}}")

    if metric["run"] == True:
        # Check inference result
        accuracy = calculate_accuracy(result_before, result_after)
        if accuracy >= 0.99:
            metric["accuracy"] = True

        # Check the graph has be rewritten and contain ttnn ops
        nodes = list(option._out_fx_graphs[0].nodes)
        if any(["ttnn" in str(node) for node in nodes]):
            metric["convert_to_ttnn"] = True

    metrics.append(metric)

    if not input_var_only_native:
        assert metric["run"] == True
        if input_var_check_accu:
            assert metric["accuracy"] == True
        if input_var_check_ttnn:
            assert metric["convert_to_ttnn"] == True
"""
            with open(basedir / filename, "w") as f:
                f.write(text)


# Generate input variation tests only contain single op, it will
#  - check the graph has been rewritten and contain ttnn ops
#  - check inference result
if __name__ == "__main__":
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
        model_ = model.replace(" ", "_").replace("(", "").replace(")", "")

        # Only collect input variations from original models
        original_schema_metrics_path = model_path / "original-schema_list.pickle"
        original_schema_metrics = load_pickle(original_schema_metrics_path) or {}
        input_var_per_op = InputVarTestExporter(original_schema_metrics, compiled_schema_metrics={})
        input_var_per_op.export_tests(Path(f"tests/input-variations/{model_}"), model)
