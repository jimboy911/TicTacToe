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
    winningTest(round5)
    print(round5)
    round6 = playerO(round5)
    winningTest(round6)
    print(round6)
    round7 = playerX(round6)
    winningTest(round5)
    print(round7)
    round8 = playerO(round7)
    winningTest(round5)
    print(round8)
    round9 = playerX(round8)
    winningTest(round5)
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

def winningTest(round):
    pureBoard = round.replace("\n", "")
    gameBoardArr = pureBoard.split("|")

    while '' in gameBoardArr:
        gameBoardArr.remove('')

    #cover horiztonals
    if gameBoardArr[0] == gameBoardArr[1] == gameBoardArr[2]:
        print("You Win!")

    elif gameBoardArr[3] == gameBoardArr[4] == gameBoardArr[5]:
        print("You Win!")

    elif gameBoardArr[6] == gameBoardArr[7] == gameBoardArr[8]:
        print("You Win!")

    #cover verticals
    elif gameBoardArr[0] == gameBoardArr[3] == gameBoardArr[6]:
        print("You Win!")

    elif gameBoardArr[1] == gameBoardArr[4] == gameBoardArr[7]:
        print("You Win!")

    elif gameBoardArr[2] == gameBoardArr[5] == gameBoardArr[8]:
        print("You Win!")

    #cover diagonals
    elif gameBoardArr[0] == gameBoardArr[4] == gameBoardArr[8]:
        print("You Win!")

    elif gameBoardArr[2] == gameBoardArr[4] == gameBoardArr[6]:
        print("You Win!")

    else:
        print("Keep playing!")


#runs the program
main()
