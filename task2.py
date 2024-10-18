from task1 import create_graph
import networkx as nx


if __name__ == "__main__":
    G = create_graph()

    dfs_path = list(nx.dfs_tree(G, source="Барське шосe"))
    bfs_path = list(nx.bfs_tree(G, source="Барське шосe"))

    print(f"DFS path: {dfs_path} \n")
    print(f"BFS path: {bfs_path}")