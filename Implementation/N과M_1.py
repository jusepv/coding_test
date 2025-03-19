from itertools import permutations

N, M = map(int, input().split())


ls = [i+1 for i in range(N)]
for perm in permutations(ls, M):
    print(*perm)