import torch
import ttnn
from torch.fx.passes.infra.pass_base import PassBase, PassResult


def _eliminate_pair(node, func, pre_func):
    """
    Eliminate redundant pattern of paired data movement, such as from_device => to_device.
    """
    changed = False
    available_func_list = [
        ttnn.from_device,
        ttnn.to_device,
        ttnn.from_torch,
        ttnn.to_torch,
    ]
    if func not in available_func_list or pre_func not in available_func_list:
        return changed
    if len(node.users) == 0:
        return changed
    if node.op != "call_function" or node.target != func:
        return changed
    pre_node = node.args[0]
    if type(pre_node) != torch.fx.node.Node:
        return changed
    if pre_node.op != "call_function" or pre_node.target != pre_func:
        return changed
    node.replace_all_uses_with(pre_node.args[0])
    changed = True
    return changed


def _eliminate_to_copy(node):
    if node.target == torch.ops.aten._to_copy.default:
        kwargs = node.kwargs
        target_users = [user.target for user in node.users.keys()]
        if kwargs["dtype"] == torch.bfloat16 and ttnn.from_torch in target_users:
            node.replace_all_uses_with(
                node.args[0],
                delete_user_cb=lambda node: node != node.args[0],
            )
        return True
    else:
        return False


class EliminateCoreopsPass(PassBase):
    def call(self, gm: torch.fx.GraphModule):
        modified = False
        for node in gm.graph.nodes:
            modified |= _eliminate_pair(node, ttnn.to_device, ttnn.from_device)
            modified |= _eliminate_pair(node, ttnn.from_device, ttnn.to_device)
            modified |= _eliminate_pair(node, ttnn.to_torch, ttnn.from_torch)
            modified |= _eliminate_pair(node, ttnn.from_torch, ttnn.to_torch)
            modified |= _eliminate_to_copy(node)
        if modified:
            gm.graph.eliminate_dead_code()
        return PassResult(gm, modified)
