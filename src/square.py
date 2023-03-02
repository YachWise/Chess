class Square:
    
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def has_piece(self):
        return self.piece != None
    
    def isEmpty(self):
        return self.has_piece()
    
    def has_team(self, color):
        return self.has_piece() and self.piece.color == color

    #sq has a piece and that piece does not match your color 
    def has_enemy(self, color):
        return self.has_piece() and self.piece.color != color
    def empty_or_enemy(self, color):
        return self.isEmpty() or self.has_enemy(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            #outside board
            if arg < 0 or arg > 7:
                return False
        #made through full loop without false, can return true
        return True
