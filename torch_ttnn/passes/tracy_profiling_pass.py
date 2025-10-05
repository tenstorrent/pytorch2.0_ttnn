# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import torch
from torch.fx.passes.infra.pass_base import PassBase, PassResult
import ttnn
from torch_ttnn.utils import GraphCleanup
from torch_ttnn.utils import TtnnDevice


class TracyProfilingPass(PassBase):
    def __init__(self, enable_tracy_profiling):
        super().__init__()
        torch.fx.node.has_side_effect(ttnn.ReadDeviceProfiler)
        self.enable_tracy_profiling = enable_tracy_profiling
        # To avoid dropping profiling data, it's recommended to call ttnn.ReadDeviceProfiler every 1000 nodes or so.
        # https://github.com/tenstorrent/tt-metal/blob/5635e909b7af40a1f4ede2ffd7f4de24acc6f4b9/docs/source/ttnn/ttnn/profiling_ttnn_operations.rst
        # Configurable via this variable:
        self.dump_device_profiler_op_count = 500

    def call(self, gm: torch.fx.GraphModule):
        if self.enable_tracy_profiling:
            graph = gm.graph

            num_nodes = len(graph.nodes)
            for i, node in enumerate(graph.nodes):
                # Insert ttnn.ReadDeviceProfiler at an interval and before the last
                if i % self.dump_device_profiler_op_count == 0 or i == (num_nodes - 1):
                    with graph.inserting_before(node):
                        graph.call_function(ttnn.ReadDeviceProfiler, (TtnnDevice(),))

            GraphCleanup(gm)

        return PassResult(gm, True)
