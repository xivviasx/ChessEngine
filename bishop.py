from piece import Piece
from board import Board
from square import Square
class Bishop(Piece):
    def bishop_moves(self, piece, row, column):
        self.direction = [
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1)
        ]
        for dir in self.direction:
            self.left, self.right = dir
            self.possible_row = row + self.left
            self.possible_column = column + self.right
            while True:
                if Square.on_board(self.possible_row, self.possible_column) is True:
                    if self.board.boardlist[self.possible_row][self.possible_column].has_piece() is False:
                        piece.add_moves((self.possible_row, self.possible_column))
                        self.possible_row = self.possible_row + self.left
                        self.possible_column = self.possible_column + self.right
                    elif self.board.boardlist[self.possible_row][self.possible_column].is_rival(piece.color) is True:
                        piece.add_moves((self.possible_row, self.possible_column))
                        break
                    else:
                        break
                else:
                    break