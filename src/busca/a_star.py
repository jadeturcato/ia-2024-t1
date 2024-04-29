from typing import Dict, List, Tuple

def a_star(graph: Dict[int, List[int]], start: int, goal: int) -> Tuple[int, float, List[int]]:

     def reconstruct_path(cameFrom, current):
         total_path = [current]
         while current in cameFrom:
            current = cameFrom[current]
            total_path.insert(0, current)
         return total_path


def a_star(start, goal, neighbors, distance, h):
    openSet = {start}
    cameFrom = {}
    gScore = {node: float('inf') for node in neighbors.keys()}
    gScore[start] = 0
    fScore = {node: float('inf') for node in neighbors.keys()}
    fScore[start] = h(start)
    analyzed_nodes = 0

    while openSet:
      analyzed_nodes  += 1
      current = None
      min_fScore = float('inf')
      for node in openSet:
          if fScore[node] < min_fScore:
              min_fScore = fScore[node]
              current = node
            
      if current == goal:
          path = reconstruct_path(cameFrom, current)
          return analyzed_nodes , gScore [goal], path

      openSet.remove(current)
      for neighbor in neighbors[current]:        
          tentative_gScore = gScore[current] + distance(current, neighbor)
          if tentative_gScore < gScore[neighbor]:               
              cameFrom[neighbor] = current
              gScore[neighbor] = tentative_gScore
              fScore[neighbor] = tentative_gScore + h(neighbor)
              if neighbor not in openSet:
                  openSet.add(neighbor)

    return analyzed_nodes, float('inf'), None
