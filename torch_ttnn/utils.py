import torch

def GraphCleanup(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    gm.graph.eliminate_dead_code()
    gm.graph.lint()
    gm.recompile()

    return gm

# See https://docs.google.com/document/d/1r2D4AagoeTRjEmXFnWzzafaWQkf-8hlIbX2ze-JAUFo/edit#heading=h.zad9rwqjv6cr
class DummyDevice:
    def __repr__(self):
        return f"ttnn_Specified_Device"

class DummyTtnnRowMajorLayout:
    def __repr__(self):
        return f"ttnn_ROW_MAJOR_LAYOUT"

class DummyTtnnTileLayout:
    def __repr__(self):
        return f"ttnn_TILE_LAYOUT"

class DummyTtnnUint32:
    def __repr__(self):
        return f"ttnn_uint32"

class DummyTtnnBfloat16:
    def __repr__(self):
        return f"ttnn_bfloat16"
