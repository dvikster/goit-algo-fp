import heapq
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Функція Дейкстри
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Задаємо граф з 6 вершин
graph_dict = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('F', 2)],
    'E': [('C', 5), ('F', 3)],
    'F': [('D', 2), ('E', 3)]
}

# Створення графа networkx із використанням graph_dict
G = nx.Graph()
for node, edges in graph_dict.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

# Визначення позицій для вершин (використовуючи spring_layout)
positions = nx.spring_layout(G, seed=42)

# Обчислюємо найкоротші шляхи від вершини 'A'
start_node = "A"
shortest_paths = dijkstra(G, start_node)

# Формування таблиці результатів за допомогою pandas
df_dijkstra = pd.DataFrame(list(shortest_paths.items()), columns=["Вершина", "Найкоротша відстань від A"])
df_dijkstra = df_dijkstra.sort_values(by="Найкоротша відстань від A")

# Виведення результатів у консоль
print("\nНайкоротші відстані від A до інших вершин (алгоритм Дейкстри):")
print(df_dijkstra.to_string(index=False))

# === Візуалізація графа ===
plt.figure(figsize=(10, 7))
ax = plt.gca()  # отримуємо поточні осі
nx.draw(G, positions, with_labels=True, node_color='lightblue', node_size=2000, 
        edge_color='gray', font_size=10, ax=ax)
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, font_size=8)
ax.set_title("Граф з 6 вершин")
plt.axis('off')
plt.show()
