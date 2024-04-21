"""Implementação de uma estrutura de grafo."""

from typing import List


class Graph:
    def __init__(self):
        self.NodeList: List[Node] = []
        self.EdgeList: List[Edge] = []


class Node:
    def __init__(self, node: int, latitude: float, longitude: float):
        self.Node: int = node
        self.Latitude: float = latitude
        self.Longitude: float = longitude


class Edge:
    def __init__(self, node1: int, node2: int, cost: float):
        self.Node1: int = node1
        self.Node2: int = node2
        self.Cost: float = cost
        self.IsVisited: bool = False

    def set_is_visited(self, is_visited: bool):
        self.IsVisited = is_visited

    def get_is_visited(self):
        return self.IsVisited


def read_graph(filename: str):
    graph: Graph = Graph()
    with open(filename, "rt") as input_file:
        node_count: int = int(input_file.readline().strip())
        for _ in range(node_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph.NodeList.append(Node(int(index), float(latitude), float(longitude)))

        edge_count: int = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = input_file.readline().strip().split()
            graph.EdgeList.append(Edge(int(from_vertex), int(to_vertex), float(cost)))
    return graph

