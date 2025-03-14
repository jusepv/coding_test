from collections import deque

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = float('inf') 

def dfs(start, current, count, cost):
    global min_cost

    # 모든 도시 방문 후 출발 도시로 돌아갈 수 있으면 최소 비용 갱신
    if count == N and W[current][start] != 0:
        min_cost = min(min_cost, cost + W[current][start])
        return

    for next_city in range(N):
        if not visited[next_city] and W[current][next_city] != 0:
            visited[next_city] = True  # 방문 체크
            dfs(start, next_city, count + 1, cost + W[current][next_city])
            visited[next_city] = False  # 백트래킹 (다시 방문 안 한 상태로 되돌리기)

visited[0] = True
dfs(0, 0, 1, 0)

print(min_cost)



