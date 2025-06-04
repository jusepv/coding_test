from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
distance  = [[-1 for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1, 1, 1,-1,-1]
dy = [1, -1, 0, 0, 1,-1, 1,-1]

q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))
            distance[i][j] =0

# bfs 수행
while q:
    x, y = q.popleft()
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<N and 0<=ny<M and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))

max_distance = max(max(row) for row in distance)

print((max_distance))
