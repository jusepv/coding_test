king_pos, stone_pos, N = input().split()
N = int(N)

ls = []
for _ in range(N):
    ls.append(input().strip())

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

# 알파벳 -> 숫자
def pos_to_coord(pos):
    col = ord(pos[0]) - ord('A')
    row = 8 - int(pos[1])
    return (row, col)

# 숫자 -> 알파벳
def coord_to_pos(row, col):
    return chr(col + ord('A')) + str(8 - row)

king = pos_to_coord(king_pos)
stone = pos_to_coord(stone_pos)

for move in ls:
    dr, dc = directions[move]
    new_king = (king[0] + dr, king[1] + dc)

    # 킹이 체스판 안에 있는지 확인
    if 0 <= new_king[0] < 8 and 0 <= new_king[1] < 8:
        if new_king == stone:
            new_stone = (stone[0] + dr, stone[1] + dc)
            if 0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8:
                king = new_king
                stone = new_stone
        else:
            king = new_king

print(coord_to_pos(*king))
print(coord_to_pos(*stone))
