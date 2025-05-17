import sys
from itertools import combinations

n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

left, right = 0, n-1
ls.sort()

cnt = 0

while left<right:
    cur_sum = ls[left]+ls[right]
    if cur_sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif cur_sum > x:
        right -= 1
    else:
        left += 1

print(cnt)