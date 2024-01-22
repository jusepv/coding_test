def simulate_movement(map_data, start_position, start_direction):
    # 방향: 0=북, 1=동, 2=남, 3=서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시작 위치와 방향 설정
    x, y, direction = start_position
    visited = set([(x, y)])  # 시작 위치를 방문한 칸으로 설정

    while True:
        moved = False
        for _ in range(4):
            # 왼쪽으로 회전
            direction = (direction - 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

            # 이동 가능한지 확인 (육지이고, 아직 방문하지 않은 칸)
            if map_data[nx][ny] == 0 and (nx, ny) not in visited:
                x, y = nx, ny
                visited.add((x, y))
                moved = True
                break

        # 네 방향 모두 이동할 수 없는 경우
        if not moved:
            nx, ny = x - dx[direction], y - dy[direction]
            # 뒤가 바다인 경우 움직임을 멈춤
            if map_data[nx][ny] == 1:
                break
            x, y = nx, ny

    return len(visited)

N, M = 4, 4
start_position = (1, 1, 0)
map_data = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

# 이동 후 방문한 칸의 수 계산
visited_count = simulate_movement(map_data, start_position, start_position[2])
print(visited_count)