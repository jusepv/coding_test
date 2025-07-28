# n = int(input())
# dp = [*range(0, n + 1)]  # 초기값: A만 누르는 경우

# for i in range(6, n + 1):  # 최소 3번 복사-붙여넣기 하려면 6번 이상 필요
#     dp[i] = max(
#         2 * dp[i - 3],  # Ctrl-A, Ctrl-C, Ctrl-V 1번
#         3 * dp[i - 4],  # Ctrl-A, Ctrl-C, Ctrl-V 2번
#         4 * dp[i - 5],  # Ctrl-A, Ctrl-C, Ctrl-V 3번
#     )

# print(dp[n])

n = 7
dp = [*range(0, n+1)]
print(dp)