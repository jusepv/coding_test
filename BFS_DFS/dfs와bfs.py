from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        next = q.popleft()
        print(next, end=' ')
        graph[v].sort()
        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = True



dfs_visited = [False] * (N+1)
dfs(graph, V, dfs_visited)
print()
bfs_visited = [False] * (N+1)
bfs(graph, V, bfs_visited)