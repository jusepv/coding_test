start = input()

row, column = int(start[1]), ord(start[0])-96

steps = [(-1, 2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2,-1)]

cnt = 0
for s in steps:
    if (column + s[0] < 1):
        continue
    elif (column + s[0] > 8):
        continue
    elif (row + s[1] < 1):
        continue
    elif (row + s[1] > 8):
        continue
    cnt += 1

print(cnt)