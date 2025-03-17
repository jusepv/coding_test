from collections import deque

n, m, k, x = map(int, input().split())

res = []

graph = [
    [] for _ in range(n+1)
]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)


distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)


check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)