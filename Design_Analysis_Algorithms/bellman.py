def bellman_ford(graph, source):
    # Step 1: Initialize distances
    distances = {vertex: float("inf") for vertex in graph}
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


# Example
# graph = {"A": {"B": -1, "C": 4}, "B": {"C": 3, "D": 2, "E": 2}, "C": {}, "D": {"B": 1, "C": 5}, "E": {"D": -3}}
# source = "A"
graph = {}
while True:
    edge = input("Enter source, dest, cost - ")
    if edge.strip() == "":
        break
    temp = edge.split()
    if len(temp) == 3:
        u, v, w = temp
    elif len(temp) == 1:
        graph[temp[0]] = {}
    w = int(w)
    if u not in graph:
        graph[u] = {}
    graph[u][v] = w
print(graph)
source = input("enter source - ")

shortest_distances = bellman_ford(graph, source)
print(shortest_distances)
