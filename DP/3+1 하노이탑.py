def move_hanoi(num_disks, from_peg, to_peg):
    """
    일반적인 3기둥 하노이 이동 함수 (A, B, C만 사용).
    num_disks개의 원판을 from_peg → to_peg로 옮긴다.
    나머지 하나의 보조 기둥은 자동 계산.
    """
    if num_disks == 0:
        return
    aux_peg = 3 - from_peg - to_peg  # 중간 기둥 (0+1+2=3)
    move_hanoi(num_disks - 1, from_peg, aux_peg)
    print('ABC'[from_peg], 'ABC'[to_peg])
    move_hanoi(num_disks - 1, aux_peg, to_peg)

# 입력: 원판 개수
N = int(input())

# 최소 이동 횟수 계산 (DP 이용)
# dp[i]: i개의 원판을 3+1 하노이 방식으로 옮길 때 최소 이동 횟수
min_moves = [0, 1]  # N=0, N=1의 경우 초기화
for i in range(2, 21):
    moves = (2 ** (i - 2)) - 1 + 3 + min_moves[i - 2]
    min_moves.append(moves)

# 1. 최소 이동 횟수 출력
print(min_moves[N])
# 2. 이동 경로 출력
# 현재 원판이 놓여 있는 출발 기둥의 인덱스 (A=0, B=1, C=2)
current_source_peg = 0
remaining_disks = N
# 반복적으로 2개씩 큰 원판을 처리
while remaining_disks >= 2:
    small_disk_count = remaining_disks - 2
    aux_peg = 2 - current_source_peg  # 출발 기둥 A→C or C→A (0↔2)
    # 1단계: 작은 원판 (N-2개)을 A→C (출발 → 보조 기둥) 로 일반 하노이 이동
    move_hanoi(small_disk_count, current_source_peg, aux_peg)
    # 2단계: 큰 두 개 원판을 D로 옮기는 3단계 이동
    # (1) 큰 원판 N-1: 출발 → B
    print('ABC'[current_source_peg], 'B')
    # (2) 가장 큰 원판 N: 출발 → D
    print('ABC'[current_source_peg], 'D')
    # (3) 큰 원판 N-1: B → D
    print('B', 'D')
    # N에서 2개 줄이기 (큰 원판 2개 처리 완료)
    remaining_disks -= 2
    # 다음 사이클을 위해 출발 기둥 전환 (A↔C)
    current_source_peg = aux_peg
# 남은 원판이 1개일 경우: 그냥 바로 D로 옮기면 됨
if remaining_disks == 1:
    print('ABC'[current_source_peg], 'D')
