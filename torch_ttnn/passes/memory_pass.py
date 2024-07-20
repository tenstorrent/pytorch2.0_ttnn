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



def get_shape(node):
    if is_tt_data_move(node):
        assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
        return get_shape(node.all_input_nodes[0])
    else:
        return node.meta["val"].size()


def get_dtype(node):
    if is_tt_data_move(node):
        assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
        return get_dtype(node.all_input_nodes[0])
    else:
        return node.meta["val"].dtype

            

def memory_footprint(gm: torch.fx.GraphModule) -> torch.fx.GraphModule:
    print("Track memory footprint for each of the ops:")
    nodes = list(gm.graph.nodes)

    # Each node's output tensor will be assigned a unique tensor ID
    node_to_tid_map = {}
    # Tensor ID to address map
    tid_to_addr_map_in_L1 = {}
    # Tensor ID allocation tracker
    last_assigned_tid = 0
    # Memory address allocation tracker
    last_assigned_addr = 0
    # List of already executed nodes on device
    computed_nodes = []

    # Tensor IDs allocation for ttnn ops input & output
    for node in nodes:
        if is_tt_compute(node):
            # For inputs
            for input_node in node.all_input_nodes:
                if input_node not in node_to_tid_map:
                    node_to_tid_map[input_node] = last_assigned_tid
                    last_assigned_tid += 1
            # For output
            if node not in node_to_tid_map:
                node_to_tid_map[node] = last_assigned_tid
                last_assigned_tid += 1
    
    print(f"Tensor IDs for nodes on device:\n{node_to_tid_map}")

    # Tracks the total compute memory of the model
    compute = 0
    
    for node in nodes:
        on_device = False
        # Has to be a ttnn op
        if is_tt_compute(node):
            total_input_size = 0
            for input_node in node.all_input_nodes:
                # If input tensor on device or coming as output from another ttnn on device op
                if input_node.target is ttnn.to_device or is_tt_compute(input_node):
                    on_device = True
                    input_shape = get_shape(input_node)
                    input_dtype = get_dtype(input_node)
                    input_size = get_size(input_shape, input_dtype)
                    total_input_size += input_size
                    
                    assert input_node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"
                    tid = node_to_tid_map[input_node]
                    tid_to_addr_map_in_L1[tid] = last_assigned_addr
                    last_assigned_addr += input_size


            if on_device:
                output_shape = get_shape(node)
                output_dtype = get_dtype(node)
                output_size = get_size(output_shape, output_dtype)
                compute += total_input_size + output_size

                assert node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"
                tid = node_to_tid_map[node]
                tid_to_addr_map_in_L1[tid] = last_assigned_addr
                last_assigned_addr += output_size

                print("\n---------------------------------------------------")
                print(f"op execution on device: {node.name}")
                print(f"input size: {total_input_size} bytes")
                print(f"output size: {output_size} bytes")
                print(f"total compute memory parked in L1: {compute} bytes")
                
                if is_tt_compute(node):
                    print(f"Tensor IDs existing on device after {node.name} is executed")
                    print(f"{tid_to_addr_map_in_L1}")

                node_users = list(node.users.keys())
                # Are any users of current node a ttnn op?
                is_follow_up_tt_compute = False
                 # Is from device op a user of the node?
                is_follow_up_from_device = False
                for user in node_users:
                    if is_tt_compute(user):
                        is_follow_up_tt_compute = True
                    if user.target == ttnn.from_device:
                        is_follow_up_from_device = True
  
                # If no follow up ttnn op using the output of current node
                # and if one of the users is a from device operation,
                # then swap out output tensor from device
                if not is_follow_up_tt_compute and is_follow_up_from_device:
                    compute = compute - output_size
                    tid_to_addr_map_in_L1.pop(tid)
                    last_assigned_addr -= output_size
                    
                    print(f"op removed from device: {node.name}")
                    print(f"output size: {output_size} bytes")
                    print(f"total compute memory parked in L1: {compute} bytes")
                # Once current node's input & output tensor processing is over, mark it as computed
                computed_nodes.append(node)

                # Swap out input tensors from device if its usage is completed
                # i.e there are no ttnn ops on device which uses the tensor
                for input_node in node.all_input_nodes:
                    keep_on_device = False
                    input_node_users = list(input_node.users.keys())
                    for user in input_node_users:
                        if user not in computed_nodes and is_tt_compute(user):
                            keep_on_device = True
                    if keep_on_device is False:
                        input_size = get_size(
                            get_shape(input_node),
                            get_dtype(input_node)
                        )
                        compute -= input_size
                        tid = node_to_tid_map[input_node]
                        tid_to_addr_map_in_L1.pop(tid)
                        last_assigned_addr -= input_size

                        print(f"input tensor removed from device: {input_size} bytes")
                        print(f"total compute memory parked in L1: {compute} bytes")
    
    print(f"Tensor IDs existing on device after the model is executed:")
    print(f"{tid_to_addr_map_in_L1}")


    return gm


class MemoryPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        gm = memory_footprint(gm)
        return PassResult(gm, True)