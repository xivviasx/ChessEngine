from square import Square
from piece import Piece
class Board:
    def __init__(self):
        #utworzenie listy przechowującej obiekty square
        self.boardlist = [[0, 0, 0, 0, 0, 0, 0, 0] for x in range(8)]

        #creating board
        for row in range(8):
            for column in range(8):
                self.boardlist[row][column] = Square(row, column)
        self._add_pieces('white')
        self._add_pieces('black')
    def _add_pieces(self, color):
        if color == 'white':
            self.pawn_row = 6
            self.other_row = 7
        else:
            self.pawn_row = 1
            self.other_row = 0
        #pawns
        for column in range(8):
            self.boardlist[self.pawn_row][column] = Square(self.pawn_row, column, Piece("pawn", color))
        #rooks
        self.boardlist[self.other_row][0] = Square(self.other_row, 0, Piece("rook", color))
        self.boardlist[self.other_row][7] = Square(self.other_row, 7, Piece("rook", color))
        #knigths
        self.boardlist[self.other_row][1] = Square(self.other_row, 1, Piece("knight", color))
        self.boardlist[self.other_row][6] = Square(self.other_row, 6, Piece("knight", color))
        #bishops
        self.boardlist[self.other_row][2] = Square(self.other_row, 2, Piece("bishop",color))
        self.boardlist[self.other_row][5] = Square(self.other_row, 5, Piece("bishop",color))
        #queen
        self.boardlist[self.other_row][3] = Square(self.other_row, 3, Piece("queen", color))
        #king
        self.boardlist[self.other_row][4] = Square(self.other_row, 4, Piece("king", color))

