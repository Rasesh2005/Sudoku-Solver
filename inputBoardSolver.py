from functions import prettyPrint, solveBoard, inputBoard




if __name__ == "__main__":
    board=inputBoard()
    print(board)
    prettyPrint(board)
    print("\n\nTrying to solve the Sudoku Board\n\n")
    if solveBoard(board):
        prettyPrint(board)
    else:
        print("The Sudoku Puzzle Cannot be solved")
