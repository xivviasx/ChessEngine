class Square:
    def __init__(self, row, column, piece=None):
        self.row = row
        self.column = column
        self.piece = piece
    def has_piece(self):
        if self.piece is None:
            return False
        else:
            return True
    def is_rival(self, color):
        if self.has_piece() is True and self.piece.color != color:
            return True
    def empty_or_rival(self, color):
        if self.is_rival(color) is True or self.has_piece() is False:
            return True
        else:
            return False
    @staticmethod
    def on_board(row, column):
        if row < 0 or row > 7:
            return False
        if column < 0 or column > 7:
            return False
        return True