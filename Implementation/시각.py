n = int(input())

cnt = 0

for h in range(n):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)