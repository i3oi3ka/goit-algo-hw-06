from task1 import create_weight_graph
from dijkstra import dijkstra
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    G = create_weight_graph()

    shortest_paths_length = dijkstra(G, "Барське шосe")
    print(f"Найкоротший час до вершин {shortest_paths_length}\n")
    shortest_paths = nx.single_source_dijkstra_path(G, "Барське шосe")
    print(f"Найкоротший маршрут до вершин {shortest_paths}")
    
    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    