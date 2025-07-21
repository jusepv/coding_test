N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


total_dist = 0
for i in range(1, N):
    total_dist += manhattan(coords[i-1], coords[i])

min_dist = total_dist
for i in range(1, N-1): #i번째 건너뛰기, 처음과 마지막은 건너뛰기 불가
    before = manhattan(coords[i-1], coords[i])
    after = manhattan(coords[i], coords[i+1])
    skip = manhattan(coords[i-1], coords[i+1])

    new_dist = total_dist - (before+after) + skip
    min_dist = min(new_dist, min_dist)


print(min_dist)