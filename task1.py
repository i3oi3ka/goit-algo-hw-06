import networkx as nx
import matplotlib.pyplot as plt


weights_1 = [3, 2, 4, 5, 2, 3]  # Ваги для зупинок лінії 1
weights_2 = [2, 3, 4, 2, 3, 4, 5, 3, 2, 4, 3, 2]  # Ваги для зупинок лінії 2
weights_4 = [2, 3, 2, 5, 3, 2, 4, 3, 3, 4, 3, 2, 3, 2, 4, 3, 3, 2, 4]  # Ваги для зупинок лінії 4

station_1 = [
    "Електромережа",
    "вул. Зодчих",
    "вул. Дачна",
    "вул. Ак. Заболотного",
    "Мед Університет",
    "Лікарня ім. Пирогова",
    "вул. Отамановського",
]

station_2 = [
    "Героїв-Пожежників",
    "вул. Стельмаха",
    "100-річчя Він. трамвая",
    "9-й мікрорайон",
    "Ринок Вишенька",
    "вул. М. Ващука",
    "Політехнічна",
    "пр. Юності",
    "пр. Космонавтів",
    "вул. 600-річчя",
    "вул. Лялі Ратушної",
    "вул. Шевченка",
]

station_4 = [
    "Барське шосe",
    "обласна дит. лікарня",
    "Технічний університет",
    "Лісопарк",
    "вул. Праведників світу",
    "Олександра Музики",
    "Палац Школярів",
    "Данила Галицького",
    "Площа Василя Стуса",
    "Площа Калічанська",
    "Майдан Небесної Сотні",
    "Пл. Ліверпуль",
    "Музей Коцюбинського",
    "Пл. Перемоги",
    "Пед. університет",
    "вул. Ак. Янгеля",
    "вул. Героїв Нацгвардії",
    "Муніципальний ринок",
    "ТЦ Епіцентр",
    "Залізничний вокзал",
]


def create_edges(graph, nodes, weights=None):
    if weights:
        for i in range(len(nodes) - 1):
            graph.add_edge(nodes[i], nodes[i + 1], weight=weights[i])
    for i in range(len(nodes) - 1):
        graph.add_edge(nodes[i], nodes[i + 1])


def create_graph():
    G = nx.Graph()
    G.add_nodes_from(station_1 + station_2 + station_4)
    create_edges(G, station_1)
    create_edges(G, station_2)
    create_edges(G, station_4)
    G.add_edge(station_2[-1], station_1[4])
    G.add_edge("вул. Отамановського", "Площа Калічанська")
    G.add_edge("Барське шосe", "Героїв-Пожежників")
    G.graph["name"] = "Vinnytsia tram"
    return G


def create_weight_graph():
    G = nx.Graph()
    G.add_nodes_from(station_1 + station_2 + station_4)
    create_edges(G, station_1, weights_1)
    create_edges(G, station_2, weights_2)
    create_edges(G, station_4, weights_4)
    G.add_edge(station_2[-1], station_1[4], weight=2)
    G.add_edge("вул. Отамановського", "Площа Калічанська", weight=2)
    G.add_edge("Барське шосe", "Героїв-Пожежників", weight=2)
    G.graph["name"] = "Vinnytsia tram"
    return G


def graph_info(graph):
    print(G)

    degree_centrality = nx.degree_centrality(G)
    print("degree_centrality")
    print(degree_centrality)
    print("=================================")

    betweenness_centrality = nx.betweenness_centrality(G)
    print("betweenness_centrality")
    print(betweenness_centrality)
    print("=================================")

    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == "__main__":
    G = create_graph()
    graph_info(G)
