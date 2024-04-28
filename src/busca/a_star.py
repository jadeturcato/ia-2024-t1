def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


def A_Star(start, goal, h, neighbors, distance):
    openSet = {start}
    cameFrom = {}
    gScore = {node: float('inf') for node in neighbors.keys()}
    gScore[start] = 0
    fScore = {node: float('inf') for node in neighbors.keys()}
    fScore[start] = h(start)

    while openSet:
        current = min(openSet, key=lambda node: fScore[node])
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in neighbors[current]:        
            tentative_gScore = gScore[current] + distance(current, neighbor)
            if tentative_gScore < gScore[neighbor]:               
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)

    return None
