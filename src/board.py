from const import *
from square import Square
from piece import *
class Board: 
    def __init__(self):
         #creates the board 
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLUMNS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    #_ to denote private methods
    def _create(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)

        #creates the pawns
        for col in range(COLUMNS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        #create the knights
        self.squares[row_other][1] = Square(row_other,1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        #create the bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        #create the rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        #create the quueens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        #create the kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))
