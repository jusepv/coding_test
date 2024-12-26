A, B = map(int, input().split())

cnt = 0

ls = [0]
for i in range(1,1000):
    for _ in range(i):
        ls.append(i)

print(sum(ls[A:B+1]))