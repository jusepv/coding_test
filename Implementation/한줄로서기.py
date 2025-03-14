N = int(input())  
ls = list(map(int, input().split()))  
res = [0] * N  

for i in range(1, N + 1):  # 키 
    count = ls[i - 1]  # 왼쪽에 있어야 하는 큰 사람 수
    for j in range(N):
        if res[j] == 0:  # 빈 자리일 때만 카운트 감소
            if count == 0:  
                res[j] = i  # 현재 키 i 배치
                break  
            count -= 1  # 건너뛰어야 하는 빈 자리 수 감소

print(*res)  
