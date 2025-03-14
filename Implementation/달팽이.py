N = int(input())
target = int(input())

# 방향 벡터: 동→남→서→북 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0] * N for _ in range(N)]

# 시작 위치 (중앙)
x, y = N // 2, N // 2
num = 1 
arr[x][y] = num

# 목표 위치 초기화
target_x, target_y = x, y

# 초기 방향 (동쪽)
direction = 0

# 초기 이동 거리
length = 1

while num < N * N:
    # 같은 길이로 두 방향 이동
    for i in range(2):
        # 현재 길이만큼 이동
        for j in range(length):
            # 방향대로 이동
            x += dx[direction]
            y += dy[direction]
            
            # 배열 범위 체크
            if x < 0 or x >= N or y < 0 or y >= N:
                break
                
            num += 1
            if num > N * N:
                break
                
            arr[x][y] = num
            
            if num == target:
                target_x, target_y = x, y
        
        # 방향 변경
        direction = (direction + 1) % 4
        
        if num >= N * N:
            break
            
    # 이동 거리 증가
    length += 1

# 결과 출력
for row in arr:
    print(*row)

print(target_x + 1, target_y + 1)