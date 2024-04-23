"""Funções auxiliares para o projeto"""

import math
from graph import Edge, Node
from typing import List


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = lat1 * math.pi / 180.0
    lat2 = lat2 * math.pi / 180.0
    # apply formulae
    a = (
        pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
        math.cos(lat1) * math.cos(lat2)
    )
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c)*1000


#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#

def find_neighbor(node_list: List[int], edge_list: List[Edge], goal: int) -> List[List[int]]:
    node_to_analyzed: int = node_list[-1]
    new_list: List[List[int]] = []
    for edge in edge_list:
        if not edge.get_is_visited() and (node_to_analyzed == edge.Node1 or node_to_analyzed == edge.Node2):
            node_to_append: int = edge.Node1 if node_to_analyzed == edge.Node2 else edge.Node2
            if goal == node_to_append:
                new_list.append(new_item_of_list(node_list.copy(), node_to_append))
                set_is_visited(edge_list, node_to_analyzed, node_to_append)
                return new_list
            else:
                new_list.append(new_item_of_list(node_list.copy(), node_to_append))
                set_is_visited(edge_list, node_to_analyzed, node_to_append)
    return new_list


def new_item_of_list(node_list: List[int], new_node: int) -> List[int]:
    node_list.append(new_node)
    return node_list


def set_is_visited(edge_list: List[Edge], starting_node: int, ending_node: int) -> None:
    edges_to_visit: List[Edge] = list(filter(lambda e: (starting_node == e.Node1 or starting_node == e.Node2) and
                                                       (ending_node == e.Node1 or ending_node == e.Node2), edge_list))
    for edge in edges_to_visit:
        edge.set_is_visited(True)


def get_length_path(node_list: List[Node], path: List[int]) -> float:
    length_path: float = 0
    for index in range(len(path) - 1):
        latitude1, longitude1 = get_lat_long(node_list, path[index])
        latitude2, longitude2 = get_lat_long(node_list, path[index + 1])
        length_path += haversine(latitude1, longitude1, latitude2, longitude2)
    return length_path


def get_lat_long(node_list: List[Node], node: int) -> (float, float):
    node: Node = list(filter(lambda e: node == e.Node, node_list))[0]
    return node.Latitude, node.Longitude


def check_if_node_is_in_graph(node_list: List[Node], node: int) -> bool:
    find_node = next(filter(lambda e: node == e.Node, node_list), None)
    return find_node is None


def reset_is_visited(edge_list: List[Edge]) -> None:
    for edge in edge_list:
        edge.set_is_visited(False)
