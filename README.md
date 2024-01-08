# `torch_ttnn` Module

The `torch_ttnn` module has a `backend` function, which can used with the `torch.compile()` function.

```python
import torch
import torch_ttnn

# A torch Module
class FooModule(torch.Module):
    ...
# Create a module
module = FooModule()
# Compile the module, with ttnn backend
ttnn_module = torch.compile(module, torch_ttnn.backend)
# Running inference
ttnn_module(input_data)
```



# Tracer
The tracer dump the information of fx graph such as node's op_name, args and shape.

For example, you can run this script to parse the information
```
PYTHONPATH=`pwd` python3 tools/stat_torchvision.py
ls stat/raw
```

By default, the result will be stored at `stat/raw`, and you can run this script to generate the report
```
python3 tools/generate_report.py
ls stat/
```
Now the `stat/` folder have these report
 - `node_count.csv`
 - `total_input_size_dist/`
 - `total_arguments/`

The `node_count.csv` show the node with `op_type` appear in the fx graph. This report can help analyze the frequency of op type appear in the graph.

The `total_input_size_dist/` statistics the `op_type`'s input_size distribution from all fx graph recored in `stat/raw`. This report can help analyze the memory footprint durning the calculation of `op_type`. Notice the default `input_shapes` in `tools/stat_torchvision.py` is `[1,3,224,224]`, which has dependency with `total_input_size_dist/` report.

The `total_arguments/` statistics the `op_type`'s argument value from all fx graph recored in `stat/raw`. For example the `aten.convolution.default.csv`

| aten.convolution.default.csv  |              |            |            |     |
| ----------------------------- | ------------ | ---------- | ---------- | --- |
| arg0's appeared value         | not_jsonable |            |            |     |
| arg0's appeared value's count | 7360         |            |            |     |
| arg3's appeared value         | "[1, 1]"     | "[14, 14]" | "[16, 16]" | ... |
| arg3's appeared value's count | 6889         | 2          | 2          |     |

According to the `stat/raw`, The `arg3` of `aten.convolution.default`
 - "[1, 1]" value appeared 6889 times
 - "[14, 14]" value appeared 2 times
 - "[16, 16]" value appeared 2 times

Seem `arg3` is the `stride` described in [there](https://pytorch.org/docs/stable/torch.compiler_ir.html#torch-compiler-ir)(There have diffcult to parse the argument name in fx), so this report show how the frequency of attribute `op_type` use

The `not_jsonable` means this argument cannot serialized in json format, most of it is the graph node, which is not the op attribute we care.
