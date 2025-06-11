from collections import deque

N, K = map(int, input().split())

max_pos = 100001
visited = [float('inf')] * max_pos
count = [0] * max_pos

q = deque()
q.append(N)
visited[N] = 0
count[N] = 1

while q:
    curr = q.popleft()
    for next in  [curr-1, curr+1, curr*2]:
        if 0<=next<max_pos:
            # 다음 위치가 처음 방문했거나, 동일한 시간에 다시 도달한 경우
            if visited[next] > visited[curr] + 1:
                visited[next] = visited[curr] + 1
                count[next] = count[curr]
                q.append(next) # q에 추가해줘야 다음 curr가 여기서부터 시작작
            elif visited[next] == visited[curr] + 1:
                count[next] += count[curr] # 이미 방문한 최소시간이므로 경로의 수만 추가

print(visited[K])
print(count[K])
