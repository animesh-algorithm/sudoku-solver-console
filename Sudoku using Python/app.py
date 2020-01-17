def displayBoard(board):
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print('- - - - - - - - - - - -')
        for j in range(len(board[i])):
            if j != 0 and j % 3 == 0:
                print(' | ', end='')
            print(board[i][j], end=' ')
        print()

def solve(board):
    emptyCellPosition = findEmptyCell(board)
    if emptyCellPosition == None:
        return True
    row = emptyCellPosition[0]
    col = emptyCellPosition[1]

    for num in range(1, 10):
        if isValid(board, num, emptyCellPosition):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def isValid(board, num, position):
    for i in range(len(board)):
        if board[position[0]][i] == num and position[1] != i:
            return False
        if board[i][position[1]] == num and position[0] != i:
            return False
    hCell = position[1] // 3
    vCell = position[0] // 3

    for i in range(vCell*3, vCell*3 + 3):
        for j in range(hCell*3, hCell*3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False
    return True

def findEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def run():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0], 
        [6, 0, 0, 0, 7, 5, 0, 0, 9], 
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0], 
        [0, 0, 1, 0, 5, 0, 9, 3, 0], 
        [9, 0, 4, 0, 6, 0, 0, 0, 5], 
        [0, 7, 0, 3, 0, 0, 0, 1, 2], 
        [1, 2, 0, 0, 0, 7, 4, 0, 0], 
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    displayBoard(board)
    solve(board)
    print('- - - - - - - - - - - - - - - - - - - - - - -')
    displayBoard(board)


if __name__ == '__main__':
    run()
