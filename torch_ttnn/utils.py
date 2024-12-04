import torch


def GraphCleanup(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()

    return gm


def get_shape(node_or_shape):
    if isinstance(node_or_shape, (int, float)):
        return torch.Size()
    if isinstance(node_or_shape, (torch.Size, list, tuple)):
        return node_or_shape
    if isinstance(node_or_shape, torch.fx.node.Node):
        if (val := node_or_shape.meta.get("val", None)) is not None:
            return val.size()
    return None


def get_dtype(node):
    if isinstance(node, torch.fx.node.Node):
        if (val := node.meta.get("val", None)) is not None:
            return val.dtype
    return None


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


class TtnnUint32:
    def __repr__(self):
        return f"ttnn_uint32"


class TtnnBfloat16:
    def __repr__(self):
        return f"ttnn_bfloat16"


class TtnnBfloat8_B:
    def __repr__(self):
        return f"ttnn_bfloat8_b"


class TtnnDramMemoryConfig:
    def __repr__(self):
        return f"ttnn_DRAM_MEMORY_CONFIG"


class TtnnL1MemoryConfig:
    def __repr__(self):
        return f"ttnn_L1_MEMORY_CONFIG"


class TtnnCoreGrid:
    def __repr__(self):
        return f"ttnn_CORE_GRID"
