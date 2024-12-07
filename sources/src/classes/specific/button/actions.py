import pygame
import sys


class ButtonActions:
    def __init__(self, game_loop):
        self.game_loop = game_loop

    def pause_game(self):
        self.game_loop.paused = True
        self.game_loop.ui_manager.set_buttons(self.game_loop.pause_buttons)
        print("Game paused")

    def unpause_game(self):
        self.game_loop.paused = False
        self.game_loop.ui_manager.set_buttons(self.game_loop.default_buttons)
        print("Game unpaused")

    def quit_game(self):
        pygame.quit()
        sys.exit()
