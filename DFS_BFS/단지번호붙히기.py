from collections import deque
import copy


N = int(input())

arr = []
for i in range(N):
    for j in range(N):
        arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque([x,y])
    arr[x][y] = 0 # 방문처리
    cnt = 1 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 집이 있으면 큐에 추가하고 방문처리
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

res = []
# 집의 좌표를 큐에 넣는다
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            res.append(bfs(i, j))

# 단지 수 출력
print(len(res))
# 집의 수를 오름차순으로 정렬하여 출력
for num in sorted(res):
    print(num)