from random import randrange

def checkboard():
    print(' ')
    print('--------------')
    print(board[(0, 0)], ' | ',board[(0, 1)], ' | ',board[(0, 2)])
    print('--------------')
    print(board[(1, 0)], ' | ',board[(1, 1)], ' | ',board[(1, 2)])
    print('--------------')
    print(board[(2, 0)], ' | ',board[(2, 1)], ' | ',board[(2, 2)])
    print('--------------')
    print(' ')
    print('=============='/n)

def player_move():
  while y == True:
        x = int(input("Please enter your move from 1-9: "))
        if x in range(1,10):
            # for i, j in board:
            #     if j == x:
            #         board.get(i, 0)
            #         board[i] = x
                    y = False
                else: print(x , " is already taken.")
        else: print("Please enter a valid move from 1-9. ")

def npc_move():
  while True:
    # npcMove = randrange(1, 10)
    # for k in board:
    #     if board[k] == npcMove:
    #         board[k] = npc_move
            break

def check_win(board, z):
   if board[(0, 0)] == board[(0, 1)] == board[(0, 2)] == z or board[(1, 0)] == board[(1, 1)] == board[(1, 2)] == z or  board[(2, 0)] == board[(2, 1)] == board[(2, 2)]== z or board[(0, 0)] == board[(1, 0)] == board[(2, 0)] == z or board[(0, 1)] == board[(1, 1)] == board[(2, 1)] == z or board[(0, 2)] == board[(1, 2)] == board[(2, 2)] == z or board[(0, 0)] == board[(1, 1)] == board[(2, 2)] == z or board[(0, 2)] == board[(1, 1)] == board[(2, 0)] == z:
        return True
   else: return False

 # board = [[" " for i in range(4)] for j in range(4)]

board = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}

moves = 0

print("Hello and welcome to tic-tac-toe. You are O and the computer is X. The computer goes first. Have fun.")
checkboard()

while moves < 9:
    npc_move()
    if check_win(board, X) == True:
        print("You lose.")
        checkboard()
        break
    moves += 1
    checkboard()

    if moves == 9:
        print("Nobody won.")
        break

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
