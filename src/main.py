import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move

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
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():

                #user clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    print(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col)
                            print(piece)
                            #save position if the user clicked on a piece
                            dragger.start_pos(event.pos)
                            dragger.drag_piece(piece)

                            game.show_bg(screen)
                            game.show_moves(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)

                #user moved mouse
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                #user let go of MB1
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SQSIZE
                        release_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.start_row, dragger.start_col)
                        final = Square(released_row, release_col)

                        move = Move(initial, final)

                        if board.valid_moves(dragger.piece, move):
                            board.move(dragger.piece, move)
                            game.show_bg(screen)
                            #game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.next_turn()
                    dragger.undrag_piece()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        game.change_theme()

                #user pressed x in top right
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()   


main = Main()

main.mainloop()