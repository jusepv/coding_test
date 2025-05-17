N, K = map(int, input().split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))

dp = [[0, 0]] * (N+1) # 무게, 가치를 2차원 배열로.

for i in range(1, N+1):
    w, v = ls[i]
    # 가방에 넣을 수 있는 경우
    if dp[i][0] + w <=K:
        dp[i][1] = max(dp[i-1][1], dp[i]+v)
        dp[i][0] = 
    # 무게 초과
    dp[i] = max(dp[i], dp[i-1])