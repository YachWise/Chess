import pygame

from const import *

class Dragger:
    def __init__(self):
        #mouse pos
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.start_row = 0
        self.start_col = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def start_pos(self, pos):
        self.start_row = pos[1] // SQSIZE
        self.start_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def update_blit(self, surface):
        #make selected piece use the larger asset
        self.piece.set_texture(size=128)

        img = pygame.image.load(self.piece.texture)

        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        surface.blit(img, self.piece.texture_rect)
