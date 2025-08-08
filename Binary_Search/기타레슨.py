N, M = map(int, input().split())
ls = list(map(int, input().split()))

start = max(ls)
end = sum(ls)

res = 0
while (start<=end):
    mid = (start+end)//2
    # 블루레이에 강의 넣기
    cnt, total = 1, 0
    for i in range(N):
        if total + ls[i] > mid:
            cnt += 1
            total = 0
        total += ls[i]
    if cnt <= M:
        res = mid
        end = mid-1
    else:
        start = mid+1

print(res)