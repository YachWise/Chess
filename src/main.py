import pygame
import sys

from const import *
from game import Game

class Main: 
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cat Chess @YachWise")
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():

                #user clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    print(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
            
                    if board.squares[clicked_row][clicked_col].has_piece():
                        print("yes")
                #user moved mouse
                elif event.type == pygame.MOUSEMOTION:
                    pass
                #user let go of MB1
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                #user pressed x in top right
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()   


main = Main()

main.mainloop()