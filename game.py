from board import Board
from move import Move
class Game:
    def __init__(self):
        self.board = Board()
    def printBoard(self):
        self.b = []
        for row in range(8):
            if row == 0: self.b.append('0')
            if row == 1: self.b.append('1')
            if row == 2: self.b.append('2')
            if row == 3: self.b.append('3')
            if row == 4: self.b.append('4')
            if row == 5: self.b.append('5')
            if row == 6: self.b.append('6')
            if row == 7: self.b.append('7')
            for column in range(8):
                if self.board.boardlist[row][column].has_piece():
                    self.piece = self.board.boardlist[row][column].piece.name
                    self.color=self.board.boardlist[row][column].piece.color
                    if self.piece == 'rook':
                        if self.color =='white':
                            self.b.append('r')
                        else: self.b.append('R')
                    elif self.piece == 'pawn':
                        if self.color =='white':
                            self.b.append('p')
                        else:
                            self.b.append('P')
                    elif self.piece == 'knight':
                        if self.color =='white':
                            self.b.append('h')
                        else:
                            self.b.append('H')
                    elif self.piece == 'bishop':
                        if self.color =='white':
                            self.b.append('b')
                        else:
                            self.b.append('B')
                    elif self.piece == 'queen':
                        if self.color =='white':
                            self.b.append('q')
                        else:
                            self.b.append('Q')
                    elif self.piece == 'king':
                        if self.color =='white':
                            self.b.append('k')
                        else:
                            self.b.append('K')
                else:
                    self.b.append(' ')
            print(self.b)
            self.b = []
        self.b.append(' ')
        self.b.append('A')
        self.b.append('B')
        self.b.append('C')
        self.b.append('D')
        self.b.append('E')
        self.b.append('F')
        self.b.append('G')
        self.b.append('H')
        print(self.b)
        print('')
    def currently_available_moves(self): #obliczenie dostępnych ruchów dla wszystkich figur
        for row in range(8):
            for column in range(8):
                if self.board.boardlist[row][column].has_piece():
                    self.piece = self.board.boardlist[row][column].piece
                    Move.calc_moves(self, self.piece, row, column)
    def nextMove(self, ruch):
        #sprawdzenie ruchu przeciwnika
        if ruch == None:
            self.currently_available_moves()
            return Move.move_boot(self, 'black') #wykonanie naszego ruchu i zwrócenie go
        else:
            self.color = Move.move_rival(self, ruch) #wykonanie ruchu rywala, funkcja zwaraca kolor rywala
            self.currently_available_moves()
            return Move.move_boot(self, self.color) #wykonanie naszego ruchu i zwrócenie go