from collections import deque
def BFS(graph, start, visited={}):
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for nei in graph[vertex]:
            if nei not in visited:
                queue.append(nei)
    return visited