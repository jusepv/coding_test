N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (N+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)