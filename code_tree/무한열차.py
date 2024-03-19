n = int(input())

loc_ls, vel_ls = [], []

for i in range(n):
    loc, vel = map(int, input().split())
    loc_ls.append(loc)
    vel_ls.append(vel)

    # loc.append(data[0])
    # vel.append(data[1])
train  = 1

min_v = 100000000
for j in range(n):
    if min_v < vel_ls[j]:
        continue
    elif min_v >= vel_ls[j]:
        train += 1
        min_v = vel_ls[j]

print(train)  