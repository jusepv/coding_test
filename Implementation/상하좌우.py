n = int(input())

plans = input().split()

x,y = 1, 1

for p in plans:
    if p == 'R':
        x += 1
    elif p == 'L':
        if x <= 1:
            continue
        x -= 1
    elif p == 'U':
        if y <= 1:
            continue
        y -= 1
    elif p == 'D':
        y += 1

print(x, y)

