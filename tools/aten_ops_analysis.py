# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Dict, Optional, Any
from collections import Counter
from datetime import datetime
import logging
import torch

from tools.data_collection.pydantic_models import AtenOpInfo, AtenOpsSummary


def analyze_remaining_aten_ops(
    graph_nodes: List[torch.fx.Node], original_ops_count: Optional[int] = None
) -> AtenOpsSummary:
    """
    Analyze remaining aten operations in a compiled graph.

    Args:
        graph_nodes: List of nodes from the compiled graph
        original_ops_count: Optional count of original aten ops before compilation

    Returns:
        AtenOpsSummary containing detailed analysis of remaining aten ops
    """

    remaining_ops_details = []
    op_names = []

    # Analyze each node to identify remaining aten operations
    for node in graph_nodes:
        if node.op == "call_function" and "aten." in str(node.target):
            op_name = str(node.target)
            op_names.append(op_name)

            # Extract input shapes from metadata if available
            input_shapes = []
            output_shape = None

            try:
                if hasattr(node, "meta") and "val" in node.meta:
                    output_val = node.meta["val"]
                    if hasattr(output_val, "shape"):
                        output_shape = str(list(output_val.shape))

                # Try to get input shapes from args
                for arg in node.args:
                    if hasattr(arg, "meta") and "val" in arg.meta:
                        arg_val = arg.meta["val"]
                        if hasattr(arg_val, "shape"):
                            input_shapes.append(str(list(arg_val.shape)))

            except Exception as e:
                # Don't let metadata extraction failure stop the analysis
                logging.debug(f"Failed to extract metadata for node {node.name}: {e}")

            aten_op_info = AtenOpInfo(
                op_name=op_name,
                node_name=node.name,
                args_str=str(node.args),
                kwargs_str=str(node.kwargs),
                input_shapes=input_shapes,
                output_shape=output_shape,
            )
            remaining_ops_details.append(aten_op_info)

    # Generate summary statistics
    op_frequency = dict(Counter(op_names))
    total_remaining_ops = len(op_names)
    unique_op_types = len(set(op_names))

    # Get most frequent ops (top 10)
    most_frequent_ops = [op for op, _ in Counter(op_names).most_common(10)]

    # Calculate conversion percentage if original count is available
    conversion_percentage = None
    if original_ops_count is not None and original_ops_count > 0:
        conversion_percentage = ((original_ops_count - total_remaining_ops) / original_ops_count) * 100

    return AtenOpsSummary(
        total_remaining_ops=total_remaining_ops,
        unique_op_types=unique_op_types,
        op_frequency=op_frequency,
        most_frequent_ops=most_frequent_ops,
        remaining_ops_details=remaining_ops_details,
        original_ops_count=original_ops_count,
        conversion_percentage=conversion_percentage,
        compilation_timestamp=datetime.now(),
    )


def log_aten_ops_summary(summary: AtenOpsSummary, logger: logging.Logger = None) -> None:
    """
    Log a summary of remaining aten operations.

    Args:
        summary: AtenOpsSummary object containing the analysis results
        logger: Optional logger instance, uses default logging if None
    """

    if logger is None:
        logger = logging.getLogger(__name__)

    logger.info("=" * 60)
    logger.info("ATEN OPS ANALYSIS SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total remaining aten ops: {summary.total_remaining_ops}")
    logger.info(f"Unique aten op types: {summary.unique_op_types}")

    if summary.original_ops_count is not None:
        logger.info(f"Original aten ops count: {summary.original_ops_count}")
        if summary.conversion_percentage is not None:
            logger.info(f"Conversion success: {summary.conversion_percentage:.2f}%")

    if summary.most_frequent_ops:
        logger.info("Most frequent remaining aten ops:")
        for i, op in enumerate(summary.most_frequent_ops[:5], 1):
            count = summary.op_frequency[op]
            logger.info(f"  {i}. {op}: {count} occurrences")

    logger.info("=" * 60)


def count_aten_ops_in_nodes(nodes: List[torch.fx.Node]) -> int:
    """
    Count the number of aten operations in a list of nodes.

    Args:
        nodes: List of torch.fx.Node objects

    Returns:
        Number of aten operations found
    """
    count = 0
    for node in nodes:
        if node.op == "call_function" and "aten." in str(node.target):
            count += 1
    return count
