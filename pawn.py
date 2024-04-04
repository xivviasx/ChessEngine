from piece import Piece
from board import Board
from square import Square
class Pawn(Piece):
    def pawn_moves(self, piece, row, column):
        if piece.moved == True:
            self.steps = 1
        else:
            self.steps = 2

        if self.steps == 2:
            self.final = row + (piece.pawn_direction * (self.steps))
            self.previous = row + (piece.pawn_direction * (self.steps - 1))
            if Square.on_board(self.final, column) is True:
                if self.board.boardlist[self.final][column].has_piece() is False:
                    if self.board.boardlist[self.previous][column].has_piece() is False:
                        piece.add_moves((self.final, column))
            self.steps = 1
        self.final = row + (piece.pawn_direction * (self.steps))
        if Square.on_board(self.final, column) is True and self.board.boardlist[self.final][column].has_piece() is False:
            piece.add_moves((self.final, column))

        # diagonal
        self.possible_row = row + piece.pawn_direction
        self.possible_columns = []
        self.possible_columns = [column - 1, column + 1]
        for possible_column in self.possible_columns:
            if Square.on_board(self.possible_row, possible_column) is True:
                if self.board.boardlist[self.possible_row][possible_column].is_rival(piece.color) is True:
                    piece.add_moves((self.possible_row, possible_column))
