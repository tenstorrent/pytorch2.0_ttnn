import torch
import pickle
import time
import os
from pathlib import Path


# Count the number of aten ops in the graph currently
# Returns a tuple of (total ops, total unique ops)
def count_aten_ops(nodes: list):
    aten_ops = [
        str(node.target)
        for node in nodes
        if node.op in ["call_function", "call_method"]
        and isinstance(node.target, torch._ops.OpOverload)
        and "aten" in str(node.target)
    ]
    return (len(aten_ops), len(set(aten_ops)))


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
            pos_args = [
                (str(arg.type), str(arg.name))
                for arg in node.target._schema.arguments
                if not arg.kwarg_only
            ]
            kw_args = {
                str(arg.name): str(arg.type)
                for arg in node.target._schema.arguments
                if arg.kwarg_only
            }
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
                if hasattr(arg, "meta"):
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
    return collection


def collect_input_variations_from_nodes(nodes: list):
    """Creates a dictionary of unique nodes with their schema and input variations.

    Returns:
        ```
        {
            <opname>:
            {
                'opname': str,
                'schema': {"args": list(tuple), "kwargs": list(tuple)}
                'input_shapes': list(str),
                'input_values': list(str|tuple),
            },
            <opname2>: {...},
        }
        ```

    """
    schemas = collect_schema_from_nodes(nodes)
    collection = {}
    for node in schemas:
        if "schema" in node:
            opname = node["opname"]
            input_shapes = node["input_shapes"]
            input_values = node["input_values"]
            # Create a new entry if opname has not been registered
            if opname not in collection:
                entry = {
                    "opname": opname,
                    "schema": node["schema"],
                    "input_shapes": [input_shapes],
                    "input_values": [input_values],
                }
                collection[opname] = entry
            else:
                if (
                    input_shapes not in collection[opname]["input_shapes"]
                    and input_values not in collection[opname]["input_values"]
                ):
                    collection[opname]["input_shapes"].append(input_shapes)
                    collection[opname]["input_values"].append(input_values)
    return collection


def RunTimeMetrics(path: str, prefix: str, f):
    """
    Measure the runtime of the model in seconds.
    * Exports a pickle file containing success and runtime data
    * Exports outputs in Pytorch tensor format

    Parameters:
        path (str): Typically the name of the model
        prefix (str): Either "original" or "compiled" is recommended
        f: lambda function of model run

    Example:
        output = RunTimeMetrics("BERT", "compiled", lambda: model(**inputs))

    Returns:
        Output from the model or None if model fails
    """
    p = Path(f"metrics/{path}")
    pt_out_path = p / f"{prefix}-outputs.pt"
    pickle_out_path = p / f"{prefix}-runtime_metrics.pickle"
    os.makedirs(p, exist_ok=True)
    try:
        start = time.perf_counter()
        ret = f()
        end = time.perf_counter()
        runtime_metrics = {"success": "✔️", "run_time": round(end - start, 2)}

        torch.save(ret, pt_out_path)
    except:
        runtime_metrics = {"success": "✘"}
        ret = None

    with open(pickle_out_path, "wb") as f:
        pickle.dump(runtime_metrics, f)

    return ret
