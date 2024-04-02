n = 4
# array = list(map(int, input()))
array = [1,3,1,5]


d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(array[i]+d[i-2], d[i-1])

print(d[n-1])