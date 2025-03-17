from collections import deque
import copy


n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    # 바이러스의 좌표를 큐에 넣는다
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
		
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0: # 감염 여부
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer # 지금까지의 최대 안전 영역의 크기를 저장하는 변수
    cnt = 0 # 안전 영역의 총 개수
    for i in range(n): 
        cnt += tmp_graph[i].count(0) # 0의 개수를 센다
        answer = max(cnt, answer)


def makeWall(cnt):
	# 벽이 3개가 세어지면 바이러스를 퍼뜨려본다
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈공간이면 벽 세우기 가능
                graph[i][j] = 1
                makeWall(cnt+1) # 두번째 벽 세우러
                graph[i][j] = 0 # 다시 벽 허무는 과정 (백트레킹)

 
answer = 0
makeWall(0)
print(answer)