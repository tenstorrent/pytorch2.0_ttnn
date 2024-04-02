import torch

# Wrap functions so that they can be used in torch.fx as leaf nodes,
# and block the trace through them. See:
# https://pytorch.org/docs/stable/fx.html#torch.fx.wrap

import ttnn

# We have to create a variable for the wrapped function,
# because the `wrap` actually will try to find the target
# with "string" to find the corresponding function.
# If we register the function by `torch.fx.wrap(ttnn.add)`
# then the string been used to find the function is `add`(ya, the behavior is weird).
# But there is no variable named `add` in this file, so during compilation
# it will cause an error:
#
#       File "lib/python3.8/site-packages/torch/fx/_symbolic_trace.py", line 837, in trace
#         _patch_wrapped_functions(patcher)
#       File "lib/python3.8/site-packages/torch/fx/_symbolic_trace.py", line 1040, in _patch_wrapped_functions
#         orig_fn = frame_dict[name]
#     torch._dynamo.exc.BackendCompilerFailed: backend='compiler_fn' raised:
#     KeyError: 'add'


opnames = [
    "abs",
    "acos",
    "acosh",
    "add",
    "add_and_apply_activation",
    "add_and_apply_activation_",
    "addcdiv",
    "addcmul",
    "arange",
    "asin",
    "asinh",
    "atan",
    "atan2",
    "atanh",
    "cbrt",
    "clip",
    "clone",
    "concat",
    "cos",
    "cosh",
    "deg2rad",
    "digamma",
    "elu",
    "embedding",
    "empty",
    "eq",
    "eqz",
    "erf",
    "erfc",
    "erfinv",
    "exp",
    "exp2",
    "expm1",
    "full",
    "full_like",
    "geglu",
    "gelu",
    "gez",
    "global_avg_pool2d",
    "glu",
    "group_norm",
    "gt",
    "gte",
    "gtz",
    "hardshrink",
    "hardsigmoid",
    "hardswish",
    "hardtanh",
    "heaviside",
    "hypot",
    "i0",
    "isclose",
    "isfinite",
    "isinf",
    "isnan",
    "isneginf",
    "isposinf",
    #  "kv_cache.fill_cache_for_user_",
    #  "kv_cache.update_cache_for_token_",
    "l1_loss",
    "layer_norm",
    "ldexp",
    "leaky_relu",
    "lerp",
    "lez",
    "lgamma",
    "linear",
    "log",
    "log_sigmoid",
    "log10",
    "log1p",
    "log2",
    "logaddexp",
    "logaddexp2",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "logit",
    "lt",
    "lte",
    "ltz",
    "mac",
    "matmul",
    "max",
    "maximum",
    "MaxPool2d",
    "mean",
    "min",
    "minimum",
    "mish",
    #  "model_preprocessing.preprocess_model",
    #  "model_preprocessing.preprocess_model_parameters",
    "mse_loss",
    "mul",
    "multigammaln",
    "ne",
    "neg",
    "nextafter",
    "nez",
    "ones",
    "ones_like",
    "pad",
    "permute",
    "polygamma",
    "polyval",
    "pow",
    "prelu",
    "print_l1_buffers",
    "rad2deg",
    "reciprocal",
    "register_post_operation_hook",
    "register_pre_operation_hook",
    "reglu",
    "relu",
    "relu6",
    "repeat",
    "repeat_interleave",
    "reshape",
    "rms_norm",
    "rsqrt",
    "set_printoptions",
    "sigmoid",
    "sign",
    "signbit",
    "silu",
    "sin",
    "sinh",
    "softmax",
    "softplus",
    "softshrink",
    "softsign",
    "split",
    "sqrt",
    "square",
    "squared_difference",
    "std",
    "sub",
    "sum",
    "swiglu",
    "swish",
    "tan",
    "tanh",
    "tanhshrink",
    "threshold",
    #  "transformer.attention_softmax",
    #  "transformer.attention_softmax_",
    #  "transformer.concatenate_heads",
    #  "transformer.rotary_embedding",
    #  "transformer.split_query_key_value_and_split_heads",
    "tril",
    "triu",
    "upsample",
    "var",
    "where",
    "xlogy",
    "zeros",
    "zeros_like",
]

for opname in opnames:
    exec(f"{opname} = ttnn.{opname}")
    torch.fx.wrap(getattr(ttnn, opname))
