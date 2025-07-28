N, T  = map(int, input().split())

ls = []
for _ in range(N):
    k, s = map(int, input().split())
    ls.append((k, s))

dp = [0] * (T+1)

for k, s in ls:
    for i in range(T, k-1, -1):
        dp[i] = max(dp[i], dp[i-k]+s)

print(dp[T])
