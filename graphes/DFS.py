def DFS(graph, start, visited=set()):
    visited.add(start)

    for neighor in graph[start]:
        if neighor not in visited:
            DFS(graph,neighor,visited)
    return visited