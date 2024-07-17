import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute

def get_size(shape, dtype):
    size = 1
    if dtype is torch.bfloat16:
        size = 2
    for val in list(shape):
        size = val * size
    return size

def memory_footprint(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    print("Track memory for each of the ops:")
    nodes = list(gm.graph.nodes)
    compute = 0
    for node in nodes:
        if node.target is ttnn.add:
            breakpoint()
        if node.target is ttnn.matmul:
            continue
        if len(node.all_input_nodes) == 1:
            if node.prev.target is ttnn.to_device:
                input_meta = node.prev.prev.prev.prev.meta
                input_shape = input_meta["val"].size()
                input_dtype = input_meta["val"].dtype
                input_size = get_size(input_shape, input_dtype)
                output_size = get_size(
                    node.meta["val"].size(),
                    node.meta["val"].dtype
                )
                compute = compute + input_size + output_size
                print(f"op execution on device: {node.name}")
                print(f"input size: {input_size}")
                print(f"output size: {output_size}")
                print(f"total compute: {compute}")

            # previous ttnn op already executed on device,
            # so its output (current node's input) will be on device
            elif is_tt_compute(node) and is_tt_compute(node.prev):
                output_size = get_size(
                    node.meta["val"].size(),
                    node.meta["val"].dtype
                )
                compute = compute + output_size
                print(f"op executed on device: {node.name}")
                print(f"output size: {output_size}")
                print(f"total compute: {compute}")
            
            if node.next.target is ttnn.from_device:
                output_size = get_size(
                    node.meta["val"].size(),
                    node.meta["val"].dtype
                )
                compute = compute - output_size
                print(f"op removed from device: {node.name}")
                print(f"output size: {output_size}")
                print(f"total compute: {compute}")
        
        elif len(node.all_input_nodes) == 2:
            input_size = 0
            for input_node in node.all_input_nodes:
                if input_node.target is ttnn.to_device:
                    input_meta = input_node.prev.prev.prev.meta
                    input_shape = input_meta["val"].size()
                    input_dtype = input_meta["val"].dtype
                    input_size = input_size + get_size(input_shape, input_dtype)

            output_size = get_size(
                node.meta["val"].size(),
                node.meta["val"].dtype
            )
            compute = compute + input_size + output_size
            print(f"op execution on device: {node.name}")
            print(f"input size: {input_size}")
            print(f"output size: {output_size}")
            print(f"total compute: {compute}")

            if node.next.target is ttnn.from_device:
                output_size = get_size(
                    node.meta["val"].size(),
                    node.meta["val"].dtype
                )
                compute = compute - output_size
                print(f"op removed from device: {node.name}")
                print(f"output size: {output_size}")
                print(f"total compute: {compute}")


    return gm


class MemoryPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        gm = memory_footprint(gm)
        return PassResult(gm, True)