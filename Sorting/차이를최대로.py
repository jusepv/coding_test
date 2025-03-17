from itertools import permutations
N = int(input())

ls = list(map(int, input().split()))

max_value = 0

for perm in permutations(ls):
    total = 0
    for i in range(N-1):
        total += abs(perm[i] - perm[i+1])
        max_value = max(total, max_value)


print(max_value)