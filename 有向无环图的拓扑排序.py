def topologicalsort(graph):
    indegrees = dict((i,0) for i in range(len(graph)))
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                indegrees[j] += 1 
    q = [k for k in range(len(graph)) if indegrees[k] == 0]
    res = []
    while q:
        u = q.pop()
        res.append(u)
        for v in range(len(graph[u])):
            if graph[u][v] == 1:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
    return res








graph = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0]
]

print(topologicalsort(graph))