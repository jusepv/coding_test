N = int(input())

arr = list(map(int, input().split()))
# 증가 부분수열의 최대 길이
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 증가조건
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))