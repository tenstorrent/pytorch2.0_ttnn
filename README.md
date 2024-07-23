[comment]: <> (This README.md was generated by tools/collect_metrics.py.)
[comment]: <> (Please modify docs/README.md.in and/or collect_metrics.py to make permanent changes.)

# PyTorch 2.0 TTNN Compiler
This project allows to run PyTorch code on [Tenstorrent](https://tenstorrent.com/) hardware.

## Supported Models

The table below summarizes the results of running various ML models through our TTNN compiler. For each model, we track whether the run was successful, the number of operations before and after conversion, the number of `to_device` and `from_device` operations, performance metrics, and accuracy.

| Model                               | Run Success   | Torch Ops Before (Unique Ops)   | Torch Ops Remain (Unique Ops)   | To/From Device Ops   |   Original Run Time (s) | Compiled Run Time(s)   | Accuracy   |
|:------------------------------------|:--------------|:--------------------------------|:--------------------------------|:---------------------|------------------------:|:-----------------------|:-----------|
| [Mnist (Eval)](tests/models/mnist)  | ✘             | 14 (8)                          | 5 (4)                           | 12                   |                    0.01 | N/A                    | N/A        |
| [Mnist (Train)](tests/models/mnist) | ✅            | 14 (8)                          | 7 (5)                           | 14                   |                    0.01 | 2.52                   | 0.64       |
| [ResNet18](tests/models/resnet)     | ✅            | 70 (9)                          | 42 (4)                          | 42                   |                    1.78 | 9.46                   | 1.0        |
| [Bloom](tests/models/bloom)         | ✘             | N/A                             | N/A                             | N/A                  |                    5.58 | N/A                    | N/A        |
| [YOLOS](tests/models/yolos)         | ✘             | N/A                             | N/A                             | N/A                  |                    0.18 | N/A                    | N/A        |
| [Llama](tests/models/llama)         | ✘             | 3 (3)                           | 1 (1)                           | 5                    |                   38.21 | N/A                    | N/A        |
| [BERT](tests/models/bert)           | ✅            | 1393 (21)                       | 489 (4)                         | 1340                 |                   62    | 36.17                  | 0.99       |
| [Falcon](tests/models/falcon)       | ✘             | 3 (3)                           | 1 (1)                           | 5                    |                   34.81 | N/A                    | N/A        |
| [GPT-2](tests/models/gpt2)          | ✘             | N/A                             | N/A                             | N/A                  |                    1.04 | N/A                    | N/A        |

### Explanation of Metrics

**Model**: Name of the model.  
**Run Success**: Indicates whether the model runs successfully after conversion.  
**Torch Ops Before (Unique Ops)**: The total number of operations used by the model in the original Torch implementation. The number in parenthesis represents the total unique ops.  
**Torch Ops Remain (Unique Ops)**: The total number of operations used after conversion to TTNN. The number in parenthesis represents the total unique ops.  
**To/From Device Ops**: The number of `to/from_device` operations (data transfer to/from the device).  
**Original Run Time (s)**: Execution time (in seconds) of the model before conversion.  
**Compiled Run Time(s)**: Execution time (in seconds) of the model after conversion.  
**Accuracy**: Model accuracy on a predefined test dataset after conversion.  
***
**NOTE:** The total number of ops currently reflect only the first graph of a model. This will be fixed in a future update to include all graphs.  

***

### Op conversion status per model

#### Mnist (Eval)
| aten ops                             | status   |   count |
|:-------------------------------------|:---------|--------:|
| aten._log_softmax.default            | ✘        |       1 |
| aten.addmm.default                   | ✅       |       2 |
| aten.clone.default                   | ✅       |       2 |
| aten.convolution.default             | ✘        |       2 |
| aten.max_pool2d_with_indices.default | ✘        |       1 |
| aten.relu.default                    | ✅       |       3 |
| aten.t.default                       | ✅       |       2 |
| aten.view.default                    | ✘        |       1 |
#### Mnist (Train)
| aten ops                             | status   |   count |
|:-------------------------------------|:---------|--------:|
| aten._log_softmax.default            | ✘        |       1 |
| aten.addmm.default                   | ✅       |       2 |
| aten.convolution.default             | ✘        |       2 |
| aten.max_pool2d_with_indices.default | ✘        |       1 |
| aten.native_dropout.default          | ✘        |       2 |
| aten.relu.default                    | ✅       |       3 |
| aten.t.default                       | ✅       |       2 |
| aten.view.default                    | ✘        |       1 |
#### ResNet18
| aten ops                                          | status   |   count |
|:--------------------------------------------------|:---------|--------:|
| aten._native_batch_norm_legit_no_training.default | ✘        |      20 |
| aten.add.Tensor                                   | ✅       |       8 |
| aten.addmm.default                                | ✅       |       1 |
| aten.convolution.default                          | ✘        |      20 |
| aten.max_pool2d_with_indices.default              | ✘        |       1 |
| aten.mean.dim                                     | ✅       |       1 |
| aten.relu.default                                 | ✅       |      17 |
| aten.t.default                                    | ✅       |       1 |
| aten.view.default                                 | ✘        |       1 |
#### Llama
| aten ops               | status   |   count |
|:-----------------------|:---------|--------:|
| aten.arange.start      | ✘        |       1 |
| aten.embedding.default | ✅       |       1 |
| aten.unsqueeze.default | ✅       |       1 |
#### BERT
| aten ops                       | status   |   count |
|:-------------------------------|:---------|--------:|
| aten._softmax.default          | ✅       |      24 |
| aten._to_copy.default          | ✅       |       1 |
| aten.add.Tensor                | ✅       |      74 |
| aten.addmm.default             | ✅       |     145 |
| aten.bmm.default               | ✅       |      48 |
| aten.clone.default             | ✅       |      99 |
| aten.div.Tensor                | ✅       |      24 |
| aten.embedding.default         | ✅       |       3 |
| aten.expand.default            | ✅       |      96 |
| aten.gelu.default              | ✅       |      24 |
| aten.mul.Tensor                | ✅       |       1 |
| aten.native_layer_norm.default | ✅       |      49 |
| aten.permute.default           | ✅       |      96 |
| aten.rsub.Scalar               | ✅       |       1 |
| aten.slice.Tensor              | ✘        |       4 |
| aten.split.Tensor              | ✘        |       1 |
| aten.squeeze.dim               | ✘        |       2 |
| aten.t.default                 | ✅       |     145 |
| aten.transpose.int             | ✅       |      24 |
| aten.unsqueeze.default         | ✅       |       2 |
| aten.view.default              | ✘        |     530 |
#### Falcon
| aten ops               | status   |   count |
|:-----------------------|:---------|--------:|
| aten.arange.start      | ✘        |       1 |
| aten.embedding.default | ✅       |       1 |
| aten.unsqueeze.default | ✅       |       1 |


## Quickstart

The `torch_ttnn` module has a `backend` function, which can be used with the `torch.compile()`.

```python
import torch
import torch_ttnn

# A torch Module
class FooModule(torch.Module):
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
PYTHONPATH=$(pwd) python3 tools/run_torchvision.py --backend torch_stat --backward --profile
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

## Run transformer models
To run transformer model with ttnn backend, run:
```
PYTHONPATH=${TT_METAL_HOME}:$(pwd) python3 tools/run_transformers.py --model "phiyodr/bert-large-finetuned-squad2" --backend torch_ttnn
```

You can also substitute the backend with `torch_stat` to run a reference comparison.

