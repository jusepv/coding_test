import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
options = list(map(int, sys.stdin.readline().split()))

def op_1(arr): # 상하반전
    return arr[::-1]

def op_2(arr): # 좌우반전
    for i in range(N):
        arr[i] = arr[i][::-1]
    return arr

def op_3(arr): #오른쪽 90도 회전
    N, M = len(arr), len(arr[0])
    res = [[0]*N for _ in range(M)]  # M×N 배열
    for i in range(N):
        for j in range(M):
            res[j][N-i-1] = arr[i][j]
    return res

def op_4(arr): # 왼쪽으로 90도 회전
    N, M = len(arr), len(arr[0])
    res = [[0]*N for _ in range(M)]  # M×N 배열
    for i in range(N):
        for j in range(M):
            res[M-j-1][i] = arr[i][j]
    return res

def op_5(arr):  # 그룹 이동 (1→2, 2→3, 3→4, 4→1)
    res = [[0]*M for _ in range(N)]
    n, m = N//2, M//2
    group1 = [row[:m] for row in arr[:n]]
    group2 = [row[m:] for row in arr[:n]]
    group3 = [row[m:] for row in arr[n:]]
    group4 = [row[:m] for row in arr[n:]]
    for i in range(n):
        for j in range(m):
            res[i][j+m] = group1[i][j]
            res[i+n][j+m] = group2[i][j]
            res[i+n][j] = group3[i][j]
            res[i][j] = group4[i][j]
    return res

def op_6(arr):  # 그룹 이동 (1→4, 4→3, 3→2, 2→1)
    res = [[0]*M for _ in range(N)]
    n, m = N//2, M//2
    group1 = [row[:m] for row in arr[:n]]
    group2 = [row[m:] for row in arr[:n]]
    group3 = [row[m:] for row in arr[n:]]
    group4 = [row[:m] for row in arr[n:]]
    for i in range(n):
        for j in range(m):
            res[i][j] = group2[i][j]
            res[i][j+m] = group3[i][j]
            res[i+n][j+m] = group4[i][j]
            res[i+n][j] = group1[i][j]
    return res

for o in options:
    if o == 1:
        arr = op_1(arr)
    elif o == 2:
        arr = op_2(arr)
    elif o == 3:
        arr = op_3(arr)
        N, M = M, N  # 배열 크기 갱신
    elif o == 4:
        arr = op_4(arr)
        N, M = M, N  # 배열 크기 갱신
    elif o == 5:
        arr = op_5(arr)
    elif o == 6:
        arr = op_6(arr)

for ar in arr:
    print(*ar)
