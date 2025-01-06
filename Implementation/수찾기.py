N = int(input())
ls = set(map(int, input().split()))

M = int(input())

target_ls = list(map(int, input().split()))

for i in target_ls:
    if i in ls:
        print(1)
    else:
        print(0)
