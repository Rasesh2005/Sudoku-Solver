board = [
    [3, 2, 0, 9, 0, 0, 8, 0, 6],
    [4, 0, 1, 2, 3, 0, 0, 5, 0],
    [0, 0, 7, 6, 4, 0, 1, 2, 0],
    [2, 0, 6, 0, 0, 9, 3, 0, 0],
    [1, 0, 0, 0, 6, 3, 0, 8, 2],
    [0, 0, 4, 0, 2, 7, 6, 9, 0],
    [6, 1, 0, 0, 0, 4, 5, 3, 8],
    [5, 0, 3, 0, 1, 2, 0, 6, 9],
    [0, 0, 0, 3, 5, 6, 2, 1, 0]]

""" 
Invalid Test Case for Testing:

. . 9 | . 7 . | . . 5
. . 2 | 1 . . | 9 . .
1 . . | . 2 8 | . . .
------+-------+------
. 7 . | . . 5 | . . 1
. . 8 | 5 1 . | . . .
. 5 . | . . . | 3 . .
------+-------+------
. . . | . . 3 | . . 6
8 . . | . . . | . . .
2 1 . | . . . | . 8 7

"""

def isSolved(mat):
    for row in mat:
        for i in row:
            if i == 0:
                return False
    return True


def isValid(mat, row, col, n):
    if n in mat[row]:
        return False
    for r in mat:
        if n == r[col]:
            return False
    # Checking for boxes left
    r = row//3
    c = col//3
    rs = r*3
    cs = c*3
    for i in range(rs, rs+3):
        for j in range(cs, cs+3):
            if mat[i][j] == n:
                return False
    return True


def findEmpty(mat):
    for rowIndex, rowItem in enumerate(mat):
        for colIndex, colItem in enumerate(rowItem):
            if colItem == 0:
                return rowIndex, colIndex
    return False


def printBoard(mat):
    print("-"*17)
    for rowIndex, rowItem in enumerate(mat):
        row = list(str(rowItem).replace(
            ",", "").replace("[", "|").replace("]", "|"))
        row[6] = row[12] = "|"
        print("".join(row))
        if not (rowIndex+1) % 3:
            print("-"*19)


def solveBoard(mat):
    emptySpace=findEmpty(mat)
    if not emptySpace:
        return True
    row,col=emptySpace
    for i in range(1,10):
        if isValid(mat,row,col,i):
            # print(f"Trying {i} at row={row} col={col}")re
            mat[row][col]=i
            if solveBoard(mat):
                return True
    return False


if __name__ == "__main__":
    printBoard(board)
    if solveBoard(board):
        printBoard(board)
    else:
        print("The Sudoku Puzzle Cannot be solved")
