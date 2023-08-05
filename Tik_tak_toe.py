import random


board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = 'X'
winner = None
gameRunning = True


#starting information and title

print("WELCOME TO TIC TAK TOE!")

def boardStr():
    print("The structure of board is as follows >>")
    print("1" + " | " + "2" + " | " + "3")
    print("--|---|---")
    print("4" + " | " + "5" + " | " + "6")
    print("--|---|---")
    print("7" + " | " + "8" + " | " + "9") 
    print("NOTE : if your move is invalid computer will finish its move.... Be careful which cell you choose ")

boardStr()    

#play with computer?
ask = int(input("Play with computer?? (yes >> 1 no >> 2):"))


#printing board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|---")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|---")
    print(board[6] + " | " + board[7] + " | " + board[8]) 
    
    
#Taking input from player

def playerInput(board):
    inpt = int(input("Enter a number between 1-9: "))
    
    if inpt >= 1 and inpt <= 9 and board[inpt-1] == "-":
        board[inpt-1] = currentPlayer
        
    else:
        print("invalid move!")    

#check for win or tie

def checkCol(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[5] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
    
def checkdia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[3] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("ITS A TIE!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkCol(board) or checkRow(board) or checkdia(board):
        print(f"CONGRATULATION!! the winner is {winner}")
        printBoard(board)
        gameRunning = False
        
        
    
    
    
#switch player

def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
if ask == 1:        
    def computer(board):
        while currentPlayer == 'O':
            position = random.randint(0,8)
            if board[position] == "-":
                board[position] = 'O'
                switchPlayer()


#check for win or tie

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    if ask == 1:
        computer(board)
    checkWin()
    checkTie(board)
    
    
    



