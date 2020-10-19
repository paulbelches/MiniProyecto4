import numpy as np

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

def isGameFinished(board):
    return (sum(board) - (board[0] + board[7]) == 0)

def transferPieces(board):
    sl1, sl2 = sum(board[1:7]), sum(board[8:14])
    if (sl1 == 0 and sl2 != 0):
        board[8:14] = [0,0,0,0,0,0]
        board[0] += sl2
    elif (sl2 == 0 and sl1 != 0):
        board[1:7] = [0,0,0,0,0,0]
        board[7] += sl1
    return board

def didWin(player, board):
    pos = [7, 0]
    return board[pos[player]] > board[pos[(player + 1) % 2]]

def simulateGame(player, board):
    firstMove = -1
    while (not(isGameFinished(board))):
        randomInt = np.random.randint(6) + 1
        while(board[(player * 7) + randomInt] == 0):
            randomInt = np.random.randint(6) + 1
        if (firstMove == -1):
            firstMove = randomInt
        board, flag = makeMove(randomInt, player, board)
        if (not(flag)):
            player = (player + 1) % 2
        board = transferPieces(board)
    return board, firstMove    

def nextMove(player, initialBoard, iterations):
    win = [0,0,0,0,0,0]
    trials = [1,1,1,1,1,1]
    for i in range(iterations):
        board = initialBoard.copy()
        board, firstMove = simulateGame(player, board)
        trials[firstMove - 1] += 1
        if(didWin(player, board)):
            win[firstMove - 1] += 1
    return np.argmax(np.array(win) / np.array(trials)) + 1

nivel = [0, 500, 10000]
board = [0, 4,4,4,4,4,4, 0, 4,4,4,4,4,4]

menu = True

while(menu): 
    print("Menú")
    print("1. CPU vs Player")
    print("2. Player vs Player")
    print("3. Salir")
    m = input("Ingrese la modalidad (1-3): ")
    if (m == "1"):
        lv = -1
        while(not(lv >= 0 and lv <= 2)):
            print("1. Fácil")
            print("2. Intermedio")
            print("3. Difícil")
            lv = input("Ingrese el nivel (1-3): ")
            try:
                lv = int(lv) - 1
            except:
                print("Ingrese un número")
                lv = -1
        player = np.random.randint(2)
        printBoard(board)
        while (not(isGameFinished(board))):
            if (player):
                correctMove = False
                while (not(correctMove)):
                    try: 
                        pos = int(input("Ingrese que desea realizar (1-6): "))
                        if (pos >= 1 and pos <= 6):
                            if (board[pos] != 0):
                                correctMove = True
                            else:
                                print("Ingrese una jugada válida")
                        else:              
                            print("Ingrese una jugada válida")
                    except:
                        print("Ingrese un número")
                        pos = -1
                board, flag = makeMove(int(pos), 0, board)
                if (not(flag)):
                    player = not(player)
                print("Persona")
                printBoard(board)
            else: 
                boardCopy = board.copy()
                pos = nextMove(1, board, nivel[lv])
                board = boardCopy
                board, flag = makeMove(pos, 1, board)
                if (not(flag)):
                    player = not(player)
                print("Compu")
                printBoard(board)
            board = transferPieces(board)
        printBoard(board)
    elif (m == "2"):
        player = True
        printBoard(board)
        while (not(isGameFinished(board))):
            if (player):
                print("Jugador 1")
                correctMove = False
                while (not(correctMove)):
                    try: 
                        pos = int(input("Ingrese que desea realizar (1-6): "))
                        if (pos >= 1 and pos <= 6):
                            if (board[pos] != 0):
                                correctMove = True
                            else:
                                print("Ingrese una jugada válida")
                        else:              
                            print("Ingrese una jugada válida")
                    except:
                        print("Ingrese un número")
                        pos = -1
                board, flag = makeMove(int(pos), 0, board)
                if (not(flag)):
                    player = not(player)
                printBoard(board)
            else: 
                print("Jugador 2")
                correctMove = False
                while (not(correctMove)):
                    try: 
                        pos = int(input("Ingrese que desea realizar (1-6): "))
                        if (pos >= 1 and pos <= 6):
                            if (board[pos + 7] != 0):
                                correctMove = True
                            else:
                                print("Ingrese una jugada válida")
                        else:              
                            print("Ingrese una jugada válida")
                    except:
                        print("Ingrese un número")
                        pos = -1
                board, flag = makeMove(int(pos), 1, board)
                if (not(flag)):
                    player = not(player)
                printBoard(board)
            board = transferPieces(board)
        printBoard(board)
    elif (m == "3"):
        menu = False
