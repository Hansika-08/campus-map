"""
Route Finding & Shortest Route

Implement the logic to find the shortest path from a source to a destination.
You can use Dijkstra's Algorithm or Breadth-First Search (BFS) for this.

Example input:
    routes = ROUTES (from routes.py)
    source = "Main Gate"
    destination = "Library"

Example output:
    (["Main Gate", "CSE Block", "Library"], 200)  # (route_list, total_distance)
"""


import heapq


def find_shortest_route(routes, source, destination):
    """
    Find the shortest route from source to destination.

    Args:
        routes (dict): Graph representing locations and path distances.
        source (str): Starting location name.
        destination (str): Destination location name.

    Return:
        tuple: (route_list, total_distance)
        If no route exists, return ([], 0).
    """
    if not routes or source not in routes or destination not in routes:
        return ([], 0)

    if source == destination:
        return ([source], 0)

    # Priority queue storing (cumulative_distance, current_node, path)
    pq = [(0, source, [source])]
    min_distance = {source: 0}

    while pq:
        dist, current, path = heapq.heappop(pq)

        if current == destination:
            return (path, dist)

        if dist > min_distance.get(current, float("inf")):
            continue

        for neighbor, weight in routes.get(current, {}).items():
            new_dist = dist + weight

            if new_dist < min_distance.get(neighbor, float("inf")):
                min_distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor, path + [neighbor]))

    return ([], 0)


