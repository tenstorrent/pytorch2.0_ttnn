# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import os
import sys
from pathlib import Path
import argparse

tmp = Path(os.path.abspath(__file__))
sys.path.append(str(tmp.parent.parent))
from tools.collect_metrics import load_pickle, InputVarPerOp


class AtenOpTestExporter(InputVarPerOp):
    def render_string(self, template: str, key: str, replacement: str) -> str:
        result = template.replace("{" + key + "}", replacement)
        return result

    def export_tests(self, template_dir: Path, basedir: Path, model_name: str, model_name_: str):
        # undo _join_br
        def _unjoin_br(str_br: str):
            return str_br.split(",<br>")

        sort_by_opname = dict(sorted(self.items()))
        basedir.mkdir(parents=True, exist_ok=True)
        for opname, inputs_variations in sort_by_opname.items():
            inputs_strings = [_unjoin_br(input_variations) for input_variations in inputs_variations.keys()]
            opname_ = opname.replace(".", "_")
            metrics_dir = f"metrics-autogen-op/{model_name}"
            metrics_filename = opname
            model_name_ = model_name_.replace("/", "_")
            filename = f"test_{model_name_}_{opname_}.py"

            extra_accessor = ""
            if opname == "aten._native_batch_norm_legit_no_training.default":
                module_template = "aten_test_check_only_first_output_module.tmpl"
            else:
                module_template = "aten_test_generic_module.tmpl"
            # TODO(tt-metal#12099): ttnn.max_pool2d currently doesn't return indices so we only check the value for eval
            if opname == "aten.max_pool2d_with_indices.default" and not model_name.endswith("-train"):
                module_template = "aten_test_check_only_first_output_module.tmpl"
            # For non-training mode, only the first return value is meaningful
            elif opname == "aten._native_batch_norm_legit_no_training.default":
                module_template = "aten_test_check_only_first_output_module.tmpl"

            module_text = (template_dir / module_template).read_text()
            module_text = self.render_string(module_text, "opname", opname)

            text = (template_dir / "aten_test.tmpl").read_text()
            text = self.render_string(text, "test_module", module_text)
            text = self.render_string(text, "opname", opname)
            text = self.render_string(text, "inputs_strings", str(inputs_strings))
            text = self.render_string(text, "metrics_dir", metrics_dir)
            text = self.render_string(text, "metrics_filename", metrics_filename)
            (basedir / filename).write_text(text)
        os.system(f"pre-commit run --files {basedir}/* > /dev/null")


# Generate input variation tests only contain single op, it will
#  - check the graph has been rewritten and contain ttnn ops
#  - check inference result
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--merge", type=bool, default=False)
    args = parser.parse_args()

    if args.merge:
        all_exporter = AtenOpTestExporter()
    template_dir = Path(os.path.abspath(__file__)).parent / "templates"

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
        # Only collect input variations from original models
        original_schema_metrics_path = model_path / "original-schema_list.pickle"
        original_schema_metrics = load_pickle(original_schema_metrics_path) or {}
        if not original_schema_metrics:
            continue
        input_var_per_op = AtenOpTestExporter(original_schema_metrics, compiled_schema_metrics={})

        # Remove the "metrics" root directory and convert to string
        model = str(Path(*model_path.parts[1:]))
        model_ = model.replace(" ", "_").replace("(", "").replace(")", "").replace(".", "_")
        if not args.merge:
            input_var_per_op.export_tests(template_dir, Path(f"tests/autogen_op/{model_}"), model, model_)
        else:
            all_exporter.merge(input_var_per_op)
    if args.merge:
        all_exporter.export_tests(template_dir, Path(f"tests/autogen_op/ALL"), "ALL", "ALL")
