import uuid
import networkx as nx
import matplotlib.pyplot as plt

FIGURE_WIDTH = 8
FIGURE_HEIGHT = 5
NODE_SIZE = 2000
DEFAULT_NODE_COLOR = "lightgreen"

class Node:
    def __init__(self, key, color=DEFAULT_NODE_COLOR):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, nodes, pos, i=0, x=0, y=0, layer=1):

    if i < len(nodes):
        node = nodes[i]
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            graph.add_edge(node.id, nodes[left].id)
            add_edges(graph, nodes, pos, left, x - 1 / 2 ** layer, y - 1, layer + 1)

        if right < len(nodes):
            graph.add_edge(node.id, nodes[right].id)
            add_edges(graph, nodes, pos, right, x + 1 / 2 ** layer, y - 1, layer + 1)

    return graph


def draw_heap(list):
    heap = sorted(list, reverse=True)
    nodes = [Node(val) for val in heap]
    tree = nx.DiGraph()
    pos = {}

    tree = add_edges(tree, nodes, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=NODE_SIZE, node_color=colors)
    plt.show()


unsorted_list = [1, 5, 3, 2, 8, 7, 4, 6, 9, 10, 11, 15, 14, 12] 
draw_heap(unsorted_list)