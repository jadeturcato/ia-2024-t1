"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph, Graph
from busca import dfs


if __name__ == "__main__":
    graph: Graph = read_graph("../mapas/mini_map.txt")
    number_graph_nodes_analyzed, length_path, path = dfs(graph, 1, 6)

    print(path)
