N, X = map(int, input().split())
visit = list(map(int, input().split()))

# 첫 X일 합 계산
max_visit = sum(visit[:X])
max_cnt = 1 if max_visit >0 else 0


curr_sum = max_visit
for i in range(1, N - X + 1):
    curr_sum = curr_sum - visit[i - 1] + visit[i + X - 1]
    if curr_sum > max_visit:
        max_visit = curr_sum
        max_cnt = 1
    elif curr_sum == max_visit:
        max_cnt += 1
        

if max_visit>0:
    print(max_visit)
    print(max_cnt)
else:
    print('SAD')

    