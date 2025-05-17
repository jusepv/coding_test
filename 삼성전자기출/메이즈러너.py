def move_people():
    """사람들 이동(total_distance 추가, 목적지 도달하면 제거)"""
    distance = 0
    for i, (x, y) in enumerate(people):
        # 상하 방향 먼저 체크
        if exit_x < x and maze[x-1][y] == 0:  # 위
            people[i] = (x-1, y)
            distance += 1
        elif exit_x > x and maze[x+1][y] == 0:  # 아래
            people[i] = (x+1, y)
            distance += 1
        # 좌우 방향 이후 체크
        elif exit_y < y and maze[x][y-1] == 0:  # 왼쪽
            people[i] = (x, y-1)
            distance += 1
        elif exit_y > y and maze[x][y+1] == 0:  # 오른쪽
            people[i] = (x, y+1)
            distance += 1
    
    # 목적지 도달 제거
    new_people = [(x, y) for x, y in people if (x, y) != (exit_x, exit_y)]
    return distance, new_people

def rotate_90(arr):
    r = len(arr)
    c = len(arr[0])
    res = [[0] * r for _ in range(c)]  # 행과 열이 뒤바뀜
    for i in range(r):
        for j in range(c):
            res[j][r - i - 1] = arr[i][j]
    return res

def find_rx_ry_rd():
    # rx, ry, rd 찾기 (작은 크기부터 탐색하여 최소 크기 보장)
    for rd in range(1, N + 1):  # 한변 크기(1 ~ N)
        for rx in range(N - rd + 1):
            for ry in range(N - rd + 1):
                people_include = any(rx <= px < rx + rd and ry <= py < ry + rd for px, py in people)
                if people_include and rx <= exit_x < rx + rd and ry <= exit_y < ry + rd:
                    return rx, ry, rd
    return 0, 0, 0  # 기본값 (필요 시 조정)

# 미로 크기, 참가자 수, 게임 시간
N, M, K = map(int, input().split())

# 0: 빈칸, 1~9: 벽
maze = [list(map(int, input().split())) for _ in range(N)]
people = [(x - 1, y - 1) for x, y in [tuple(map(int, input().split())) for _ in range(M)]]
exit_x, exit_y = [x - 1 for x in map(int, input().split())]

total_distance = 0  # 모든 참가자들의 이동 거리 합

for _ in range(K):
    # 1. 모든 참가자 이동
    distance, people = move_people()
    total_distance += distance

    if not people:  # 모든 참가자 탈출
        break

    # 2. 미로 회전
    # 2-1. 가장 작은 정사각형 찾기
    rx, ry, rd = find_rx_ry_rd()

    # 2-2. 90도 회전 (maze, people, exit_x_y 변경)
    # 정사각형 부분 추출
    before_rotate = [row[ry:ry + rd] for row in maze[rx:rx + rd]]
    # 90도 회전
    after_rotate = rotate_90(before_rotate)
    # 회전 후 벽 내구도 감소 및 미로에 반영
    for i in range(rd):
        for j in range(rd):
            val = after_rotate[i][j]
            maze[rx + i][ry + j] = max(val - 1, 0) if val > 0 else 0

    # 참가자 좌표 회전
    new_people = []
    for px, py in people:
        if rx <= px < rx + rd and ry <= py < ry + rd:
            ox, oy = px - rx, py - ry 
            #px는 절대 좌표, rx는 회전할 정사각형의 좌상단, ox는 회전 영역안에서의 행좌표
            nx, ny = oy, rd - 1 - ox  # rotate_90과 동일한 변환
            new_people.append((rx + nx, ry + ny))
        else:
            new_people.append((px, py))
    people = new_people

    # 출구 좌표 회전
    if rx <= exit_x < rx + rd and ry <= exit_y < ry + rd:
        ox, oy = exit_x - rx, exit_y - ry
        nx, ny = oy, rd - 1 - ox
        exit_x, exit_y = rx + nx, ry + ny

    # 탈출 체크 (필요 시)
    people = [(x, y) for x, y in people if (x, y) != (exit_x, exit_y)]


print(total_distance)
print(exit_x + 1, exit_y + 1)  # 1-based로 출력