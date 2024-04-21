"""Implementação da busca em profundidade."""

from src.graph import Graph
from src.util import *


def dfs(graph: Graph, start: int, goal: int) -> (int, float, [int]):
    if check_if_node_is_in_graph(graph.NodeList, start) or check_if_node_is_in_graph(graph.NodeList, goal):
        raise Exception("Os valores start e/ou goal não existem no grafo")

    number_graph_nodes_analyzed: int = 0
    stack: List[List[int]] = [[start]]

    while stack:
        number_graph_nodes_analyzed += 1
        if stack[-1][-1] == goal:
            path_between_start_and_goal = stack[-1]
            length_found_path = get_length_path(graph.NodeList, path_between_start_and_goal)
            return number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal
        else:
            node = stack.pop()
            stack.extend(find_neighbor(node, graph.EdgeList, goal))

"""Busca um caminho entre start e goal usando busca em profundidade"""
