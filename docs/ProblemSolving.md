# Solving Errors in Models / Ops

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
### Read he Problem
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

