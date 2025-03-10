# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import os
import json
import torch
from torch.fx.passes.fake_tensor_prop import FakeTensorProp
from torch.fx.passes.infra.pass_base import PassBase, PassResult


def parse_fx_stat(gm: torch.fx.GraphModule, example_inputs, out_file):
    try:
        FakeTensorProp(gm).propagate(*example_inputs)
        prog_success = True
    except Exception as e:
        print(e)
        print("FakeTensorProp propagate failed")
        prog_success = False

    def get_tensor_info(t):
        def no_symInt_in_list(the_list):
            return not any(isinstance(element, torch.SymInt) for element in the_list)

        # Only record if the tensor is torch.Tensor
        # some shape is referenced by a variable, like [2, 256, s0, s1]
        if isinstance(t, torch.Tensor) and no_symInt_in_list(list(t.shape)):
            return {"shape": list(t.shape), "dtype": str(t.dtype)}
        else:
            return {}

    out = []
    for node in gm.graph.nodes:
        if node.op not in ["call_function", "call_method"]:
            continue
        node_info = {}
        # set node's op_type
        node_info["op_type"] = str(node.target)
        # skip set node's inputs/outpus if FakeTensorProp failed
        if prog_success == False:
            out.append(node_info)
            continue
        # set node's inputs info
        node_info["inputs"] = []
        inputs_info = node.args
        for input_info in inputs_info:
            input = {}
            if isinstance(input_info, torch.fx.node.Node):
                input = get_tensor_info(input_info.meta["val"])
            node_info["inputs"].append(input)
        # set node's outputs info
        node_info["outputs"] = []
        outputs_info = node.meta["val"]
        if isinstance(outputs_info, tuple) or isinstance(outputs_info, list):
            for output_info in outputs_info:
                output = get_tensor_info(output_info)
                node_info["outputs"].append(output)
        elif isinstance(outputs_info, torch.Tensor):
            output = get_tensor_info(outputs_info)
            node_info["outputs"].append(output)
        else:
            assert 0 and "unsupport outputs_info"
        out.append(node_info)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    with open(out_file, "w") as f:
        json.dump(out, f, indent=4)


# The pass to collect node's information
# Run tools/generate_report.py to genetate report
class StatPass(PassBase):
    def __init__(self, filename, example_inputs):
        super().__init__()
        self.filename = filename
        self.example_inputs = example_inputs

    def call(self, gm: torch.fx.GraphModule):
        parse_fx_stat(gm, self.example_inputs, self.filename)
        modified = False
        return PassResult(gm, modified)
