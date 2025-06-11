N = int(input())

arr = [list(input().strip()) for _ in range(N)]
result = []

def quardtree(x, y, n):
    color = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                result.append('(')
                quardtree(x,y, n//2)
                quardtree(x,y+n//2, n//2)
                quardtree(x+n//2, y, n//2)
                quardtree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color)

quardtree(0,0,N)
print("".join(result))