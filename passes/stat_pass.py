import os
import json
import torch
from torch.fx.passes.fake_tensor_prop import FakeTensorProp
from torch.fx.passes.infra.pass_base import PassBase, PassResult

def parse_fx_stat(gm: torch.fx.GraphModule, example_inputs, out_file):
    FakeTensorProp(gm).propagate(*example_inputs)
    out = []
    for node in gm.graph.nodes:
        if node.op not in ["call_function", "call_method"]:
            continue
        node_info = {}
        # set node's op_type
        node_info["op_type"] = str(node.target)
        # set node's inputs info
        node_info["inputs"] = []
        inputs_info = node.args
        for input_info in inputs_info:
            input = {}
            # Only record if the input is torch.Tensor
            if isinstance(input_info, torch.fx.node.Node) and \
               isinstance(input_info.meta["val"], torch.Tensor):
                input["shape"] = list(input_info.meta["val"].shape)
                input["dtype"] = str(input_info.meta["val"].dtype)
            node_info["inputs"].append(input)
        # set node's outputs info
        node_info["outputs"] = []
        outputs_info = node.meta["val"]
        if isinstance(outputs_info, torch.Tensor):
            output = {"shape": list(outputs_info.shape),
                      "dtype": str(outputs_info.dtype)}
            node_info["outputs"].append(output)
        elif isinstance(outputs_info, tuple):
            for output_info in outputs_info:
                output = {}
                # some output_info is None
                if isinstance(output_info, torch.Tensor):
                    output["shape"] = list(output_info.shape)
                    output["dtype"] = str(output_info.dtype)
                node_info["outputs"].append(output)
        else:
            assert(0 and "unsupport outputs_info")
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