import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult
from torch_ttnn.passes.lowering.add_data_move_pass import is_tt_data_move, is_tt_compute

L1_LIMIT = 1048576 # 1024 * 1024 bytes (1 MB)

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
        # TODO: What if meta of nth output of the node is requested?
        if len(node.meta["val"]) > 1:
            return node.meta["val"][0].size()
        else:
            return node.meta["val"].size()


def get_dtype(node):
    if is_tt_data_move(node):
        assert len(node.all_input_nodes) == 1, "Data movement operators can't have more than one input!"
        return get_dtype(node.all_input_nodes[0])
    else:
        # TODO: What if meta of nth output of the node is requested?
        if len(node.meta["val"]) > 1:
            return node.meta["val"][0].dtype
        else:
            return node.meta["val"].dtype

            

def is_input_tensor_on_device(node):
    # This is a data move op which propagates shape of input tensor
    if node.target == ttnn.Shape:
        return False
    if node.target is ttnn.to_device or is_tt_compute(node):
        return True
    if node.target is ttnn.from_device:
        return False
    # Considers cases like ttnn op --> to_layout
    if is_tt_data_move(node):
        return is_input_tensor_on_device(node.all_input_nodes[0])
    else:
        return False



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
    # Data points containing info of on device tensors allocation & deallocation for ttnn ops
    # Useful for visualization by plotting in a chart
    data_points = []
    # On device tensors info
    on_device_meta = []

    # Tensor IDs allocation for ttnn ops input & output
    tt_compute_count = 0
    for node in nodes:
        if is_tt_compute(node):
            tt_compute_count += 1
            # For inputs
            for input_node in node.all_input_nodes:
                if input_node not in node_to_tid_map:
                    node_to_tid_map[input_node] = last_assigned_tid
                    last_assigned_tid += 1
            # For output
            if node not in node_to_tid_map:
                node_to_tid_map[node] = last_assigned_tid
                last_assigned_tid += 1
    
    # print(f"Tensor IDs for nodes on device:")
    # for key, value in node_to_tid_map.items():
    #     print(f"Node: {key} - {value}")

    # Tracks the total compute memory of the model
    print(f"Total tt compute nodes: {tt_compute_count}")
    i = 0
    compute = 0
    overflow_ops = []

    for node in nodes:
        on_device = False
        # Has to be a ttnn op
        if is_tt_compute(node):
            print(f"tt compute node numbered: {i}")
            i += 1
            # This is for marking those ttnn ops whose execution on device takes the compute memory above the threshold.
            if compute < L1_LIMIT:
                can_mark = True
            # Exception: Full node has no input
            # Assumption: Full node outputs a tensor on device
            if node.target == ttnn.full:
                on_device = True
            total_input_size = 0
            for input_node in node.all_input_nodes:
                # If input tensor on device or coming as output from another ttnn on device op
                if is_input_tensor_on_device(input_node):
                    on_device = True
                    input_shape = get_shape(input_node)
                    input_dtype = get_dtype(input_node)
                    input_size = get_size(input_shape, input_dtype)
                    total_input_size += input_size
                    
                    assert input_node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"
                    tid = node_to_tid_map[input_node]
                    tid_to_addr_map_in_L1[tid] = last_assigned_addr
                    last_assigned_addr += input_size

                    if (tid, input_size) not in on_device_meta:
                        on_device_meta.append((tid, input_size))


            if on_device:
                output_shape = get_shape(node)
                output_dtype = get_dtype(node)
                output_size = get_size(output_shape, output_dtype)
                compute += total_input_size + output_size

                assert node in node_to_tid_map, "Tensor ID not allocated for one of the inputs!"
                tid = node_to_tid_map[node]
                tid_to_addr_map_in_L1[tid] = last_assigned_addr
                last_assigned_addr += output_size

                if (tid, output_size) not in on_device_meta:
                    on_device_meta.append((tid, output_size))

                data_points.append(on_device_meta.copy())

                if can_mark and compute >= L1_LIMIT:
                    can_mark = False
                    overflow_ops.append(node)

                print("\n---------------------------------------------------")
                print(f"op execution on device: {node.name}")
                print(f"input size: {total_input_size} bytes")
                print(f"output size: {output_size} bytes")
                print(f"total compute memory parked in L1: {compute} bytes")
                
                if is_tt_compute(node):
                    print(f"Tensor IDs existing on device after {node.name} is executed")
                    print(f"{tid_to_addr_map_in_L1}")

                # This part of code is to assess whether we can swap out output tensor from device
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

                    on_device_meta.remove((tid, output_size))
                    
                    print(f"op removed from device: {node.name}")
                    print(f"output size: {output_size} bytes")
                    print(f"total compute memory parked in L1: {compute} bytes")
                # Once current node's input & output tensor processing is over, mark it as computed
                computed_nodes.append(node)
                # Swap out input tensors from device if its usage is completed
                # i.e there are no ttnn ops on device which uses the tensor
                for input_node in node.all_input_nodes:
                    # Exception: Shape node is just like a parameter containing shape of input tensor
                    if input_node.target == ttnn.Shape:
                        continue
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

                        on_device_meta.remove((tid, input_size))

                        print(f"input tensor removed from device: {input_size} bytes")
                        print(f"total compute memory parked in L1: {compute} bytes")
                
                data_points.append(on_device_meta.copy())
    
    print(f"Tensor IDs existing on device after the model is executed:")
    print(f"{tid_to_addr_map_in_L1}")
    print(f"----------------------------------------------------------------")
    print(f"These ttnn ops overflow the L1 buffer: {overflow_ops}")
    print(f"Data captured for plotting on a chart:")
    for data in data_points:
        print(data)

    return gm


class MemoryPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        gm = memory_footprint(gm)
        return PassResult(gm, True)