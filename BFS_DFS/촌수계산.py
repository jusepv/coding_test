n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


stack = []

def dfs(v, num):
    num += 1 
    print(v)
    visited[v] = True
    if v == b: # 확인하고자 하는 대상 = b
        stack.append(num)

    for i in graph[v]: # v는 index
        if not visited[i]: # 방문하지 않았다면 재귀적으로 다시 탐색 
            dfs(i, num)


dfs(a, 0)

if len(stack) == 0:
    print(-1)
else:
    print(stack[0]-1)