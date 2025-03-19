from collections import deque
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken_dist = float('inf')


chickens= []
houses = []
for i in range(N):
    for j in range(N):
        if city[i][j]  == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))


def calc_dist(selected_chickens):
    total_dist = 0
    for house in houses:
        hx, hy = house
        min_dist = float('inf')

        for chicken in selected_chickens: # 선택된 치킨집 중 가장 가까운 치킨집 거리 찾기
            # 방문처리?
            cx, cy = chicken        
            dist = abs(cx-hx) + abs(cy-hy)
            min_dist = min(min_dist, dist)

        total_dist += min_dist
    return total_dist


for comb in combinations(chickens, M):
    local_dist = calc_dist(comb)
    chicken_dist = min(chicken_dist, local_dist)

print(chicken_dist)

