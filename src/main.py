"""Utilize este arquivo para depurar seus algoritmos."""

from typing import List
from graph import read_graph, Vertex
from src.busca import dfs, bfs
from src.util import reset_is_visited

if __name__ == "__main__":
    graph: List[Vertex] = read_graph("../mapas/mini_map.txt")

    # region DFS
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = dfs(graph, 0, 7)

    print("Busca em profundidade (DFS)")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion DFS

    reset_is_visited(graph)

    # region BFS
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = bfs(graph, 0, 8)

    print("\nBusca em profundidade (BFS)")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion BFS
