"""Implementação de uma estrutura de grafo."""


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
