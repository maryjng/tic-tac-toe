class board:
  def __init__(self):
    self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.moves = 0

  def checkboard(self):
    print(" ")
    print(' ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('-----------')
    print(' ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('-----------')
    print(' ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))
    print(" ")

    def check_win(self):
       if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or  board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            return True
       else: return False

    def update_move(self):
        self.moves += 1
        if self.moves >= 9:

class player():
    def __init__(self, name, piece):
      self.name = name
      self.piece = piece

  def player_move():
    while True:
        x = int(input("Please enter your move from 1-9: "))
        if x in range(1,10):
            if x in board:
                board[x-1] = self.piece
                break
            else: print(str(x) + " is already taken.")
        else: print("Please enter a valid move from 1-9. ")

class npc():
    def __init__(self):
        self.

    def npc_move():
        while True:
            npcMove = randrange(0, 9)
            if board[npcMove] != 'O':
                if board[npcMove] != 'X':
                    board[npcMove] = self.npcpiece
                    print("Computer has chosen tile " + str(npcMove+1))
                    break
