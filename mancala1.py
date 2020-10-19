
#Check invalid movements, thats not working

import numpy as np
#ya
def printBoard(board):
    s1, s2 = " ", " "
    s3 = str(board[0])
    for i in range(6):
        s1 = s1 + str(board[len(board) - i - 1]) + " "
        s2 = s2 + str(board[i + 1]) + " "
        s3 = s3 + "  "
    print(s1)
    print(s3+str(board[7]))
    print(s2)
#ya
def makeMove(pos, player, board):
    turn = False
    correction = 0
    mancalas = board[(player * 7) + pos]
    board[(player * 7) + pos] = 0
    for i in range(mancalas):
        currentPos = ((player * 7) + pos + 1 + i + correction) % 14
        # no agregar al contricantes
        if (currentPos % 7 == 0 and (currentPos % 14) // 7 == player):
            correction+= 1
            currentPos = ((player * 7) + pos + 1 + i + correction) % 14
        if (i == mancalas - 1):
            #Termino en el lugar adecuado
            if (currentPos % 7 == 0):
                turn = True
            #Robar piezas? Vacio, que no sea de inicio, y que sea mio 
            elif (board[currentPos] == 0 and currentPos // 7 == player and board[14 - currentPos] != 0):
                board[currentPos] = -1
                board[((player+1)%2)*7] += board[14 - currentPos] + 1
                board[14 - currentPos] = 0   
        board[currentPos] +=1
    return board, turn
#ya
def isGameFinished(board):
    return (sum(board) - (board[0] + board[7]) == 0)
#ya
def transferPieces(board):
    sl1, sl2 = sum(board[1:7]), sum(board[8:14])
    if (sl1 == 0 and sl2 != 0):
        board[8:14] = [0,0,0,0,0,0]
        board[0] += sl2
    elif (sl2 == 0 and sl1 != 0):
        board[1:7] = [0,0,0,0,0,0]
        board[7] += sl1
    return board
#ya
def didWin(player, board):
    pos = [7, 0]
    return board[pos[player]] > board[pos[(player + 1) % 2]]
#ya