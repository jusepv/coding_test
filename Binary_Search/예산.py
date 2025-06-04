N = int(input())
ls = list(map(int, input().split()))
M = int(input()) # 총 예산

start = 0
end = max(ls)
ls.sort()

while start<=end:
    total = 0
    mid = (start+end)//2 # 상한액
    print("start: ", start, ", end: ", end, "mid: ", mid)
    for b in ls:
        if b <= mid:
            total += b
        else:
            # 상한액 넘으면 
            total += mid
    if total <= M: # 지출양이 총 예산보다 작으면
        start = mid + 1
    else: # 지출양이 총 예산보다 크면
        end = mid - 1
print(end)