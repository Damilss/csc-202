from collections import defaultdict


def tsort(edge_list: list[list[str]]) -> list[str]:
    """"Topological sort of DAG (directed acyclic graph) returns
    list of verticies in order"""
    stack = []
    result = []
    adj_verticies = defaultdict(list)
    in_degrees = defaultdict(int)
    verticies = set()

    # adjacant verticies and incoming degrees
    for u, v in edge_list:
        adj_verticies[u].append(v)
        in_degrees[v] += 1
        verticies.add(u)
        verticies.add(v)

    # pushing all of the 0 in-degree verticies to stack
    for vertex in verticies:
        if in_degrees[vertex] == 0:
            stack.append(vertex)

    while stack:
        vertex = stack.pop()
        result.append(vertex)

        for sub_vertex in adj_verticies[vertex]:
            in_degrees[sub_vertex] -= 1
            if in_degrees[sub_vertex] == 0:
                stack.append(sub_vertex)


    if len(result) != len(verticies):
        raise ValueError("Input contains a cycle")

    return result
