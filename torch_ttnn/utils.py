# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch


def GraphCleanup(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()

    return gm


def get_shape(gm: torch.fx.GraphModule, node_or_shape):
    """
    Get the shape of a node or shape itself.

    Args:
        gm (torch.fx.GraphModule): The GraphModule containing the node.
        node_or_shape: The node or shape to get the shape of. Can be an int, float, torch.Size, list, tuple, torch.fx.node.Node, or torch.fx.proxy.Proxy.

    Returns:
        torch.Size or None: The shape of the node or shape itself, or None if it cannot be determined.
    """
    if isinstance(node_or_shape, torch.fx.proxy.Proxy):
        node_or_shape = node_or_shape.node

    if isinstance(node_or_shape, (int, float)):
        return torch.Size()
    if isinstance(node_or_shape, (torch.Size, list, tuple)):
        return node_or_shape
    if isinstance(node_or_shape, torch.fx.node.Node):
        if (val := node_or_shape.meta.get("val", None)) is not None:
            return val.size()

        if node_or_shape.op == "get_attr":
            if gm is None:
                return None
            val = getattr(gm, node_or_shape.target)
            if isinstance(val, torch.Tensor):
                return val.size()
            if isinstance(val, (int, float)):
                return torch.Size()

    return None


def get_arg(node, index, name, default=None):
    if hasattr(node, "args") and len(node.args) > index:
        return node.args[index]
    if hasattr(node, "kwargs") and name in node.kwargs:
        return node.kwargs[name]
    return default


def get_dtype(node):
    if isinstance(node, torch.fx.node.Node):
        if (val := node.meta.get("val", None)) is not None:
            return val.dtype
    return None


def get_opname(node):
    if str(node.target).startswith("aten."):
        return str(node.target)
    elif hasattr(node.target, "__name__"):
        return node.target.__name__
    elif isinstance(node.op, str):
        return node.target
    else:
        raise


def users_have_getitem(node):
    for user in list(node.users.keys()):
        if user.op != "output" and user.op != "placeholder" and user.target.__name__ == "getitem":
            return user
    return None


def is_operation(node):
    return node.op not in ["placeholder", "output"]


# Certain ops don't support certain shapes and will emit a valid_page_size error
# RuntimeError: TT_FATAL @ ../tt_metal/impl/buffers/buffer.cpp:38: valid_page_size
# For valid non-interleaved buffers page size 2048 must equal buffer size X. For interleaved-buffers page size should be divisible by buffer size
def HasValidPageSize(shape, strict=False):
    if len(shape) >= 2 and shape[-1] > 0:
        return shape[-1] % 32 == 0 or (not strict and shape[-1] < 32)
    return False


# Ttnn globals added with torch.fx._register_custom_builtin
class TtnnDevice:
    def __repr__(self):
        return f"ttnn_Specified_Device"


class TtnnRowMajorLayout:
    def __repr__(self):
        return f"ttnn_ROW_MAJOR_LAYOUT"


class TtnnTileLayout:
    def __repr__(self):
        return f"ttnn_TILE_LAYOUT"


class TtnnInt32:
    def __repr__(self):
        return f"ttnn_int32"


class TtnnUint32:
    def __repr__(self):
        return f"ttnn_uint32"


class TtnnBfloat16:
    def __repr__(self):
        return f"ttnn_bfloat16"


class TtnnDramMemoryConfig:
    def __repr__(self):
        return f"ttnn_DRAM_MEMORY_CONFIG"


class TtnnL1MemoryConfig:
    def __repr__(self):
        return f"ttnn_L1_MEMORY_CONFIG"

class TtnnMidAccuracyComputeConfig:
    def __repr__(self):
        return f"MidAccuracyComputeConfig"

class TtnnSPDAProgramConfig:
    def __repr__(self):
        return f"SPDAProgramConfig"
