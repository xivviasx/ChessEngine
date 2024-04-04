from piece import Piece
from board import Board
from square import Square
class Knight(Piece):
    def knight_moves(self, piece, row, column):
        self.possible_moves = [
            (row + 2, column - 1),
            (row + 2, column + 1),
            (row + 1, column + 2),
            (row - 1, column + 2),
            (row - 2, column + 1),
            (row - 2, column - 1),
            (row - 1, column - 2),
            (row + 1, column - 2)
        ]
        for self.possible_move in self.possible_moves:
            self.possible_row, self.possible_column = self.possible_move
            if Square.on_board(self.possible_row, self.possible_column):
                if self.board.boardlist[self.possible_row][self.possible_column].empty_or_rival(piece.color):
                    self.final = (self.possible_row, self.possible_column)
                    piece.add_moves(self.final)
