N = int(input())

# arr = []
# for _ in range(N):
#     arr.append(list(input().split()))
arr = [list(input()) for _ in range(N)]
max_size = 0

def check(arr):
    max_cnt = 1
    # 행을 체크
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    # 열을 체크
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    return max_cnt

max_size = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            # 상하 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            max_cnt = check(arr)
            max_size = max(max_cnt, max_size)
            #바꾼거 원래대로 
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        if i + 1 < N:
            # 좌우 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            max_cnt = check(arr)
            max_size = max(max_cnt, max_size)
            # 바꾼거 원래대로
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]


print(max_size)