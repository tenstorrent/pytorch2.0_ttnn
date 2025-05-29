# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
import ttnn
from torch_ttnn.utils import GraphCleanup
from torch_ttnn.utils import TtnnDevice

class TracyProfilingPass(PassBase):
    def __init__(self):
        super().__init__()
        torch.fx.node.has_side_effect(ttnn.DumpDeviceProfiler)

    def call(self, gm: torch.fx.GraphModule):
        graph = gm.graph

        num_nodes = len(graph.nodes)
        for i, node in enumerate(graph.nodes):
            # Insert ttnn.DumpDeviceProfiler every 500 nodes and before the last
            if i % 500 == 0 or i == (num_nodes - 1):
                with graph.inserting_before(node):
                    graph.call_function(ttnn.DumpDeviceProfiler, (TtnnDevice(),))
                    
        GraphCleanup(gm)

        return PassResult(gm, True)
