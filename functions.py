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
    print("-"*19)
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
            mat[row][col]=i
            if solveBoard(mat):
                return True
            mat[row][col]=0
    return False

def inputBoard(board=[]):
    while (n:=len(board))<9:
        row=input(f"Enter Row {n+1} Elements seperated by either comma or single space: ")
        if ',' in row:
            row=list(filter(lambda x:x!='',row.split(',')))
            row=list(map(int,row))
        else:
            row=list(filter(lambda x:x!='',row.split(' ')))
            row=list(map(int,row))
        if len(row)==9:
            board.append(row)
        else:
            print("Enter Exactly 9 Elements")
    return board
