from class import *
from random import randrange


def assign_pieces():
    name = input("Please enter your name: ")
    x = True
    while x:
        piece = input("Hello " + name + " do you prefer to be X or O?")
        if piece in [X, O]:
            if piece == 'X':
                npc = npc('O')
            else npc = npc('X')
            x = False
            player = player(name, piece)
       
def betweenmoves():
   moves += 1
   board.checkboard()
   if board.check_win():
     input("Game Over. Press enter to play again.")
     return True
   if moves == 9:
     input("Nobody won! Press enter to play again.")
     return True

def game():
    while True:
        moves = 0
        board = board()
        assign_pieces()
        while True:
           player.player_move()
           if betweenmoves():
                break
           npc.npc_move()
           if betweenmoves():
                break
        
if __name__ == "__main__":
    print("Hello and welcome to tic-tac-toe.")
    game()

