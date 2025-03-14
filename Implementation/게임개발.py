n = int(input())
rn=int(input())
l = [[0]*n for i in range(n)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
d = 0
x,y = n//2,n//2
l[x][y] = 1
r = 0
for i in range((n*2)-1):
    if i %2 == 0:
        r += 1
    for j in range(r):
        dx = x + di[d]
        dy = y + dj[d]
        if l[x][y] == n*n:
            break
        l[dx][dy] = l[x][y]+1
        if l[dx][dy] == rn:
            ri, rj = dx+1,dy+1
        x,y = dx,dy
    d = (d+1)%4


for i in l:
    print(' '.join(map(str,i)))
print(ri,rj)