import sys
N = int(sys.stdin.readline())


def hanoi(n, start, end, via, moves):
    if n==1:
        moves.append((start, end))
    else:
        hanoi(n-1, start, via, end, moves)
        moves.append((start, end))
        hanoi(n-1, via, end, start, moves)

print((1<<N)-1)
if N<=20:
    moves = []

    hanoi(N, 1, 3, 2, moves)
    for move in moves:
        print(*move)

