import os
from pathlib import Path
from tools.collect_metrics import load_pickle, InputVarPerOp


class AtenOpTestExporter(InputVarPerOp):
    def render_string(self, template: str, key: str, replacement: str) -> str:
        result = template.replace("{" + key + "}", replacement)
        return result

    def export_tests(self, template_path: Path, basedir: Path):
        # undo _join_br
        def _unjoin_br(str_br: str):
            return str_br.split(",<br>")

        sort_by_opname = dict(sorted(self.items()))
        basedir.mkdir(parents=True, exist_ok=True)
        for opname, inputs_variations in sort_by_opname.items():
            inputs_strings = [_unjoin_br(input_variations) for input_variations in inputs_variations.keys()]
            opname_ = opname.replace(".", "_")
            filename = f"test_{opname_}.py"
            with open(template_path, "r") as f:
                text = f.read()
            text = self.render_string(text, "opname", opname)
            text = self.render_string(text, "inputs_strings", str(inputs_strings))
            with open(basedir / filename, "w") as f:
                f.write(text)


# Generate input variation tests only contain single op, it will
#  - check the graph has been rewritten and contain ttnn ops
#  - check inference result
if __name__ == "__main__":
    template_path = os.path.dirname(os.path.abspath(__file__)) + "/aten_test.tmpl"
    cumulative_input_vars = AtenOpTestExporter()

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

        # Only collect input variations from original models
        original_schema_metrics_path = model_path / "original-schema_list.pickle"
        original_schema_metrics = load_pickle(original_schema_metrics_path) or {}
        input_var_per_op = AtenOpTestExporter(original_schema_metrics, compiled_schema_metrics={})
        cumulative_input_vars.merge(input_var_per_op)

    cumulative_input_vars.export_tests(template_path, Path("tests/input_variation/"))
