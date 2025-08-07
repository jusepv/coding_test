from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# N = 4
# arr = [[4,3,2,1],[0,0,0,0],[0,0,9,0],[1,2,3,4]]
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[now_x][now_y] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 모든 위치까지의 최단 거리를 계산하는 함수
def bfs():
    # 초기화 (-1이면 방문 안한 상태)
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((now_x, now_y))
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and now_size>=arr[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


eat_count = 0
total_time = 0

while True:
    dist = bfs()
    min_dist = float('inf')
    min_x, min_y = N, N
    for i in range(N):
        for j in range(N):
            # 물고기가 있고, 먹을 수 있고, 도달 가능
            if arr[i][j] != 0 and arr[i][j] < now_size and dist[i][j] != -1:
                if dist[i][j] < min_dist:
                    min_x, min_y = i, j
                    min_dist = dist[i][j]
                # 거리가 같다면, 더 위쪽, 더 왼쪽 우선
                elif dist[i][j] == min_dist:
                    if i < min_x or (i==min_x and j < min_y):
                        min_x, min_y = i, j
    # 먹을 물고기가 없으면 종료
    if min_dist == float('inf'):
        break

    # 물고기 먹기
    total_time += min_dist
    arr[min_x][min_y] = 0 # 물고기 먹음
    eat_count += 1
    now_x, now_y = min_x, min_y # 상어 이동

    # 크기 증가
    if eat_count == now_size:
        now_size += 1
        eat_count = 0

print(total_time)





