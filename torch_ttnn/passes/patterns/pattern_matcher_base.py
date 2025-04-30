# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
import ttnn
import torch
import torch._dynamo
from typing import Optional, Tuple, List, TypeVar, Generic

# Type variable for pattern matching results
# Can be a tuple of nodes, a single node, or any other pattern structure
PatternType = TypeVar('PatternType')

class PatternMatcherBase(Generic[PatternType]):
    """
    Base class for pattern matching in FX graphs.
    
    PatternType: The type of pattern this matcher returns.
                For example: Tuple[torch.fx.Node, ...] for a sequence of nodes,
                            or a custom dataclass for more structured patterns.
    """
    
    def __init__(self, gm: torch.fx.GraphModule):
        self.gm = gm

    def _is_ttnn_op(self, node: torch.fx.Node, op_type) -> bool:
        """Helper to check if a node is a specific ttnn operation."""
        return node.op == 'call_function' and node.target == op_type

    def _find_exclusive_user_of_type(self, node: torch.fx.Node, op_type) -> Optional[torch.fx.Node]:
        """
        Find a node that is exclusively consumed by a single user of the specified type.
        Also ensures the user is not ttnn.to_torch.
        
        Args:
            node: The node to check users for
            op_type: The operation type to match against
            
        Returns:
            The single user of specified type if found and exclusive, None otherwise
        """
        users = list(node.users)
        if len(users) != 1:  # Must have exactly one user
            return None
            
        user = users[0]
        if self._is_ttnn_op(user, ttnn.to_torch):  # Check not ttnn.to_torch
            return None
            
        return user if self._is_ttnn_op(user, op_type) else None

    def _find_single_user_of_type(self, node: torch.fx.Node, op_type) -> Optional[torch.fx.Node]:
        """Find a single user of the given node with the specified operation type,
        ensuring no immediate user is a ttnn.to_torch operation."""
        
        # Why not ttnn.to_torch? Simply because it breaks the tree structure of the graph.
        # if I do a replacement, let's say linear and then we have a ttnn.to_torch with one of 
        # the intermediate nodes, I need to do something fancier to avoid breaking the graph.
        # I prefer to be conservative when reducing nodes instead of adding an extra layer
        # of complexity to the pattern matcher.
        if any(self._is_ttnn_op(user, ttnn.to_torch) for user in node.users):
            return None
            
        matching_users = [user for user in node.users if self._is_ttnn_op(user, op_type)]
        return matching_users[0] if len(matching_users) == 1 else None

    def _is_node_in_args(self, target_node: torch.fx.Node, source_node: torch.fx.Node) -> bool:
        """Check if target_node is one of the arguments of source_node."""
        return target_node in source_node.args

    def _find_nodes_of_type(self, op_type) -> List[torch.fx.Node]:
        """Find all nodes of a specific operation type in the graph."""
        return [
            node for node in self.gm.graph.nodes 
            if self._is_ttnn_op(node, op_type)
        ]

    def match_pattern(self) -> List[PatternType]:
        """
        Abstract method to be implemented by subclasses.
        Should return a list of matched patterns.
        """
        raise NotImplementedError("Subclasses must implement match_pattern")

    def replace_pattern(self, matches: List[PatternType]) -> None:
        """
        Abstract method to be implemented by subclasses.
        Should implement the pattern replacement logic.
        """
        raise NotImplementedError("Subclasses must implement replace_pattern")

    def safe_remove_nodes(self, nodes: List[Optional[torch.fx.Node]]) -> None:
        """
        Remove nodes from the graph. Since ttnn.to_torch checks are handled during pattern matching,
        we can safely remove these nodes.
        
        Args:
            nodes: List of nodes to be removed (can contain None values which will be skipped)
        """

        for node in nodes:
            if node is not None:
                node.users.clear()  # Clear users to ensure clean removal
                self.gm.graph.erase_node(node)

