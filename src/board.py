from const import *
from square import Square
from piece import *
from move import Move

class Board: 
    def __init__(self):
         #creates the board 
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLUMNS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
        self.last_move = None
    #_ to denote private methods
    def valid_moves(self, piece, move):
        return move in piece.moves
    
    def move(self, piece, move):
        initial = move.initial
        final = move.final 

        #move logically before ui 
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        piece.moved = True
        piece.clear_moves()

        self.last_move = move

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
        #demo piece in middle of board self.squares[4][4] = Square(4, 4, Bishop('black'))

        #create the rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        #create the quueens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        #create the kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))

    def calc_moves(self, piece, row, col):
            def pawn_moves():
                        #up and down movement
                        steps = 1 if piece.moved else 2

                        start = row + piece.dir
                        end = row + (piece.dir * (1 + steps))
                        for move_row in range(start, end, piece.dir):
                            if Square.in_range(move_row):
                                if self.squares[move_row][col].isEmpty():
                                    initial = Square(row, col)
                                    final = Square(move_row, col)
                                    move = Move(initial, final)
                                    piece.add_move(move)
                                else: break
                            else: break

                        #diag movement
                        move_row = row + piece.dir
                        move_cols = [col-1, col+1]
                        for move_col in move_cols:
                            if Square.in_range(move_row, move_col):
                                if self.squares[move_row][move_col].has_enemy(piece.color):
                                    #an enemy is in the square
                                    initial = Square(row, col)
                                    final = Square(move_row, move_col)
                                    move = Move(initial, final)
                                    piece.add_move(move)
                                    #this is allowed
            def straight_movement(moves):
                for move in moves:
                    row_inc, col_inc = move
                    move_row = row + row_inc
                    move_col = col + col_inc
                    while True:
                        if Square.in_range(move_row, move_col):
                            initial = Square(row, col)
                            final = Square(move_row, move_col)
                            move = Move(initial, final)

                            #empty square
                            if self.squares[move_row][move_col].isEmpty():
                                piece.add_move(move)
                            #enemy square, break after one enemy
                            if self.squares[move_row][move_col].has_enemy(piece.color):
                                piece.add_move(move)
                                break
                            if self.squares[move_row][move_col].has_team(piece.color):
                                break
                        else: break
                        move_row, move_col = move_row + row_inc, move_col + col_inc
            def knight_moves():
                # 8 possible moves
                possible_moves = [
                    (row-2, col+1),
                    (row-1, col+2),
                    (row+1, col+2),
                    (row+2, col+1),
                    (row+2, col-1),
                    (row+1, col-2),
                    (row-1, col-2),
                    (row-2, col-1),
                ]

                for possible_move in possible_moves:
                    possible_move_row, possible_move_col = possible_move

                    if Square.in_range(possible_move_row, possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].empty_or_enemy(piece.color):
                            # create squares of the new move
                            initial = Square(row, col)
                            final_piece = self.squares[possible_move_row][possible_move_col].piece
                            final = Square(possible_move_row, possible_move_col, final_piece)
                            # create new move
                            move = Move(initial, final)
                            piece.add_move(move)
            def king_moves():
                adjacentSq = [
                    (row-1,col),
                    (row-1, col+1),
                    (row,col+1),
                    (row+1,col+1),
                    (row+1,col),
                    (row+1,col-1),
                    (row, col-1),
                    (row-1,col-1),
                    ]
                for move in adjacentSq:
                    move_row, move_col = move
                    if Square.in_range(move_row, move_col):
                        if self.squares[move_row][move_col].empty_or_enemy(piece.color):
                        # create squares of the new move
                            initial = Square(row, col)
                            final_piece = self.squares[move_row][move_col].piece
                            final = Square(move_row, move_col, final_piece)
                            # create new move
                            move = Move(initial, final)
                            piece.add_move(move)
        #pawn check
            if isinstance(piece, Pawn):
                pawn_moves()
            elif isinstance(piece, Knight):
                knight_moves()
            elif isinstance(piece, Bishop):
                straight_movement([
                    (-1,1),
                    (-1,-1),
                    (1,1),
                    (1,-1)])
            elif isinstance (piece, Rook):
                straight_movement([
                    (-1,0),
                    (0,1),
                    (1,0),
                    (0,-1)])
            elif isinstance (piece, Queen):
                straight_movement([
                    (-1,-1),
                    (-1,-1),
                    (1,1),
                    (1,-1),
                    (-1,0),
                    (0,1),
                    (1,0),
                    (0,-1)])
            elif isinstance (piece, King):
                king_moves()
