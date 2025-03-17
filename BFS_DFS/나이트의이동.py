from collections import deque
N = int(input())

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]


for _ in range(N):
    L = int(input())
    dist = [[-1]*L for _ in range(L)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        print(0)
        continue
    q = deque()
    q.append(start)
    dist[start[0]][start[1]] = 0

    while q:
        x,y = q.popleft()      
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<L and 0<=ny<L and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                
                if (nx, ny) == end:
                    print(dist[nx][ny])
                    break
        else:
            continue
        break