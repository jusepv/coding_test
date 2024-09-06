from collections import deque

n, m, k, x = map(int, input().split())

data = []

for _ in range(m):
    data.append((map(int, input().split())))


graph = [[] for _ in range(n+1)]


# 그래프 정보 입력
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)


queue = deque([x])

distance = [-1] * (n+1)
distance[x] = 0

while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)



check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check == True

if check == False:
    print(-1)