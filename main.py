from functions import prettyPrint, solveBoard
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

0 0 9 | 0 7 0 | 0 0 5
0 0 2 | 1 0 0 | 9 0 0
1 0 0 | 0 2 8 | 0 0 0
------+-------+------
0 7 0 | 0 0 5 | 0 0 1
0 0 8 | 5 1 0 | 0 0 0
0 5 0 | 0 0 0 | 3 0 0
------+-------+------
0 0 0 | 0 0 3 | 0 0 6
8 0 0 | 0 0 0 | 0 0 0
2 1 0 | 0 0 0 | 0 8 7

"""



if __name__ == "__main__":
    prettyPrint(board)
    print("\n\nTrying to solve the Sudoku Board\n\n")
    if solveBoard(board):
        prettyPrint(board)
    else:
        print("The Sudoku Puzzle Cannot be solved")
