from functions import printBoard, solveBoard, inputBoard




if __name__ == "__main__":
    board=inputBoard()
    print(board)
    printBoard(board)
    print("\n\nTrying to solve the Sudoku Board\n\n")
    if solveBoard(board):
        printBoard(board)
    else:
        print("The Sudoku Puzzle Cannot be solved")
