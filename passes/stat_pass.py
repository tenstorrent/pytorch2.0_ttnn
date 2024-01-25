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
        node_info["op_type"] = str(node.target)
        output_info = node.meta["val"]
        #TODO: currently just handle the output format is instance of torch.Tensor
        if isinstance(output_info, torch.Tensor):
            output = {"shape": list(output_info.shape),
                      "dtype": str(output_info.dtype)}
            node_info["output"] = output
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