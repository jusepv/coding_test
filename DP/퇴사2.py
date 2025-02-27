N = int(input())

ls = []
for i in range(N):
    ls.append(list(map(int, input().split())))

dp = [0] * (N+1)


for i in range(N):
    Ti = ls[i][0]
    Pi = ls[i][1]
    # 상담이 가능한 경우
    if i + Ti <= N:
        dp[i+Ti] = max(dp[i+Ti], dp[i]+Pi)
    # 상담이 불가능한 경우
    dp[i+1] = max(dp[i+1], dp[i])
    
print(dp[N])