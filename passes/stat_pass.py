import os
import json
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult


class StatPass(PassBase):
    def __init__(self, model_name):
        super().__init__()
        self.model_name = model_name

    def call(self, gm: torch.fx.GraphModule):
        out = {}
        for node in gm.graph.nodes:
            if node.op in ["call_function", "call_method"]:
                out.setdefault(node.target.__name__, 0)
                out[node.target.__name__] += 1
        out_folder = "stat"
        out_file = os.path.join(out_folder, f"{self.model_name}.json")
        os.makedirs(out_folder, exist_ok=True)
        with open(out_file, "w") as f:
            json.dump(out, f, indent=4)
        modified = False
        return PassResult(gm, modified)