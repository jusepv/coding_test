def permutations(arr, n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return # 해당 지점에서 더 이상 탐색하지 않고 재귀 호출 종료
    for i in range(len(arr)):
        if not visited[i]: # 순서를 고려해야 되서
            visited[i] = True
            permutations(arr, n, new_arr + [arr[i]])
            visited[i] = False # 백트래킹

arr = [1, 2, 3, 4]
visited = [False]*len(arr)

permutations(arr, 2, [])

def combinations(arr, n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return # 현재 호출 종료 
    for i in range(c, len(arr)):  # 순서 상관 없으므로 c부터 시작
        combinations(arr, n, new_arr+[arr[i]], i+1)


arr = [1, 2, 3, 4]
combinations(arr, 2, [], 0)

def product(arr, n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(arr, n, new_arr+[arr[i]])
arr = [1, 2, 3, 4]
product(2, [])

def combination_dupli(arr, n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return 
    for i in range(c, len(arr)):
        combination_dupli(arr, n, new_arr+[arr[i]],i)

