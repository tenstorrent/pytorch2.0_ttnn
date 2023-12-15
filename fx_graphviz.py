import graphviz
import torch
import os
import math


def _tensor_weight(t):
    s = t.shape
    if s is None:
        return 1

    result = 1
    for d in s:
        if d is None:
            continue
        else:
            result *= d

    return result


def _tensor_width(t):
    w = _tensor_weight(t)
    # Strange, some tensor has 0 element
    if w <= 0:
        w = 1
    l = math.log10(w) * 2
    return max(l, 4)


def _tensor_label(t):
    return str(t.shape)


def node_name(node):
    if isinstance(node, torch.fx.node.Node):
        return hex(id(node))
    else:
        return str(node)


def node_text_const(op):
    return op.kind()

def node_label(node):
    if isinstance(node, torch.fx.node.Node):
        return str(node.op + '\n' + node.name)
    else:
        return str(node)


def from_port(from_op, it):
    port_table = [
        [],
        [''],
        [':sw', ':se'],
        [':sw', ':s', ':se'],
        [':w', ':sw', ':s', ':se'],
        [':w', ':sw', ':s', ':se', ':e'],
        [':sw', ':sw', ':s', ':s', ':se', ':se'],
    ]
    idx = list(from_op.outputs()).index(it)
    result = port_table[len(list(from_op.outputs()))][idx]
    return result

def to_port(to_op, it_idx):
    port_table = [
        [],
        [''],
        [':nw', ':ne'],
        [':nw', ':n', ':ne'],
        [':w', ':nw', ':n', ':ne'],
        [':w', ':nw', ':n', ':ne', ':e'],
        [':nw', ':nw', ':n', ':n', ':ne', ':ne'],
    ]
    result = port_table[len(list(to_op.args))][it_idx]
    return result

def to_svg(g: torch.fx.Graph, filename: str):
    # Setup dot
    dot = graphviz.Digraph()
    dot.node_attr['style'] = 'rounded,filled'
    dot.node_attr['shape'] = 'box'
    dot.node_attr['fillcolor'] = '#eeeeee'
    dot.edge_attr['color'] = '#77777777'

    # setup nodes
    map_node_idx = dict()
    map_idx_node = dict()
    for op_idx, node in enumerate(g.nodes):
        map_node_idx[node] = op_idx
        map_idx_node[op_idx] = node
        dot.node(
            node_name(node),
            label = node_label(node)
        )

    # setup edges
    edge_color_table = [
        '#77ffff77',
        '#ff77ff77',
        '#7777ff77',
        '#ff777777',
        '#77ff7777',
    ]

    for node in g.nodes:
        if node.op == 'output':
            in_nodes = node.args[0]
        else:
            in_nodes = node.args
        for idx, in_node in enumerate(in_nodes):
            edge_color = edge_color_table[(id(node) + idx) % 5]
            print(type(in_node), in_node)
            dot.edge(
                node_name(in_node),
                node_name(node) + to_port(node, idx),
                color = edge_color,
                penwidth = str(4)
            )

    # Write .dot & .svg
    dot.save(f'{filename}.dot')
    os.system(f'dot -T svg -O {filename}.dot')

