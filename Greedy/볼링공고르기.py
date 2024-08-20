n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
cnt = 0

for x in data:
    array[x] += 1


for i in range(1, m+1):
    n -= array[i]
    cnt += array[i] * 2
