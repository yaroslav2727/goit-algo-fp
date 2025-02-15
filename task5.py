import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    
def generate_color(step, total_steps):
    intensity = int(40 + (200 * step / total_steps))
    return f'#{intensity:02x}{intensity:02x}ff'

def dfs_traverse(root):
    if not root:
        return []
    
    visited = []
    stack = [(root, 0)]
    total_nodes = 0
    
    temp_stack = [(root)]
    while temp_stack:
        node = temp_stack.pop()
        total_nodes += 1
        if node.right:
            temp_stack.append(node.right)
        if node.left:
            temp_stack.append(node.left)
    
    step = 0
    while stack:
        node, level = stack.pop()
        if node not in visited:
            step += 1
            node.color = generate_color(step, total_nodes)
            visited.append(node)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
            draw_tree(root)
            plt.pause(1)
            plt.close()
    
    return visited

def bfs_traverse(root):
    if not root:
        return []
    
    visited = []
    queue = deque([(root, 0)])
    total_nodes = 0
    
    temp_queue = deque([root])
    while temp_queue:
        node = temp_queue.popleft()
        total_nodes += 1
        if node.left:
            temp_queue.append(node.left)
        if node.right:
            temp_queue.append(node.right)
    
    step = 0
    while queue:
        node, level = queue.popleft()
        if node not in visited:
            step += 1
            node.color = generate_color(step, total_nodes)
            visited.append(node)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            draw_tree(root)
            plt.pause(1)
            plt.close()
    
    return visited

def example_tree():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(16)
    return root

print("DFS Traversal displaying...")
dfs_traverse(example_tree())
plt.close()

print("BFS Traversal displaying...")
bfs_traverse(example_tree())
plt.close()