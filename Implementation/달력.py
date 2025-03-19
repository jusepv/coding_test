N = int(input())

schedule = []

for _ in range(N):
    schedule.append(list(map(int, input().split())))

schedule = sorted(schedule, key=lambda x: (x[0], -x[1]))

date =  [[0] * 367 for _ in range(N)]

max_cnt = 0


for start, end in schedule:
    cnt = 0
    while any(date[cnt][start:end+1]):
        cnt += 1
    for i in range(start, end+1):
        date[cnt][i] = 1
    max_cnt = max(max_cnt, cnt+1)

total_coting = 0
width, height = 0, 0

for day in range(1, 367):
    col_height = sum(date[row][day] for row in range(max_cnt)) # 해당 날짜의 최대 높이
    if col_height > 0: # 일정이 있을때
        width += 1
        height = max(height, col_height)
    else: # 끊어지는 로직을 여기서
        total_coting += width * height
        width, height = 0, 0
    

if width > 0:
    total_coting += width * height

print(total_coting)