T = int(input())

def dfs(v):
    visited[v] = True # 방문 체크
    node = ls[v]
    if not visited[node]:
        dfs(node)

for _ in range(T):
    N = int(input())
    cycle = 0 
    ls = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)

    for i in range(1, N+1):
        if not visited[i]: # 방문하지 않았으면
            dfs(i)
            cycle += 1

    print(cycle)