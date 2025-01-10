from collections import deque
N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


q = deque()
min_dim = min(N, M)
# 레이어별로 돌면서 확인
for i in range(min_dim // 2):
    # 현재 레이어의 전체 길이
    total = (N -1 - 2 * i + M - 1 -2 * i) * 2
    rotate_cnt = R % total # 실제 회전 횟수

    q.extend([row[i] for row in arr[i:N-i-1]]) # 왼쪽
    q.extend([arr[N-i-1][i:M-i-1]]) # 아래쪽
    q.extend([row[M-i-1] for row in arr[i+1:N-i][::-1]]) # 오른쪽
    q.extend(arr[i][i+1:M-i][::-1])
    q.rotate(rotate_cnt)

    # 레이어를 다시 배열에 삽입
    for k in range(i, N-i-1):
        arr[k][i] = q.popleft() # 왼쪽
    for k in range(i, M-i-1):
        arr[N-i-1][k] = q.popleft() # 아래쪽
    for k in range(N-i-1, i, -1): # 오른쪽
        arr[k][M-i-1] = q.popleft()
    for k in range(M-i-1, i, -1): #위쪽
        arr[i][k] = q.popleft()


for row in arr:
    print(*row)