import os
import sys
import argparse
import pickle
from pathlib import Path


class GuardFuncExporter:
    def __init__(self, metric_input_var_path: Path):
        self.metric_input_var_path = metric_input_var_path
        self.input_vars_result = self.load_input_varations_test_result()

    def render_string(self, template: str, key: str, replacement: str) -> str:
        result = template.replace("{" + key + "}", replacement)
        return result

    def load_pickle(self, path: str):
        if os.path.isfile(path):
            with open(path, "rb") as f:
                return pickle.load(f)
        else:
            return None

    def load_input_varations_test_result(self):
        input_vars_result = {}
        for dirpath, dirnames, filenames in os.walk(self.metric_input_var_path):
            input_vars_result_model = []
            for filename in filenames:
                if filename.endswith(".pickle"):
                    path = Path(dirpath) / filename
                    input_vars_result_model += self.load_pickle(path)
            model_name = dirpath.split("/")[-1].replace(" ", "_")
            if input_vars_result_model:
                input_vars_result[model_name] = input_vars_result_model
        return input_vars_result

    def get_op_blocklist(self, threshold: list):
        def need_block(input_var: dict, threshold: list):
            for key in threshold:
                if input_var[key] == False:
                    return True

        op_blocklist = {}
        for model_name, input_vars in self.input_vars_result.items():
            for input_var in input_vars:
                if need_block(input_var, threshold):
                    opname = input_var["opname"]
                    if opname not in op_blocklist:
                        op_blocklist[opname] = []
                    if input_var["input_strings"] not in op_blocklist[opname]:
                        op_blocklist[opname].append(input_var["input_strings"])
        return op_blocklist

    def export_guard_function(self, template_path: Path, threshold: list = ["run", "accuracy"]):
        blocklist_list = []
        guardfunc_list = []
        guard_ops_list = []
        op_blocklist = self.get_op_blocklist(threshold)
        for opname, blocklist in op_blocklist.items():
            op_name_ = opname.replace(".", "_")
            op_blocklist_name = f"{op_name_}_blocklist"
            blocklist = f"{op_blocklist_name} = {str(blocklist)}"
            guardfunc = f"torch.ops.{opname}: partial(guard_aten, {op_blocklist_name}),"
            guard_ops = f"torch.ops.{opname}"
            blocklist_list.append(blocklist)
            guardfunc_list.append(guardfunc)
            guard_ops_list.append(f'"{guard_ops}",')

        with open(template_path, "r") as f:
            text = f.read()

        text = self.render_string(text, "BLOCKLIST", "\n".join(blocklist_list))
        text = self.render_string(text, "GUARD", "\n".join(guardfunc_list))
        text = self.render_string(text, "GUARD_OPS", "\n".join(guard_ops_list))

        guard_path = "to_tt_guard_autogen.py"
        with open(guard_path, "w") as f:
            f.write(text)
        os.system(f"pre-commit run --files {guard_path} > /dev/null")
        print(f"Guard function generated: ./{guard_path}")


if __name__ == "__main__":
    template_path = os.path.dirname(os.path.abspath(__file__)) + "/to_tt_guard_autogen.tmpl"

    if not os.path.isdir("metrics-autogen-op"):
        print("metrics-autogen-op directory not found. Please run tests/autogen-op")
        exit(0)

    exporter = GuardFuncExporter(Path("metrics-autogen-op"))
    exporter.export_guard_function(template_path, threshold=["run", "accuracy"])
