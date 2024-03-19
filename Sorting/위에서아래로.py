n = int(input())

ls = []

for i in range(n):
    ls.append(int(input()))

ls2 = sorted(ls, reverse=True)

for i in ls2:
    print(i, end=' ')