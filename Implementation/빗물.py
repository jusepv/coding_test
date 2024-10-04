H, W = map(int, input().split())
world = list(map(int, input().split()))

cnt = 0

for i in range(1, W-1):
    left_max = max(world[:i])
      right_max = max(world[i+1:])
    min_height = min(left_max, right_max)
    if world[i] < min_height:
        cnt += min_height - world[i]

print(cnt)