class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.valid_moves = [] #dostępne ruchy dla figury
        self.moved = False #informacja czy figura wykonała już swój pierwszy ruch, potrzebne do policzenia ruchow pawn
        if color == 'white':
            self.pawn_direction = -1
        else:
            self.pawn_direction = 1
    def add_moves(self, move):
        self.valid_moves.append(move)
    def delete_moves(self):
        self.valid_moves = []


