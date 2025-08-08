N = int(input())
K = list(map(int, input().split()))

#차분 배열 초기화
diff = [0] * (N+2)

# 각 주장에 대해 거짓말쟁이 조건 반영
for k in K:
    if k > 0:
        diff[0] += 1
        diff[k] -= 1
    else:
        k = -k
        if k + 1 <= N:
            diff[k + 1] += 1
            diff[N + 1] -= 1

# 누적합으로 가능한 x 찾기
liars = []
count = 0
for x in range(N + 1):
    count += diff[x]
    if count == x:
        liars.append(x)

# 출력
print(len(liars))
if liars:
    print(" ".join(map(str, liars)))