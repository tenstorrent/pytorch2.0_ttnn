How to make an op conversion
============================
Generally speaking, there are 3 places to write code to implement and test a
lowering conversion between ops.  In this document, we take lowering from
`aten.sqrt` to `ttnn.sqrt` as an example.

- [Conversion logic](#conversion-logic)
- [Registering data movement](#registering-data-movement)
- [Unit tests](#unit-tests)

Conversion logic
----------------
The conversion logic resides in
[/torch_ttnn/passes/lowering/to_tt_pass.py](/torch_ttnn/passes/lowering/to_tt_pass.py).
There are two kinds of lowering conversions: simple and complex.

### Simple conversion
Simple conversion is a one-to-one mapping between ops.  The conversion also does
not inspect the metadata (shape and type) of the input tensors.  For example,
`aten.sqrt` to `ttnn.sqrt` is a simple conversion.  Simple conversions are
registered inside `ReplaceMoreTt.call_function`.

```py
if target == torch.ops.aten.sqrt.default:
    return self.call_function_prop_meta(ttnn.sqrt, args, kwargs)
```
https://github.com/tenstorrent/pytorch2.0_ttnn/blob/9277f6ff179deac536f1e4ccefd390ff485a4ec5/torch_ttnn/passes/lowering/to_tt_pass.py#L176-177

### Complex conversion
Most of the time, we want a simple conversion.  However, there are some cases
where a complex conversion is needed.

- When we need to inspect the metadata of the input tensors.
- When we need to create more than one op to replace the original op.
- ...

Complex conversions are registered inside the `ReplaceMoreTtManually` function.
For example, [conversion to `ttnn.clone` is
complex](https://github.com/tenstorrent/pytorch2.0_ttnn/blob/9277f6ff179deac536f1e4ccefd390ff485a4ec5/torch_ttnn/passes/lowering/to_tt_pass.py#L319).
If conversion to `ttnn.sqrt` were complex, its code would look like this:

```py
if node.target == torch.ops.aten.sqrt.default:
    new_node = g.call_function(ttnn.sqrt, args, node.kwargs)
    new_nodes.append(new_node)
```

Registering data movement
-------------------------
We should register the target op in the mega list (technically a set)
[here](https://github.com/tenstorrent/pytorch2.0_ttnn/blob/9277f6ff179deac536f1e4ccefd390ff485a4ec5/torch_ttnn/passes/lowering/add_data_move_pass.py#L142-L163).
In this example, `ttnn.sqrt` is registered through
[`TTNN_POINTWISE_UNARY_OPS`](https://github.com/tenstorrent/pytorch2.0_ttnn/blob/9277f6ff179deac536f1e4ccefd390ff485a4ec5/torch_ttnn/passes/lowering/add_data_move_pass.py#L63).

Unit tests
----------
We make a test file for a single op in
[`test/lowering/<category>/test_<op>.py`](/torch_ttnn/test/lowering/pointwise/test_sqrt.py).
Feel free to copy boilerplate code from other test files.

Sometimes, a test fails for a bug or a missing feature.  In this case, we fire a
ticket and mark the test as `xfail` in the test file.  For example, if the
`aten.sqrt` test failed, we link the issue with `xfail` like this: (`#420` as a
dummy example)

```py
@pytest.mark.xfail(reason="#420 sqrt is not implemented")
def test_sqrt():
    ...
```
