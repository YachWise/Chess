from const import *
from square import Square
class Board: 
    def __init__(self):
         #creates the board 
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLUMNS)]
        self._create()
    #_ to denote private methods
    def _create(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass

