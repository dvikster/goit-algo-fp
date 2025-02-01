import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Початковий колір (буде змінено при обході)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання ребер в граф для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол з його id, кольором та міткою
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для відображення дерева з використанням matplotlib
def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    # Отримуємо список кольорів та міток вузлів
    colors = [data['color'] for _, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    if title:
        plt.title(title)
    plt.show()

# Функція для генерації градієнтних кольорів у hex (від темного до світлого)
def generate_gradient_colors(n, start_color, end_color):
    # Видаляємо символ '#' та отримуємо значення RGB
    start_color = start_color.lstrip('#')
    end_color = end_color.lstrip('#')
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))
    colors = []
    for i in range(n):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (n - 1))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (n - 1))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (n - 1))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

# Допоміжна функція для підрахунку загальної кількості вузлів 
def count_nodes(root):
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count

# Ітеративний алгоритм обходу в глибину (DFS) з використанням стеку 
def iterative_dfs(root, start_color="#00008B", end_color="#ADD8E6"):
    total_nodes = count_nodes(root)
    colors = generate_gradient_colors(total_nodes, start_color, end_color)
    stack = [root]
    order = 0
    traversal_order = []  # Список для збереження порядку обходу
    while stack:
        node = stack.pop()
        node.color = colors[order]
        traversal_order.append(node.val)
        order += 1
        # Додаємо спочатку правого, щоб лівий оброблявся першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print("DFS traversal order:", traversal_order)
    return root

# Ітеративний алгоритм обходу в ширину (BFS) з використанням черги 
def iterative_bfs(root, start_color="#00008B", end_color="#ADD8E6"):
    total_nodes = count_nodes(root)
    colors = generate_gradient_colors(total_nodes, start_color, end_color)
    queue = deque([root])
    order = 0
    traversal_order = []  # Список для збереження порядку обходу
    while queue:
        node = queue.popleft()
        node.color = colors[order]
        traversal_order.append(node.val)
        order += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("BFS traversal order:", traversal_order)
    return root

# Створення прикладного дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в глибину (DFS) та вивід порядку обходу в консоль
print("Обхід в глибину (DFS):")
dfs_root = iterative_dfs(root, "#00008B", "#ADD8E6")
draw_tree(dfs_root, "DFS Traversal")

# Для тестування BFS створюємо нове дерево, щоб не впливали попередні зміни кольорів
root2 = Node(0)
root2.left = Node(4)
root2.left.left = Node(5)
root2.left.right = Node(10)
root2.right = Node(1)
root2.right.left = Node(3)

# Візуалізація обходу в ширину (BFS) та вивід порядку обходу в консоль
print("Обхід в ширину (BFS):")
bfs_root = iterative_bfs(root2, "#00008B", "#ADD8E6")
draw_tree(bfs_root, "BFS Traversal")
