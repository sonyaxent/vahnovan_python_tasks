# There is a queen on an 8 x 8 chessboard.
# Mark the position of the queen on the board and mark all the squares that the queen captures.
# Mark the cell where the queen stands with the letter Q, mark the cells that the queen beats with asterisks *, fill in the rest of the cells with dots.
# The chess queen can move vertically, horizontally and diagonally.
if __name__ == "__main__":
    type_in = input()
    board = [['.'] * 8 for _ in range(8)]
    y, x = 8 - int(type_in[1]), ord(type_in[0]) - 97
    for i in range(8):
        for j in range(8):
            if (y == i) or (x == j) or abs(y - i) == abs(x - j):
                board[i][j] = '*'
    board[y][x] = 'Q'
    for line in board:
        print(*line)