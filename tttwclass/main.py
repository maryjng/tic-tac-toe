from class import *
from random import randrange


def player_pref():
    name = input("Please enter your name: ")
    piece = input("Hello " + name + " do you prefer to be X or O?")
    x = True
    while x:
        if piece in piecechoices:
            x = False
            return player(name, piece)


# X = 'X'
# O = 'O'

print("Hello and welcome to tic-tac-toe.")

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
