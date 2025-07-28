N = int(input())
dist_ls = list(map(int, input().split()))
price_ls = list(map(int, input().split()))

min_cost = price_ls[0]
total = 0

for i in range(N-1):
    min_cost = min(min_cost, price_ls[i]) 
    total += min_cost * dist_ls[i] # 더 싼 주유소 가격으로 현재 거리까지 기름 넣기
 
print(total)