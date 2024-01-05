import os
import json
import torch
from torch.fx.passes.fake_tensor_prop import FakeTensorProp
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from collections import Counter

def parse_fx_stat(gm: torch.fx.GraphModule, example_inputs, out_file):
        try:
            FakeTensorProp(gm).propagate(*example_inputs)
        except Exception as e:
            print(e)
            print("FakeTensorProp propagate failed, do nothing.")
            return
        def is_jsonable(x):
            try:
                json.dumps(x)
                return True
            except:
                return False

        out = {}
        for node in gm.graph.nodes:
            if node.op in ["call_function", "call_method"]:
                try:
                    name = str(node.target)
                except:
                    name = node.target.__name__
                out.setdefault(name, {})
                out[name].setdefault("cnt", 0)
                out[name].setdefault("args", [])
                out[name].setdefault("metas", [])
                out[name]["cnt"] += 1
                args_list = []
                for arg in node.args:
                    arg = arg if is_jsonable(arg) else f"not_jsonable:{str(arg)}"
                    args_list.append(arg)
                out[name]["args"].append(args_list)
                if 'tensor_meta' in node.meta:
                    meta = {"shape": list(node.meta['tensor_meta'].shape),
                            "dtype": str(node.meta['tensor_meta'].dtype)}
                    out[name]["metas"].append(meta)
        os.makedirs(os.path.dirname(out_file), exist_ok=True)

        try:
            with open(out_file, "w") as f:
                json.dump(out, f, indent=4)
        except Exception as e:
            print(e)

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
        out_file = os.path.join(self.out, "raw", f"{self.model_name}_{self.counter['val']}.json")
        self.counter["val"] += 1
        parse_fx_stat(gm, self.example_inputs, out_file)
        modified = False
        return PassResult(gm, modified)