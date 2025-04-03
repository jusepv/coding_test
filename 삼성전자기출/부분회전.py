arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]

start_x, start_y = 2, 2
length = 3

#정사각형 배열의 특정 부분만 회전시키는 함수
def partial_rotate(arr, start_x, start_y, length):
    n = len(arr)
    new_arr = [[0] * n for _ in range(n)]
    for y in range(start_y, start_y+length):
        for x in range(start_x, start_x+length):
            # 1. (0,0)으로 옮겨주는 변환 진행
            oy, ox = y - start_y, x-start_x
            # 2. 90도 회전했을때 좌표 구함
            ry, rx = ox, length-oy-1
            # 3. 다시 (start_y, start_x)를 더해줌
            new_arr[start_y][start_x] = arr[y][x]

    for y in range(start_y, start_y+length):
        for x in range(start_x, start_x+length):
            arr[y][x] = new_arr[y][x]

    return arr