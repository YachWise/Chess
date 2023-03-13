import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config
class Game:
    
    def __init__(self):
        self.next_player = 'white'
        self.board  = Board()
        self.dragger = Dragger()
        self.config = Config()

    def show_bg(self, surface):
        theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = theme.bg.light
                else:
                    color = theme.bg.dark

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):

                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture()

                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        theme = self.config.theme
        if self.dragger.dragging:
            piece = self.dragger.piece
            #show moves for this piece

            for move in piece.moves:
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark

                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.config.theme
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    def change_theme(self):
        self.config.change_theme()
    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play
        else:
            self.config.move_sound.play
    def reset(self):
        self.__init__()
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'