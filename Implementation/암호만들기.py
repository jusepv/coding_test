from itertools import combinations

L, C = map(int, input().split())
ls = list(input().split())
ls.sort()

moum_ls = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(ls, L):
    moum_cnt = sum(1 for char in comb if char in moum_ls)
    if (moum_cnt >= 1 and  (L-moum_cnt) >= 2):
        print(''.join(comb))