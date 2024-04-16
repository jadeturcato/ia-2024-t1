"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star


if __name__ == "__main__":
    grafo = read_graph("vertices.txt")
    caminho = a_star(grafo, 1, 100)

    print(caminho)
