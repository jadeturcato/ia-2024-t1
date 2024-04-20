"""Implementação da busca em profundidade."""
from typing import List
from src.graph import Graph, Edge


def dfs(graph: Graph, start: int, goal: int):
    # assert start in graph.Node and goal in graph.Node

    number_graph_nodes_analyzed: int = 0
    length_found_path: float = 0
    path_between_start_and_goal: List[int] = []

    stack: List[List[int]] = [[start]]

    while stack:
        number_graph_nodes_analyzed += 1
        if stack[-1][-1] == goal:
            return number_graph_nodes_analyzed, 0, stack[-1]
        else:
            node = stack.pop()
            stack.extend(find_neighbor(node, graph.EdgeList))


def find_neighbor(node_list: List[int], edge_list: List[Edge]):
    node_to_analyzed: int = node_list[-1]
    new_stack: List[List[int]] = []
    for edge in edge_list:
        if node_to_analyzed == edge.Node1 and not edge.get_is_visited():
            new_stack.append(new_item_of_stack(node_list.copy(), edge.Node2))
            set_is_visited(edge_list, node_to_analyzed, edge.Node2)
        elif node_to_analyzed == edge.Node2 and not edge.get_is_visited():
            new_stack.append(new_item_of_stack(node_list.copy(), edge.Node1))
            set_is_visited(edge_list, node_to_analyzed, edge.Node1)
    return new_stack


def new_item_of_stack(node_list: List[int], new_node: int):
    node_list.append(new_node)
    return node_list


def set_is_visited(edge_list: List[Edge], starting_node: int, ending_node: int):
    edges_to_visit: List[Edge] = list(filter(lambda e: (starting_node == e.Node1 or starting_node == e.Node2) and
                                                       (ending_node == e.Node1 or ending_node == e.Node2), edge_list))
    for edge in edges_to_visit:
        edge.set_is_visited()


def get_length_path(edge_list: List[Edge], path: List[int]):
    length_path: float = 0
    for node in path:
        pass


    """Busca um caminho entre start e goal usando busca em profundidade."""
