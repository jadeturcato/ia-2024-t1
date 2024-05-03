"""Implementação do algoritmo A*."""

from typing import List, Dict

class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def a_star(graph, start, goal):
    frontier = [(0, start)]  
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        frontier.sort()  
        _, current = frontier.pop(0)  

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return len(came_from), cost_so_far[goal], path

        for next_node in neighbors(graph, current):  
            new_cost = cost_so_far[current] + graph_cost(graph, current, next_node)
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + manhattan(goal, next_node)
                frontier.append((priority, next_node))  
                came_from[next_node] = current

    return None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def manhattan(a, b):
    return abs(a.lat - b.lat) + abs(a.lon - b.lon)

def neighbors(graph, node):
    return graph[node]

def graph_cost(graph, node_a, node_b):
    return graph[node_a][node_b]  
