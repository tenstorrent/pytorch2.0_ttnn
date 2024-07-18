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



def get_input_shape(node):
    if is_tt_data_move(node):
        assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
        return get_input_shape(node.all_input_nodes[0])
    else:
        return node.meta["val"].size()


def get_input_dtype(node):
    if is_tt_data_move(node):
        assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
        return get_input_dtype(node.all_input_nodes[0])
    else:
        return node.meta["val"].dtype



def memory_footprint(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    print("Track memory footprint for each of the ops:")
    nodes = list(gm.graph.nodes)
    # Tracks the total compute memory of the model
    compute = 0
    for node in nodes:
        on_device = False
        if is_tt_compute(node):
            input_size = 0
            for input_node in node.all_input_nodes:
                if input_node.target is ttnn.to_device:
                    on_device = True
                    input_shape = get_input_shape(input_node)
                    input_dtype = get_input_dtype(input_node)
                    input_size = input_size + get_size(input_shape, input_dtype)

            if on_device:
                output_size = get_size(
                    node.meta["val"].size(),
                    node.meta["val"].dtype
                )
                compute = compute + input_size + output_size
                print(f"op execution on device: {node.name}")
                print(f"input size: {input_size}")
                print(f"output size: {output_size}")
                print(f"total compute: {compute} bytes")

                node_users = list(node.users.keys())

                if ttnn.from_device in node_users:
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