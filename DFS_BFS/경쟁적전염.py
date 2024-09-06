from collections import deque
n, k = map(int, input().split())

graph = []
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0: # 해당 좌표에 바이러스가 존재하는 경우
            data.append((graph[i][j], 0, i, j))
    
target_s, target_x, target_y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

data.sort() # 낮은 번호의 바이러스부터 증식하므로
queue = deque(data)

while queue:
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0: # 감염여부
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))
    
print(graph[target_x-1][target_y-1])