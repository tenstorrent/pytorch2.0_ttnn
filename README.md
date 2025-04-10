[comment]: <> (This README.md was generated by tools/collect_metrics.py.)
[comment]: <> (Please modify docs/README.md.in and/or collect_metrics.py to make permanent changes.)

# PyTorch 2.0 TTNN Compiler
This project allows to run PyTorch code on [Tenstorrent](https://tenstorrent.com/) hardware.

## Supported Models

The table below summarizes the results of running various ML models through our TTNN compiler. For each model, we track whether the run was successful, the number of operations before and after conversion, the number of `to_device` and `from_device` operations, performance metrics, and accuracy.

| Model                                    | Status   | Torch Ops Before (Unique Ops)   | Torch Ops Remain (Unique Ops)   |   To/From Device Ops |   Original Run Time (ms) |   Compiled Run Time for 5th Iteration (ms) |   Accuracy (%) |
|:-----------------------------------------|:---------|:--------------------------------|:--------------------------------|---------------------:|-------------------------:|-------------------------------------------:|---------------:|
| [MLPMixer](<docs/models/MLPMixer>)       | ✅       | 255 (11)                        | 0 (0)                           |                    0 |                  4882.55 |                                     424.92 |          99.99 |
| [Mnist](<docs/models/Mnist>)             | ✅       | 14 (8)                          | 0 (0)                           |                    1 |                    25.25 |                                      32.05 |          99.42 |
| [Mnist-train](<docs/models/Mnist-train>) | 🚧       | 46 (15)                         | 10 (6)                          |                    0 |                  2566.95 |                                      73.94 |         100    |

### Explanation of Metrics

**Model**: Name of the model.  
**Status**: Indicates whether the model is ❌ traced / 🚧 compiled / ✅ E2E on device.  
**Torch Ops Before (Unique Ops)**: The total number of operations used by the model in the original Torch implementation. The number in parenthesis represents the total unique ops.  
**Torch Ops Remain (Unique Ops)**: The total number of operations used after conversion to TTNN. The number in parenthesis represents the total unique ops.  
**To/From Device Ops**: The number of `to/from_device` operations (data transfer to/from the device).  
**Original Run Time (ms)**: Execution time (in seconds) of the model before conversion.  
**Compiled Run Time for 5th Iteration (ms)**: Execution time (in seconds) of the model after conversion for the 5th iteration.  
**Accuracy (%)**: Model accuracy on a predefined test dataset after conversion.  

***

## Quickstart

The `torch_ttnn` module has a `backend` function, which can be used with the `torch.compile()`.

```python
import torch
import torch_ttnn

# A torch Module
class FooModule(torch.nn.Module):
    ...
# Create a module
module = FooModule()

# Compile the module, with ttnn backend
device = ttnn.open_device(device_id=0)
option = torch_ttnn.TorchTtnnOption(device=self.device)
ttnn_module = torch.compile(module, backend=torch_ttnn.backend, options=option)

# Running inference / training
ttnn_module(input_data)
```

## Tracer
The tracer dump the information of fx graph such as node's op_name and shape.

For example, you can run this script to parse the information
```
PYTHONPATH=$(pwd) python3 tools/stat_models.py --trace_orig --backward --profile
ls stat/raw
```

By default, the raw result will be stored at `stat/raw`, and you can run this script to generate the report
```
python3 tools/generate_report.py
ls stat/
```
Now the `stat/` folder have these report
 - `fw_node_count.csv`
 - `bw_node_count.csv`
 - `fw_total_input_size_dist/`
 - `bw_total_input_size_dist/`
 - `fw_total_output_size_dist/`
 - `bw_total_output_size_dist/`
 - `profile/`

The `node_count.csv` show the node with `op_type` appear in the fx graph. This report can help analyze the frequency of op type appear in the graph.

The `*_total_*_size_dist/` statistics the `op_type`'s input/output_size distribution from all fx graph recored in `stat/raw`. This report can help analyze the memory footprint durning the calculation of `op_type`.

 - Notice: the default `input_shapes` in `tools/stat_torchvision.py` is `[1,3,224,224]`, which has dependency with `*_total_*_size_dist/` report.

 - Notice: the [aten ir interface is in there](https://pytorch.org/docs/stable/torch.compiler_ir.html)

[The `profile/` is the tools provided by pytorch](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html), you can open it by the url: chrome://tracing


# For developers

## Install torch-ttnn with editable mode

During development, you may want to use the torch-ttnn package for testing.
In order to do that, you can install the torch-ttnn package in "editable"
mode with

```shell
pip install -e .
```

Now, you can utilize `torch_ttnn` in your Python code. Any modifications you make to the `torch_ttnn` package will take effect immediately, eliminating the need for constant reinstallation via pip.

## Build wheel file

For developers want to deploy the wheel, you can build the wheel file with

```shell
python -m build
```

Then you can upload the `.whl` file to the PyPI (Python Package Index).

## Run transformer models
To run transformer model with ttnn backend, run:
```
PYTHONPATH="$TT_METAL_HOME:$(pwd)" python3 tools/run_transformers.py --model "phiyodr/bert-large-finetuned-squad2" --backend torch_ttnn
```

You can also substitute the backend with `torch_stat` to run a reference comparison.

