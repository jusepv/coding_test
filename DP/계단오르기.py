N = int(input())
scores = [0]+ list(int(input()) for i in range(N))

dp = [0] * (N+1)
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]


for i in range(3, N):
    dp[i] = max(dp[i-1]+scores[i-1], )
    print(dp)