Known Issues
============

This document outlines the known issues present in the current release of the PyTorch 2.0 TTNN Compiler. Basically, the issues are about some specific attributes owned by a model but unable to be processed by the current compiler.

## 1. Complex dynamic shape.

While Torch Dynamo is capable of handling dynamic shapes to a certain extent — critical for models like YOLO, which require processing inputs of varying sizes — we encountered a model with dynamic shapes that our compiler was unable to handle. Without conducting a detailed investigation, the most likely cause seems to be the introduction of "complex" dynamic shape usage. Specifically, it may involve what is known as **data-dependent shapes**, where the shape of a tensor is determined not solely by the input's dimensions but also by the actual data within the input tensors.

This type of dynamic shape makes inference particularly challenging because:

* The shape cannot be determined or inferred statically before execution.
* The model needs to perform some operations, sometimes on the input data itself, to deduce the final shape.

We have a [test case](../tests/models/openpose/test_openpose.py) that reproduces this issue. The test triggers the following error message, indicating that the Dynamo backend compiler expects a `Tensor` type but encounters a `SymInt` type instead.

```
torch._dynamo.exc.BackendCompilerFailed: backend='ttnn_backend' raised:
E       RuntimeError: aten::clone() Expected a value of type 'Tensor' for argument 'self' but instead found type 'SymInt'.
E       Position: 0
E       Value: s1
E       Declaration: aten::clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor
E       Cast error details: Unable to cast s1 to Tensor
```

Why does `SymInt` remain in the model? A likely reason is that it cannot be statically determined before execution, which aligns with the concept of data-dependent shapes — where the tensor's shape is influenced by the actual data within the input, rather than just the input dimensions.

This test serves as a useful starting point for further investigation.

Also refer to [PR 132](https://github.com/tenstorrent/pytorch2.0_ttnn/pull/132)

## 2. Pipeline abstraction.

A pipeline refers to a high-level abstraction that simplifies the process of using pre-trained models. A pipeline handles the entire workflow of passing input data through the model, managing preprocessing and postprocessing steps, and returning results in a user-friendly way.

It is understandable that the current compiler does not support the entire pipeline. Traditionally, we compile the model itself but leave the pre-processing and post-processing algorithms out of the compilation process. These algorithms tend to involve more control logic and less data-parallelism, making them more suited for execution on the CPU. We have a [test case](../tests/models/autoencoder_conv/test_autoencoder_conv.py) that reproduces this issue, where the error message "unable to create tensor" appears, likely indicating that the issue occurs in the code outside of the model.

```
E               ValueError: Unable to create tensor, you should probably activate truncation and/or padding with 'padding=True' 'truncation=True' to have batched tensors with the same length. Perhaps your features (`input_ids` in this case) have excessive nesting (inputs type `list` where type `int` is expected).
```

Also refer to [PR 127](https://github.com/tenstorrent/pytorch2.0_ttnn/pull/127)
