from typing import List
import torch
import pickle
from pathlib import Path


# Save a pickle file from a Python object to metrics/{base_path}/{filename}.pickle
def save_pickle(obj, base_path, filename):
    p = Path(f"metrics/{base_path}")
    p.mkdir(parents=True, exist_ok=True)
    pickle_out_path = p / f"{filename}.pickle"
    with open(pickle_out_path, "wb") as f:
        pickle.dump(obj, f)


def _get_shape_from_fake_tensor(faketensor):
    if isinstance(faketensor, torch._subclasses.fake_tensor.FakeTensor):
        return list(faketensor.size())
    else:
        return faketensor


def _sanitize_value(value):
    # Put this in a map?
    if isinstance(value, int) and value == 9223372036854775807:
        return -1
    elif isinstance(value, list):
        val_list = []
        for val in value:
            if isinstance(val, torch.fx.node.Node):
                val_shape = _get_shape_from_fake_tensor(val.meta["val"])
                val_list.append(f"torch.Size({val_shape})")
            else:
                val_list.append(val)
        return val_list
    else:
        return value


class Inputs:
    def __init__(self, dtype, name, shape, value):
        self.dtype = dtype
        self.name = name
        self.shape = shape

        shape = _get_shape_from_fake_tensor(shape) if shape is not None else ""
        self.shape = f"<{str(shape)}>"

        value = _sanitize_value(value) if value is not None else "?"
        self.value = f"{str(value)}"

    def __repr__(self):
        return f"{str(self.dtype)}{self.shape} {str(self.name)} = {self.value}"


class InputVariation:
    def __init__(self, opname, inputs: List[Inputs]):
        self.opname = opname
        self.inputs = inputs

    def get_input_str_list(self):
        return [str(input) for input in self.inputs]

    def __repr__(self):
        input_str = ", ".join(self.get_input_str_list())
        return f"{self.opname}:\n\t{input_str}\n"

    def dict(self):
        return {"opname": str(self.opname), "inputs": self.get_input_str_list()}


class ConvertedInput:
    def __init__(self, opname, original_input_variation: InputVariation):
        self.opname = opname
        self.original_input_variation = original_input_variation

    def __repr__(self):
        return f"{self.opname} --> {self.original_input_variation}"

    def dict(self):
        return {"opname": str(self.opname), "original_inputs": self.original_input_variation.dict()}


def collect_input_variation(target, args, kwargs):
    """
    Collect the input variation from schema of a target function if exists

    Returns:
        InputVariation class or None
    """
    if hasattr(target, "_schema"):
        # Get schema list for this op
        schema_pos_args = [arg for arg in target._schema.arguments if not arg.kwarg_only]
        schema_kw_args = {arg.name: arg.type for arg in target._schema.arguments if arg.kwarg_only}

        # Map args with schema
        inputs = []
        for i, arg in enumerate(args):
            dtype = schema_pos_args[i].type
            name = schema_pos_args[i].name

            if isinstance(arg, torch.fx.proxy.Proxy):
                arg = arg.node

            # Collect the input shapes from the metadata if possible.
            if hasattr(arg, "meta") and "val" in arg.meta:
                shape = arg.meta["val"]
            else:
                shape = None

            # Collect the input values.
            # Unknown values will be substituted with an empty string.
            if not isinstance(arg, torch.fx.node.Node):
                value = arg
            else:
                value = None

            inputs.append(Inputs(dtype, name, shape, value))

        # Map kwargs with schema
        for name, value in kwargs.items():
            dtype = schema_kw_args[name]
            # Collect the shape of a value if it's a node
            if isinstance(value, torch.fx.node.Node):
                shape = value.meta["val"]
            else:
                shape = None
            inputs.append(Inputs(dtype, name, shape, value))

        return InputVariation(target, inputs)
    else:
        return None


def collect_input_variation_from_node(node: torch.fx.Node):
    """
    Collection input variation from a torch.fx.Node. If the node consists of a TTNN op, then
    also process the schema from the original aten op.

    Returns:
        class InputVariation or class ConvertedInput
    """
    if node.op in [
        "call_function",
        "call_method",
    ] and node.target.__name__.startswith("ttnn."):
        if hasattr(node, "meta") and "original_input_variations" in node.meta:
            original_input_variations = node.meta["original_input_variations"]
            assert isinstance(original_input_variations, InputVariation)
            return ConvertedInput(node.target.__name__, original_input_variations)
    else:
        return collect_input_variation(node.target, node.args, node.kwargs)


def collect_input_variations_from_list_nodes(nodes: List[torch.fx.Node]):
    """
    Collect all the input variations from a list of torch.fx.Nodes.

    Returns:
        List of InputVariation or ConvertedInput class objects.
    """
    collection = []
    for node in nodes:
        if (input_variations := collect_input_variation_from_node(node)) is not None:
            collection.append(input_variations)

    return collection
