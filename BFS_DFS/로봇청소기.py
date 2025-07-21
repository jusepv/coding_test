
N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 북 동 남 서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn_left(d):
    return (d+3)%4

cnt = 0

while True:
    # 1. 현재 위치 청소
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
    
    cleaned = False
    for _ in range(4):
        d = turn_left(d)
        nx, ny = r+dx[d], c+dy[d]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
            r, c = nx, ny # 이동
            cleaned = True
            break

    if not cleaned:
        # 후진 시도
        back_d = (d+2)%4
        br, bc = r+dx[back_d], c+dy[back_d]

        if 0<=br<N and 0<=bc<M and arr[br][bc] == 0:
            r,c = br, bc # 후진
        else:
            break

print(cnt)