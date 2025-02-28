N = int(input())

arr = list(map(int, input().split()))
# 감소 부분수열의 최대 길이
dp = [1] * N

for i in range(1, N):
    for j in range(i):# i 이전의 병사 (j)를 모두 탐색
        # 감소조건
        if arr[i] < arr[j]: # 이전 병사의 전투력이 더 큰, 즉 내림차순 가능이면
            dp[i] = max(dp[i], dp[j]+1) # 부분 수열 갱신

max_lds = max(dp)

print(N-max_lds)