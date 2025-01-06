from itertools import combinations


N = int(input())
half = int(N/2)
arr = [list(map(int, input().split())) for _ in range(N)]


ls = [i for i in range(N)]
comb = combinations(ls, half)

abil_ls = []

for c in comb:
    # 두 팀으로 나누기
    team1 = list(c)
    team2 = [x for x in ls if x not in team1]
    team1_comb = combinations(team1, 2)
    team2_comb = combinations(team2, 2)
    team1_score = 0
    team2_score = 0
    for i in team1_comb:
        team1_score += arr[i[0]][i[1]]  + arr[i[1]][i[0]]  
    for j in team2_comb:
        team2_score += arr[j[0]][j[1]]  + arr[j[1]][j[0]]  
    abil_ls.append(abs(team1_score-team2_score))

print(min(abil_ls))

