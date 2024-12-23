H, W = map(int, input().split())

blocks = list(int, input().split())

res = 0

for i in (1, W-1):
    left_max = max(blocks[:i]) 
    right_max = max(blocks[i+1:])
    min_height = min(right_max, left_max)
    if blocks[i] < min_height:
        res += min_height - blocks[i]


print(res)

