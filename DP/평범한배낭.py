N, K = map(int, input().split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))

dp = [0] * (K+1)

for i in range(N):
    w, v = ls[i]
    for j in range(K, w-1, -1): # j는 무게
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[K])
        

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = ls[i-1]
    for k in range(K+1):
        if k < w: # 무게 초과
            dp[i][k] = dp[i-1][k]
        else: # 무게 초과 아님
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v)

print(dp[N][K])