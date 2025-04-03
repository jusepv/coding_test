arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def rotate_90(arr):
    r = len(arr)
    c = len(arr[0])
    res = [[0]*r for _ in range(c)] # 배열의 row, col 뒤바뀌는것 주의
    for i in range(r):
        for j in range(c):
            res[j][r-i-1] = arr[i][j]
    return res


def rotate_180(arr):
    r = len(arr)          
    c = len(arr[0])       
    res = [[0]*c for _ in range(r)]  # 결과 배열: r x c (원래 크기 유지)
    for i in range(r):
        for j in range(c):
            res[r-1-i][c-1-j] = arr[i][j]  # 180도 회전
    return res

def rotate_270(arr):
    r = len(arr)          
    c = len(arr[0])       
    res = [[0]*r for _ in range(c)]  # 결과 배열: c x r (90도와 동일)
    for i in range(r):
        for j in range(c):
            res[c-1-j][i] = arr[i][j]  # 270도 회전
    return res