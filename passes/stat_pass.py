import os
import json
import torch
from torch.fx.passes.fake_tensor_prop import FakeTensorProp
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from collections import Counter

# The pass to collect node's information
# Run tools/generate_report.py to genetate report
class StatPass(PassBase):
    def __init__(self, model_name, example_inputs, counter: Counter,
                 out = os.path.join(os.getcwd(), "stat")):
        super().__init__()
        self.model_name = model_name
        self.example_inputs = example_inputs
        self.counter = counter
        self.out = out

    def call(self, gm: torch.fx.GraphModule):
        FakeTensorProp(gm).propagate(*self.example_inputs)
        out = {}
        for node in gm.graph.nodes:
            if node.op in ["call_function", "call_method"]:
                name = node.target.__name__
                out.setdefault(name, {})
                out[name].setdefault("cnt", 0)
                out[name].setdefault("metas", [])
                out[name]["cnt"] += 1
                if 'tensor_meta' in node.meta:
                    meta = {"shape": list(node.meta['tensor_meta'].shape),
                            "dtype": str(node.meta['tensor_meta'].dtype)}
                    out[name]["metas"].append(meta)
        out_folder = os.path.join(self.out, "raw")
        out_file = os.path.join(out_folder, f"{self.model_name}_{self.counter['val']}.json")
        os.makedirs(out_folder, exist_ok=True)
        with open(out_file, "w") as f:
            json.dump(out, f, indent=4)
        modified = False
        self.counter["val"] += 1
        return PassResult(gm, modified)