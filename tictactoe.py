#TicTacToe Game

def main():
    theBoard = gameBoard()
    print("Welcome to TicTacToe!\n")
    print(theBoard)
    round1 = playerX(theBoard)
    print(round1)
    round2 = playerO(round1)
    print(round2)
    round3 = playerX(round2)
    print(round3)
    round4 = playerO(round3)
    print(round4)
    round5 = playerX(round4)
    print(round5)
    round6 = playerO(round5)
    print(round6)
    round7 = playerX(round6)
    print(round7)
    round8 = playerO(round7)
    print(round8)
    round9 = playerX(round8)
    print(round9)

#display gameBoard
def gameBoard():
    gameBoard = "|1|2|3|\n|4|5|6|\n|7|8|9|\n"
    return gameBoard

def playerX(theBoard):
    X_Move = str(input("Player X Move: "))
    X_Board = theBoard.replace(X_Move, "X")
    return X_Board

def playerO(theBoard):
    O_Move = str(input("Player O Move: "))
    O_Board = theBoard.replace(O_Move, "O")
    return O_Board

#runs the program
main()
