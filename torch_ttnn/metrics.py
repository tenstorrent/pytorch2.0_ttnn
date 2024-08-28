import torch
import pickle
import time
import os
from pathlib import Path


# Save a pickle file from a Python object to metrics/{base_path}/{filename}.pickle
def save_pickle(obj, base_path, filename):
    p = Path(f"metrics/{base_path}")
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


# Save the number of to/from device ops in current graph
def count_to_from_device_ops(nodes: list):
    to_from_device_ops = [
        node.target.__name__
        for node in nodes
        if node.op in ["call_function", "call_method"]
        and ("ttnn.to" in node.target.__name__ or "ttnn.from" in node.target.__name__)
    ]
    return len(to_from_device_ops)


def collect_schema_from_nodes(nodes: list):
    """Collect a list of opname, schema, input_shapes, and input_values for all nodes.

    Returns:
        ```
        [
            {
                'opname': str,
                'schema': {"args": list(tuple), "kwargs": list(tuple)}
                'input_shapes': list(str),
                'input_values': list(str|tuple),
            },
        ]
        ```
    """
    collection = []
    for node in nodes:
        if hasattr(node.target, "_schema"):
            node_stats = {}
            # Collect the opname
            node_stats["opname"] = str(node.target)

            # Get schema from op
            pos_args = [(str(arg.type), str(arg.name)) for arg in node.target._schema.arguments if not arg.kwarg_only]
            kw_args = {str(arg.name): str(arg.type) for arg in node.target._schema.arguments if arg.kwarg_only}
            op_schema = {"args": pos_args, "kwargs": kw_args}
            node_stats["schema"] = op_schema

            arg_shapes = []
            arg_values = []
            for arg in node.args:
                # Collect the input values.
                # Unknown values will be substituted with an empty string.
                if not isinstance(arg, torch.fx.node.Node):
                    if isinstance(arg, int) and arg == 9223372036854775807:
                        arg_values.append(str(-1))
                    else:
                        arg_values.append(str(arg))
                else:
                    arg_values.append("")

                # Collect the input shapes from the metadata if possible.
                if hasattr(arg, "meta") and "val" in arg.meta:
                    arg_shapes.append(str(list(arg.meta["val"].size())))
                else:
                    arg_shapes.append("")

            # Collect any additional kwargs values if they exist
            for key, val in node.kwargs.items():
                # Can kwargs values be other nodes?
                arg_values.append((key, val))
                arg_shapes.append("")

            # Merge all the input information into a single string
            node_stats["input_shapes"] = arg_shapes
            node_stats["input_values"] = arg_values

            collection.append(node_stats)
        elif node.op in [
            "call_function",
            "call_method",
        ] and node.target.__name__.startswith("ttnn."):
            node_stats = {}
            node_stats["opname"] = node.target.__name__
            node_stats["schema"] = ""
            node_stats["input_shapes"] = ""
            node_stats["input_values"] = ""

            collection.append(node_stats)

    return collection
