def permutations(arr, n, result=None, visited=None):
    # 첫 호출 시 초기화
    if result is None:
        result = []
    if visited is None:
        visited = [False] * len(arr)

    # 목표 길이에 도달하면 출력
    if len(result) == n:
        print(result[:])
        return

    # 순열 생성
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            permutations(arr, n, result, visited)
            result.pop()
            visited[i] = False

# 사용 예시
arr = [1, 2, 3, 4]
permutations(arr, 2)