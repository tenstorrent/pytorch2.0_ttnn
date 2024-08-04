import torch


def GraphCleanup(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()

    return gm


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


class TtnnDramMemoryConfig:
    def __repr__(self):
        return f"ttnn_DRAM_MEMORY_CONFIG"


class TtnnL1MemoryConfig:
    def __repr__(self):
        return f"ttnn_L1_MEMORY_CONFIG"
