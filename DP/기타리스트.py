N, S, M = map(int, input().split())

V = list(map(int, input().split()))

dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True # 초기 볼륨 설정

for i in range(1, N+1): # 곡 순회
    for v in range(M+1): # 볼륨 순회
        if dp[i-1][v]: # 이전 상태가 가능한 경우
            if v + V[i-1] <= M:
                dp[i][v + V[i-1]] = True
            if v - V[i-1] >= 0:
                dp[i][v - V[i-1]] = True


for v in range(M, -1, -1):  # 마지막 곡의 볼륨 중 최댓값 찾기
    if dp[N][v]:
        print(v)
        break
else:
    print(-1) 