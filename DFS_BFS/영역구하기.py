from collections import deque

M, N, K = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

q = deque()

area_ls = []

for a in range(M): # y축
    for b in range(N): # x축
        if visited[a][b] or graph[a][b] == 1:
            continue
        visited[a][b] = True
        q.append((a,b))
        cnt = 0
        while q:
            x, y = q.popleft()
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            
        area_ls.append(cnt)

area_ls.sort()
print(len(area_ls))
print(" ".join(map(str, area_ls)))