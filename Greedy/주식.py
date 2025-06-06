T = int(input())

for _ in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    max_price = 0
    profit = 0
    for i in range(N-1, -1, -1):
        if ls[i] > max_price:
            max_price = ls[i]
        else:
            profit += (max_price - ls[i])
    print(profit)