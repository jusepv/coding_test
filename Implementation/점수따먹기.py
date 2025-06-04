N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dp = [[0] * (M+1) for _ in range(N+1)]

# 
for row in range(1, N+1):
    for col in range(1, M+1):
        dp[row][col] = graph[row-1][col-1] + dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1]

answer = -int(1e7)
# sx, sy는 부분행렬의 좌상단 좌표
# ex, ey는 부분행렬의 우하단 좌표
for sy in range(1, N+1):
    for sx in range(1, M+1):
        for ey in range(sy, N+1):
            for ex in range(sx, M+1):
                answer = max(answer, dp[ey][ex] - dp[sy-1][ex] - dp[ey][sx-1] + dp[sy-1][sx-1])

print(answer)