N = int(input())

ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))

dp = [[0] * (3) for _ in range(N)]
dp[0] = ls[0]

for i in range(1, N):
   for c in range(3):
        dp[i][c] = min(dp[i-1][(c+1)%3],dp[i-1][(c+2)%3]) + ls[i][c]


print(min(dp[N-1]))
# print(dp[N-1])