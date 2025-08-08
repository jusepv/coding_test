import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

if (9*M) % 10 == 0:
    target = (9*M)/10
else:
    target = int(9*M/10) + 1

freq = {}
# 초기 윈도우 빈도 계산
for i in range(M):
    height = A[i]
    freq[height] = freq.get(height, 0) + 1

#최대 빈도 확인
max_freq = max(freq.values()) if freq else 0
if max_freq >=target:
    print('YES')
else:
    for i in range(N-M):
        # 이전 구간의 첫 요소 제거
        remove_height = A[i]
        freq[remove_height] -= 1
        if freq[remove_height] == 0:
            del freq[remove_height]
        
        # 새 요소 추가
        add_height = A[i+M]
        freq[add_height] = freq.get(add_height, 0) + 1

        max_freq = max(freq.values()) if freq else 0
        if max_freq >= target:
            print("YES")
            break
    else:
        print('NO')