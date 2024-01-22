n, m = map(int, input().split())


card = 0 
for i in range(n):
    data = list(map(int, input().split()))
    if card <= min(data):
        card = min(data)

print(card)
    