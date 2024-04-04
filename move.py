from board import Board
from square import Square
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
import random
class Move:
    def move_rival(self, ruch):
        self.from_column = Move.letters_to__numbers(ruch[0])
        self.from_row = int(ruch[1])

        self.to_column = Move.letters_to__numbers(ruch[3])
        self.to_row = int(ruch[4])

        #update board
        self.x = self.board.boardlist[self.from_row][self.from_column].piece
        self.board.boardlist[self.from_row][self.from_column].piece = None
        self.board.boardlist[self.to_row][self.to_column].piece = self.x

        Move.pawn_promotion(self, self.x, self.to_row)
        self.board.boardlist[self.to_row][self.to_column].piece.moved = True
        return self.board.boardlist[self.to_row][self.to_column].piece.color
    def move_boot(self, color):
        #random move
        self.initial_row, self.initial_column, self.final_row, self.final_column = Move.random_valid_move(self, color)

        #update board
        self.x = self.board.boardlist[self.initial_row][self.initial_column].piece
        self.board.boardlist[self.initial_row][self.initial_column].piece = None
        Move.mat(self, self.final_row, self.final_column)
        self.board.boardlist[self.final_row][self.final_column].piece = self.x
        Move.pawn_promotion(self, self.x, self.final_row)

        # update piece
        self.board.boardlist[self.final_row][self.final_column].piece.moved = True
        self.board.boardlist[self.final_row][self.final_column].piece.delete_moves()

        self.initial_column = Move.numbers_to_letters(self.initial_column)
        self.final_column = Move.numbers_to_letters(self.final_column)
        self.ruch = str(self.initial_column) + str(self.initial_row) + ' ' + str(self.final_column) + str(self.final_row)
        return self.ruch
    def random_valid_move(self, color):
        self.boot_piece = []
        self.piece_row_column = []
        self.amount_of_pieces = 0

        # usuwanie ruchów z valid_moves, które mogłyby doprowadzić do szachowania króla
        # usuwanie ruchów z valid_moves, które nie ochronią szachowanego króla przed matem
        for r in range(0, 8):
            for c in range(0, 8):
                if self.board.boardlist[r][c].has_piece():
                    self.amount_of_pieces = self.amount_of_pieces + 1
                    if self.board.boardlist[r][c].piece.color != color:
                        self.kopia = []
                        for move in self.board.boardlist[r][c].piece.valid_moves:
                            if Move.check_szach(self, color, r, c, move[0], move[1]) is False:
                                self.kopia.append(move)
                        self.board.boardlist[r][c].piece.valid_moves = self.kopia

        if self.amount_of_pieces == 2: #jeśli na planszy zostaną tylko dwa króle to kończy się gra
            exit(0)

        #spis pól z figurami, które mają możliwość ruchu
        for r in range(8):
            for c in range(8):
                if self.board.boardlist[r][c].has_piece() and self.board.boardlist[r][c].piece.color != color:
                    if len(self.board.boardlist[r][c].piece.valid_moves) > 0:
                        self.boot_piece.append(self.board.boardlist[r][c])

        #jeśli nie ma żadnego dostępnego ruchu który nie doprowadziłby do szachowania króla
        #lub obronił króla (jeśli król jest szachowany) przed matem, to kończy się gra
        if len(self.boot_piece) == 0:
            exit(0)

        #losowanie figury z figur z dostępnymi ruchami
        self.value = random.randrange(0, len(self.boot_piece))
        self.initial_square = self.boot_piece[self.value]

        #losowanie ruchu figury
        self.move_initial_row = self.initial_square.row
        self.move_initial_column = self.initial_square.column
        self.value = random.randrange(0, len(self.initial_square.piece.valid_moves))
        self.move_final_square = self.initial_square.piece.valid_moves[self.value]
        self.move_final_row = self.move_final_square[0]
        self.move_final_column = self.move_final_square[1]

        return self.move_initial_row, self.move_initial_column, self. move_final_row, self.move_final_column
    def calc_moves(self, piece, row, column):
        piece.delete_moves()
        if piece.name == 'rook':
            Rook.rook_moves(self, piece, row, column)
            pass
        elif piece.name == 'pawn':
            Pawn.pawn_moves(self, piece, row, column)
            pass
        elif piece.name == 'knight':
            Knight.knight_moves(self, piece, row, column)
        elif piece.name == 'bishop':
            pass
            Bishop.bishop_moves(self, piece, row, column)
        elif piece.name == 'queen':
            pass
            Queen.queen_moves(self, piece, row, column,True)
            Queen.queen_moves(self, piece, row, column,False)
        elif piece.name == 'king':
            King.king_moves(self, piece, row, column)
            pass
    def pawn_promotion(self, x, final_row):
        if x.name == "pawn":
            if (final_row == 0) or (final_row == 7):
                x.name = "queen"
    def mat(self, final_row, final_column):
        if self.board.boardlist[final_row][final_column].has_piece():
            if self.board.boardlist[final_row][final_column].piece.name == 'king':
                exit(0)
        pass
    def check_szach(self, color, initial_row, initial_column, final_row, final_column):

        #zapisanie poprzedniego ustawienia tablicy i wykonanie ruchu
        self.piece = self.board.boardlist[initial_row][initial_column].piece
        self.previous_piece = self.board.boardlist[final_row][final_column].piece
        self.board.boardlist[initial_row][initial_column].piece = None
        self.board.boardlist[final_row][final_column].piece = self.piece

        #szukanie króla i liczenie dostępnych ruchów dla każdego pionka
        for r in range(8):
            for c in range(8):
                if self.board.boardlist[r][c].has_piece():
                    if self.board.boardlist[r][c].piece.color == color:
                        Move.calc_moves(self, self.board.boardlist[r][c].piece, r, c)
                    elif self.board.boardlist[r][c].piece.name == 'king':
                        self.king_position = (r, c)

        #szukanie króla w możliwych ruchach przeciwnika
        for r2 in range(8):
            for c2 in range(8):
                if self.board.boardlist[r2][c2].has_piece():
                    if self.board.boardlist[r2][c2].piece.color == color:
                        if self.king_position in self.board.boardlist[r2][c2].piece.valid_moves:
                            #przywracanie poprzednich ustawień tablicy z pionkami
                            self.board.boardlist[final_row][final_column].piece = self.previous_piece
                            self.board.boardlist[initial_row][initial_column].piece = self.piece
                            for r4 in range(8):
                                for c4 in range(8):
                                    if self.board.boardlist[r4][c4].has_piece():
                                        if self.board.boardlist[r4][c4].piece.color == color:
                                            Move.calc_moves(self, self.board.boardlist[r4][c4].piece, r4, c4)
                            return True
        #przywracanie poprzednich ustawień tablicy z pionkami
        self.board.boardlist[final_row][final_column].piece = self.previous_piece
        self.board.boardlist[initial_row][initial_column].piece = self.piece
        for r3 in range(8):
            for c3 in range(8):
                if self.board.boardlist[r3][c3].has_piece():
                    if self.board.boardlist[r3][c3].has_piece():
                        if self.board.boardlist[r3][c3].piece.color == color:
                            Move.calc_moves(self, self.board.boardlist[r3][c3].piece, r3, c3)
        return False
    @staticmethod
    def numbers_to_letters(number):
        if number == 0:
            number = "A"
        elif number == 1:
            number = "B"
        elif number == 2:
            number = "C"
        elif number == 3:
            number = "D"
        elif number == 4:
            number = "E"
        elif number == 5:
            number = "F"
        elif number == 6:
            number = "G"
        elif number == 7:
            number = "H"
        return number
    @staticmethod
    def letters_to__numbers(letter):
        if letter == 'A':
            letter = 0
        elif letter == 'B':
            letter = 1
        elif letter == 'C':
            letter = 2
        elif letter == 'D':
            letter = 3
        elif letter == 'E':
            letter = 4
        elif letter == 'F':
            letter = 5
        elif letter == 'G':
            letter = 6
        elif letter == 'H':
            letter = 7
        return letter