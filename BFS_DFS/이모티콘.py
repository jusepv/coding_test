from collections import deque

S = int(input())


q = deque()
q.append((1,0)) # (화면에 존재하는 이모티콘 수, 클립보드에 저장된 이모티콘 수)
visited = [[0]* 1001 for _ in range(1001)]

while q:
    x_screen, x_clip = q.popleft()
    if x_screen == S:
        ans = visited[x_screen][x_clip]
        break
        
    arr = [
        (x_screen, x_screen),
        (x_screen+x_clip, x_clip),
        (x_screen-1,x_clip)
    ]
    for screen, clip in arr:
        if 0<=screen<1001 and 0<=clip<1001 and not visited[screen][clip]:
            q.append((screen,clip)) # 조건 진행.
            visited[screen][clip] = visited[x_screen][x_clip]+1 # 조건이 진행되면 시간 1초 추가
    
print(ans)