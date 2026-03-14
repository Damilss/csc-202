from collections import defaultdict, deque

def is_two_colorable(edge_list: list[list[str]]) -> bool:
    graph = defaultdict(list)
    vertices = set()

    # Build undirected adjacency list
    for u, v in edge_list:
        graph[u].append(v)
        graph[v].append(u)
        vertices.add(u)
        vertices.add(v)

    colors = {}

    for start in vertices:
        if start in colors:
            continue

        colors[start] = 0
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[vertex]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[vertex]:
                    return False

    return True
