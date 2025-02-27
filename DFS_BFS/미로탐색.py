from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

# 거리 저장 배열 초기화
distance = [[-1 for _ in range(M)] for _ in range(N)]
distance[0][0] = 1  # 시작 위치의 거리를 1로 설정

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# BFS를 위한 큐 초기화
q = deque()
q.append((0, 0))


while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위 확인, 이동 가능 여부, 방문 여부 확인
        if 0 <= nr < N and 0 <= nc < M and miro[nr][nc] == 1 and distance[nr][nc] == -1:
            q.append((nr, nc))
            distance[nr][nc] = distance[r][c] + 1

print(distance[N - 1][M - 1])
