# Solving Errors in Models / Operations

## Prerequisites
### Know
* TT-NN operations and their Python bindings are located here <br>
https://github.com/tenstorrent/tt-metal/tree/main/ttnn/cpp/ttnn/operations
*  The TT-Metal repository contains numerous examples of TT-NN operations usage in Tests and Models.

### Don't be scared
Search across the two main repositories 
* https://github.com/tenstorrent/tt-metal/
* https://github.com/tenstorrent/pytorch2.0_ttnn


## Incompatible Function Arguments
If you see an error in the test output like this:
```
ERROR tests/models/bert/test_bert.py::test_bert - TypeError: __call__(): incompatible function arguments. The following argument types are supported:
```
### Read the Problem
Examine the log above the error message. It includes detailed information, for example:
```
self = FastOperation(python_fully_qualified_name='ttnn.clone', function=<ttnn._ttnn.operations.data_movement.clone_t object a...<function default_postprocess_golden_function_outputs at 0x7f31a9cf7a60>, is_cpp_operation=True, is_experimental=False)
function_args = (ttnn.Tensor(<buffer is not allocated>, shape=Shape([1, 256, 1024]), dtype=DataType::BFLOAT16, layout=Layout::TILE), M...y_layout=TensorMemoryLayout::INTERLEAVED,buffer_type=BufferType::DRAM,shard_spec=std::nullopt), <DataType.BFLOAT16: 0>)
function_kwargs = {}

    def __call__(self, *function_args, **function_kwargs):
>       return self.function(*function_args, **function_kwargs)
E       TypeError: __call__(): incompatible function arguments. The following argument types are supported:
E           1. (self: ttnn._ttnn.operations.data_movement.clone_t, input_tensor: ttnn._ttnn.deprecated.tensor.Tensor, *, memory_config: Optional[ttnn._ttnn.deprecated.tensor.MemoryConfig] = None, dtype: Optional[ttnn._ttnn.deprecated.tensor.DataType] = None, queue_id: int = 0) -> ttnn._ttnn.deprecated.tensor.Tensor
E       
E       Invoked with: <ttnn._ttnn.operations.data_movement.clone_t object at 0x7f31af42ab30>, ttnn.Tensor([[[-0.34961, -0.03809,  ...,  0.36914, -0.18652],
E                     [-0.21777,  0.32422,  ...,  0.11426,  0.03149],
E                     ...,
E                     [-0.40820, -0.60938,  ..., -0.25586, -0.25391],
E                     [-0.21777,  0.24902,  ...,  0.48047, -0.15137]]], shape=Shape([1, 256, 1024]), dtype=DataType::BFLOAT16, layout=Layout::TILE), MemoryConfig(memory_layout=TensorMemoryLayout::INTERLEAVED,buffer_type=BufferType::DRAM,shard_spec=std::nullopt), <DataType.BFLOAT16: 0>
E       
E       Did you forget to `#include <pybind11/stl.h>`? Or <pybind11/complex.h>,
E       <pybind11/functional.h>, <pybind11/chrono.h>, etc. Some automatic
E       conversions are optional and require extra headers to be included
E       when compiling your pybind11 module.

../tt-metal/ttnn/ttnn/decorators.py:327: TypeError
```

The first part with `self = FastOperation` indicates which operation the compiler tried to call, in this case, `ttnn.clone`. The log specifies how it was called:
```
ttnn.clone(ttnn.Tensor([1, 256, 1024], bfloat16, tile), MemoryConfig, bfloat16)
```

### Finding the cause
Now, compare with the Python binding for `ttnn.clone` in TT-Metal:
https://github.com/tenstorrent/tt-metal/blob/main/ttnn/cpp/ttnn/operations/data_movement/copy/copy_pybind.cpp#L93-L110
```
bind_registered_operation(
    module,
    ttnn::clone,
    doc,
    ttnn::pybind_overload_t{
        [] (const decltype(ttnn::clone)& self,
            const ttnn::Tensor& input_tensor,
            const std::optional<ttnn::MemoryConfig> &memory_config,
            const std::optional<const ttnn::DataType> dtype,
            uint8_t queue_id) {
                return self(queue_id, input_tensor, memory_config, dtype);
            },
            py::arg("input_tensor").noconvert(),
            py::kw_only(), <<<<<<<<-----------------------
            py::arg("memory_config") = std::nullopt,
            py::arg("dtype") = std::nullopt,
            py::arg("queue_id") = 0}
);
```
Notice the `py::kw_only()` call, which separates positional and keyword-only arguments in the binding.

Next, check how `ttnn.clone` is used in the TT-Metal tests/models:
https://github.com/search?q=repo%3Atenstorrent%2Ftt-metal%20ttnn.clone&type=code
Here is a sample search result
```
if tt_tensors_device.layout == ttnn.TILE_LAYOUT:
    # Convert to bfloat16 to ensure untilize works
    if tt_tensors_device.dtype != ttnn.bfloat16:
        tt_tensors_device = ttnn.clone(
            tt_tensors_device, dtype=ttnn.bfloat16, memory_config=ttnn.DRAM_MEMORY_CONFIG
        )    
```

### Fix
Find where the lowering for the given operation is located and ensure that the arguments match the expected signature. 
In this case, make sure that memory_config and dtype are passed as keyword arguments.

## Backend Compiler Failure

If you see an error similar to the following:

```
E                   torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
E                   Exception: An error occurred when running the 'ToTtPass' pass after the following passes: []

../tt-metal/python_env/lib/python3.8/site-packages/torch/fx/passes/infra/pass_manager.py:296: BackendCompilerFailed
```

### Debugging steps
Run the test again but include `--trace`.


Take note of the source file and line number where `BackendCompilerFailed` happened in the error above. Set a breakpoint there:

```
(Pdb) b ../tt-metal/python_env/lib/python3.8/site-packages/torch/fx/passes/infra/pass_manager.py:296
```
***
```
Breakpoint 1 at /home/ubuntu/repo/tt-metal/build/python_env/lib/python3.8/site-packages/torch/fx/passes/infra/pass_manager.py:296
```

Run the test and wait for the breakpoint to be hit:
```
(Pdb) r
```
***
```
> /home/ubuntu/repo/tt-metal/build/python_env/lib/python3.8/site-packages/torch/fx/passes/infra/pass_manager.py(296)__call__()
-> raise Exception(msg) from e
```

Run interactive mode:
```
(Pdb) interact
```
***
```
*interactive*
```
Retrieve the source of the error:
```
>>> import pdb
>>> pdb.post_mortem(e.__traceback__)
```
***
```
> /home/ubuntu/repo/tt-metal/build/python_env/lib/python3.8/site-packages/torch/fx/node.py(98)_get_qualified_name()
-> raise RuntimeError("Unable to represent lambda") from e
```

## Mismatch Between Torch and TT-NN Tensor Types
If you see the following error:

```
E           TypeError: conv2d(): incompatible function arguments. The following argument types are supported:
```
### Read the Problem
Examine the full error message:

```
E               1. (*, input_tensor: tt_lib.tensor.Tensor, weight_tensor: tt_lib.tensor.Tensor, device: tt_lib.device.Device, in_channels: int, out_channels: int, batch_size: int, input_height: int, input_width: int, kernel_size: List[int[2]], stride: List[int[2]], padding: List[int[2]], dilation: List[int[2]], groups: int, bias_tensor: Optional[tt_lib.tensor.Tensor] = None, conv_config: Optional[ttnn::operations::conv2d::Conv2dConfig] = None) -> Tuple[tt_lib.tensor.Tensor, int, int, tt_lib.tensor.Tensor, Optional[tt_lib.tensor.Tensor]]
E
E           Invoked with: kwargs: input_tensor=tensor([[[[0.0781, 0.5547, 0.9531, 0.1797, 0.0039],
E                     [0.1055, 0.0312, 0.2148, 0.6719, 0.3086],
E                     [0.4609, 0.9062, 0.0000, 0.1680, 0.6328],
E                     [0.3594, 0.6914, 0.4883, 0.4961, 0.0898],
E                     [0.4766, 0.7266, 0.4219, 0.8672, 0.5352]],
E
E                    [[0.6133, 0.0898, 0.7812, 0.4453, 0.0273],
E                     [0.2148, 0.4375, 0.6523, 0.4375, 0.9805],
E                     [0.9766, 0.2773, 0.0430, 0.5625, 0.8867],
E                     [0.7227, 0.1562, 0.1289, 0.3438, 0.7617],
E                     [0.3555, 0.9648, 0.9453, 0.5547, 0.5117]]]], dtype=torch.bfloat16), ...

../tt-metal/ttnn/ttnn/operations/conv2d.py:448: TypeError
```

You can see that the `input_tensor` parameter expects a `tt_lib.tensor.Tensor` type, but is invoked with `input_tensor=tensor(..., dtype=torch.bfloat16)`. In other words, a `torch.Tensor` object is passed to `input_tensor` instead of a `ttnn.Tensor`.

### Fix
This usually happens because a `ttnn.from_torch` was not inserted for this particular argument. The logic to insert this is mostly under the [AddDataMovePass](https://github.com/tenstorrent/pytorch2.0_ttnn/blob/main/torch_ttnn/passes/lowering/add_data_move_pass.py).


# Mismatch between values
If the model has a very low accuracy score and you want to be able to narrow down the Aten-TTNN op pair that produced low accuracy, you can run pytest with `--export_code` to export a self-contained python script containing the graph and input data. This script will compare each original aten op and the corresponding TTNN op and report the first pair that has an accuracy score below a threshold. The scripts and input files can be found under `tests/autogen_accuracy_tests`.

For example:
```
pytest tests/models/mobilenet_ssd/test_mobilenet_ssd.py --export_code
python3 tests/autogen_accuracy_tests/MobileNetSSD_code.py
```

Output:
```
Traceback (most recent call last):
  File "MobileNetSSD_code.py", line 5650, in <module>
    forward(*inputs)
  File "MobileNetSSD_code.py", line 1347, in forward
    test_accuracy(mean, ttnn_mean)
  File "MobileNetSSD_code.py", line 225, in test_accuracy
    assert_with_pcc(expected, actual, pcc = 0.90)
  File "MobileNetSSD_code.py", line 218, in assert_with_pcc
    assert pcc_passed, construct_pcc_assert_message(pcc_message, expected_pytorch_result, actual_pytorch_result)
AssertionError: 0.7265316050734197
```

We can see that on line 1347 that the `ttnn.mean` op is reporting an accuracy of only 0.72. We can use this information to debug further.
