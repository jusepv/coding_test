N, K = map(int, input().split())

ls = list(input())

cnt = 0
for i in range(N):
    if ls[i] == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if ls[j] == 'H':
                ls[j] = '-'
                cnt += 1
                break

print(cnt)
