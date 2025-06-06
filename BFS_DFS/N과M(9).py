N, M = map(int, input().split()) # M은 수열의 타겟 길이
ls = list(map(int, input().split()))

ls.sort()
visited = [False] * len(ls)

seq = []

def backtrack(depth): # depth는 수열의 몇번째 숫자
    if depth == M: # 종료 조건
        print(*seq)
        return
    prev = 0
    for i in range(N):
        if not visited[i] and prev != ls[i]:
            visited = True
            seq.append(ls[i])
            prev = ls[i]
            backtrack(depth+1)
            seq.pop()
            visited[i] = False

backtrack(0)
