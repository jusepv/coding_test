from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

pic_ls = []
for row in range(n):
    for col in range(m):
        if not visited[row][col] and graph[row][col] == 1:
            visited[row][col] = True
            q = deque([(row, col)])
            tmp = 1
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny)) 
                        tmp += 1
            pic_ls.append(tmp)

print(len(pic_ls))
print(max(pic_ls) if pic_ls else 0)
