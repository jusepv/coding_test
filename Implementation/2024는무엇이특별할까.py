import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = [int(x) for x in sys.stdin.readline().split()]
    print((N >> K) - (N >> (K + 1))) # 수 x가 2^K의 배수지만 2^(K+1)의 배수가 아니어야 함
        