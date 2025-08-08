
N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split()) for _ in range(N))]
visited = [[0]* M for _ in range(N)]

cnt = 0

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
def turn_left(d):
    return (d+3)%4

while True:
    # 현재칸 청소
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
    # 주위에 청소되지 않은 칸이 있는 경우
    cleaned = False
    for i in range(4):
        d = turn_left(d)
        nr, nc = r+dr[d], c+dc[d]    
        if 0<=nr<N and 0<=nc<M and room[nc][nc]==0 and visited[nr][nc]==0:
            r, c = nr, nc
            cleaned = True
            break
    #주위에 청소되지 않은 칸이 없는 경우
    # 후진
    if not cleaned:
        back_d = (d+2)%4
        br, bc = r+dr[back_d], c+dc[back_d]
        # 후진할 수 있는 경우
        if 0<=br<N and 0<=bc<M and room[bc][bc]==0 and visited[br][bc]==0:
            r, c = br, bc
            cleaned = True
            break
        else:
            break

print(cnt)
            
