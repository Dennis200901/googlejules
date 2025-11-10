import pygame
import sys
from start_screen import StartScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("GTA 2 Style Car Game")
        self.clock = pygame.time.Clock()
        self.states = {}
        self.state_stack = []

    def run(self):
        self.state_stack.append(StartScreen(self))

        while self.state_stack:
            self.state_stack[-1].run()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
