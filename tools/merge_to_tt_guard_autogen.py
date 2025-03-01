# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
# Rename your two to_tt_guard_autogen.py as to_tt_guard_autogen1.py and to_tt_guard_autogen2.py and run this script
import to_tt_guard_autogen1 as g1
import to_tt_guard_autogen2 as g2
from pathlib import Path
import os


def merge_list(l1, l2):
    for v in l2:
        if v not in l1:
            l1.append(v)
    return l1


def merge_blocklist(b1, b2):
    for k, v in b2.items():
        if k not in b1:
            b1[k] = v
        else:
            b1[k] = merge_list(b1[k], v)
    return b1


def parse_blocklist(guard):
    blocklist_dict = {}
    for var in dir(guard):
        if var.startswith("aten_"):
            blocklist_dict_val = getattr(guard, var)
            blocklist_dict[var] = blocklist_dict_val
    return blocklist_dict


def get_guard_ops():
    guard_ops = g1.guard_ops
    for ops in g2.guard_ops:
        if ops not in guard_ops:
            guard_ops.append(ops)
    return guard_ops


def render_string(template: str, key: str, replacement: str) -> str:
    result = template.replace("{" + key + "}", replacement)
    return result


def export_guard_function(template_path: Path, guard_ops, blocklist_dict):
    blocklist_list = []
    guardfunc_list = []
    guard_ops_list = []

    for ops in guard_ops:
        opname = ops.replace("torch.ops.", "")
        op_name_ = opname.replace(".", "_")
        op_blocklist_name = f"{op_name_}_blocklist"
        blocklist = blocklist_dict[op_blocklist_name]
        blocklist = f"{op_blocklist_name} = {str(blocklist)}"
        guardfunc = f"torch.ops.{opname}: partial(guard_aten, {op_blocklist_name}),"
        guard_ops = f"torch.ops.{opname}"
        blocklist_list.append(blocklist)
        guardfunc_list.append(guardfunc)
        guard_ops_list.append(f'"{guard_ops}",')

    with open(template_path, "r") as f:
        text = f.read()

    text = render_string(text, "BLOCKLIST", "\n".join(blocklist_list))
    text = render_string(text, "GUARD", "\n".join(guardfunc_list))
    text = render_string(text, "GUARD_OPS", "\n".join(guard_ops_list))

    guard_path = "merged_to_tt_guard_autogen.py"
    with open(guard_path, "w") as f:
        f.write(text)
    os.system(f"pre-commit run --files {guard_path} > /dev/null")
    print(f"Guard function generated: ./{guard_path}")


if __name__ == "__main__":
    blocklist_dict1 = parse_blocklist(g1)
    blocklist_dict2 = parse_blocklist(g2)
    blocklist_dict = merge_blocklist(blocklist_dict1, blocklist_dict2)
    guard_ops = get_guard_ops()

    template_path = os.path.dirname(os.path.abspath(__file__)) + "/to_tt_guard_autogen.tmpl"
    export_guard_function(template_path, guard_ops, blocklist_dict)
