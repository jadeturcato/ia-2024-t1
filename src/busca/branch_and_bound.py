"""Implementação do algoritmo 'branch and bound'."""


def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando Branch and Bound."""
