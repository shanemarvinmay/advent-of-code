from loop_test import matrix
def get_possible_moves(row, col, char, m):
    possible_moves = []
    if char == 'S':
        for i in range(row - 1, row + 2):
            if i < 0 or i >= len(m):
                continue
            for j in range(col - 1, col + 2):
                if j < 0 or j >= len(m[i]) or (i == row and j == col):
                    continue
                possible_moves.append((i, j))
    elif char == 'J':
        if row > 0:
            possible_moves.append((row - 1, col))
        if col > 0:
            possible_moves.append((row, col - 1))
    elif char == 'L':
        if row > 0:
            possible_moves.append((row - 1, col))
        if col + 1 < len(m[row]):
            possible_moves.append((row, col + 1))
    elif char == 'F':
        if col + 1 < len(m[row]):
            possible_moves.append((row, col + 1))
        if row + 1 < len(m):
            possible_moves.append((row + 1, col))
    elif char == '7':
        if col > 0:
            possible_moves.append((row, col - 1))
        if row + 1 < len(m):
            possible_moves.append((row + 1, col))
    elif char == '|':
        if row > 0:
            possible_moves.append((row - 1, col))
        if row + 1 < len(m):
            possible_moves.append((row + 1, col))
    elif char == '-':
        if col > 0:
            possible_moves.append((row, col - 1))
        if col + 1 < len(m[row]):
            possible_moves.append((row, col + 1))
    return possible_moves        
def get_valid_moves(row, col, char, m):
    valid_moves = []
    possible_moves = get_possible_moves(row, col, char, m)
    for move in possible_moves:
        if move in get_possible_moves(move[0], move[1], m[move[0]][move[1]], m):
            valid_moves.append(move)
    return valid_moves
def get_furthest_step(row, col, m, moves=0, hist=dict()):
    if m[row][col] == 'S' and moves > 0:
        return moves // 2
    valid_moves = get_valid_moves(row, col, m[row][col], m)
    for move in valid_moves:
        row, col = move
        if row in hist and col in hist[row]:
            continue
        if row not in hist:
            hist[row] = set()
        if col not in hist[row]:
            hist[row].add(col)
    return get_furthest_step(row, col, m, moves + 1, hist)
if __name__ == '__main__':
    row, col = 0, 0
    for i in range(len(matrix)):
        if 'S' in matrix[i]:
            row = i
            col = matrix[i].index('S')
            break
    print(matrix)
    print('get_furthest_step', get_furthest_step(row, col, matrix))
