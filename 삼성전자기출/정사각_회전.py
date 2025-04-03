arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(arr)
# 시계방향 90도 회전
arr_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_90[j][n-i-1] = arr[i][j]
print(arr_90)

# 시계방향 180도 회전
arr_180 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_180[n-i-1][n-j-1] = arr[i][j]
print(arr_180)

# 시계방향 270도 (반시계 90도) 회전
arr_270 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_270[n-j-1][i] = arr[i][j]
print(arr_270)