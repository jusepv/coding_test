T = int(input())


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    commands = input()
    direction = 0 # 초기방향: 북쪽
    x, y = 0, 0
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for c in commands:
        if c == 'F':
            x += dx[direction]
            y += dy[direction]
        elif c == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif c == 'L':
            direction = (direction -1) % 4
        elif c == 'R':
            direction = (direction +1) % 4
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = min(max_y, y)

    area = (max_x - min_x) * (max_y - min_y)
    print(area)
