import os
import sys
from pathlib import Path

tmp = Path(os.path.abspath(__file__))
sys.path.append(str(tmp.parent.parent))
from tools.collect_metrics import load_pickle, InputVarPerOp


class AtenOpTestExporter(InputVarPerOp):
    def render_string(self, template: str, key: str, replacement: str) -> str:
        result = template.replace("{" + key + "}", replacement)
        return result

    def export_tests(self, template_path: Path, basedir: Path, model_name: str):
        # undo _join_br
        def _unjoin_br(str_br: str):
            return str_br.split(",<br>")

        sort_by_opname = dict(sorted(self.items()))
        mdoel_name = basedir.parts[-1]
        basedir.mkdir(parents=True, exist_ok=True)
        for opname, inputs_variations in sort_by_opname.items():
            inputs_strings = [_unjoin_br(input_variations) for input_variations in inputs_variations.keys()]
            opname_ = opname.replace(".", "_")
            metrics_dir = f"metrics-input-variations/{model_name}"
            metrics_filename = opname
            filename = f"test_{mdoel_name}_{opname_}.py"
            with open(template_path, "r") as f:
                text = f.read()
            text = self.render_string(text, "opname", opname)
            text = self.render_string(text, "inputs_strings", str(inputs_strings))
            text = self.render_string(text, "metrics_dir", metrics_dir)
            text = self.render_string(text, "metrics_filename", metrics_filename)
            with open(basedir / filename, "w") as f:
                f.write(text)


# Generate input variation tests only contain single op, it will
#  - check the graph has been rewritten and contain ttnn ops
#  - check inference result
if __name__ == "__main__":
    template_path = os.path.dirname(os.path.abspath(__file__)) + "/aten_test.tmpl"

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
        print("metrics directory not found. Please run models to generate metrics first.")
        exit(0)

    # Support subdirectories
    all_model_paths = sorted([Path(dirpath) for dirpath, dirnames, filenames in os.walk("metrics") if not dirnames])

    for model_path in all_model_paths:
        # Remove the "metrics" root directory and convert to string
        model = str(Path(*model_path.parts[1:]))
        model_ = model.replace(" ", "_").replace("(", "").replace(")", "")

        # Only collect input variations from original models
        original_schema_metrics_path = model_path / "original-schema_list.pickle"
        original_schema_metrics = load_pickle(original_schema_metrics_path) or {}
        input_var_per_op = AtenOpTestExporter(original_schema_metrics, compiled_schema_metrics={})
        input_var_per_op.export_tests(template_path, Path(f"tests/input-variations/{model_}"), model)
        os.system(f"pre-commit run --files tests/input-variations/{model_}/* > /dev/null")
