from random import randrange

board = [1, 2, 3, 4, 'X', 6, 7, 8, 9]
#computer moves first and always picks 5
moves = 0
X = 'X'
O = 'O'

print("Hello and welcome to tic-tac-toe. You are O and the computer is X. The computer goes first. Have fun.")

def checkboard():
    print(" ")
    print(' ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('-----------')
    print(' ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('-----------')
    print(' ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))
    print(" ")

def player_move():
    while True:
        x = int(input("Please enter your move from 1-9: "))
        if x in range(1,10):
            if x in board:
                board[x-1] = 'O'
                break
            else: print(str(x) + " is already taken.")
        else: print("Please enter a valid move from 1-9. ")

def npc_move():
  while True:
    npcMove = randrange(0, 9)
    if board[npcMove] != 'O':
        if board[npcMove] != 'X':
            board[npcMove] = "X"
            print("Computer has chosen tile " + str(npcMove+1))
            break

def check_win(board, z):
   if board[0] == board[1] == board[2] == z or board[3] == board[4] == board[5] == z or  board[6] == board[7] == board[8] == z or board[0] == board[3] == board[6] == z or board[1] == board[4] == board[7] == z or board[2] == board[5] == board[8] == z or board[0] == board[4] == board[8] == z or board[2] == board[4] == board[6] == z:
        return True
   else: return False

def game():
    checkboard()
    while moves < 9:
        player_move()
        if check_win(board, O) == True:
            print("You won.")
            checkboard()
            break
        moves += 1
        checkboard()

        if moves == 9:
            print("Nobody won.")
         break

        npc_move()
        if check_win(board, X) == True:
            print("You lose.")
            break
        checkboard()
        moves += 1
        checkboard()

        if moves == 9:
            print("Nobody won.")
            
game()
