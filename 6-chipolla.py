graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 4)],
    'D': [('A', 5), ('B', 3), ('C', 4)]
}

edges = []
visited = set()

start_vertex = 'A'
visited.add(start_vertex)

while len(visited) < len(graph):
    min_edge = None

    for vertex in visited:
        for neighbor, weight in graph[vertex]:
            if neighbor not in visited:
                if min_edge is None or weight < min_edge[2]:
                    min_edge = (vertex, neighbor, weight)

    if min_edge:
        edges.append(min_edge)
        visited.add(min_edge[1])

for edge in edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
