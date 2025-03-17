from collections import deque

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_region = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_rain = max(map(max, arr))

for rain in range(0, max_rain):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and not visited[i][j]: # 물에 안 잠기면
                q = deque([(i, j)])
                visited[i][j] = True
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >=N or ny < 0 or ny >= N:
                            continue
                        if not visited[nx][ny] and arr[nx][ny] > rain:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    max_region = max(cnt, max_region)

print(max_region)