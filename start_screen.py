import pygame
from car_selection import CarSelection

class StartScreen:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.state_stack.pop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.running = False
                    self.game.state_stack.append(CarSelection(self.game))

    def draw(self):
        self.screen.fill((20, 20, 20)) # Dark grey background

        # Draw Title
        title_text = self.font.render("GTA 2 Style Game", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.game.screen_width / 2, self.game.screen_height / 2 - 50))
        self.screen.blit(title_text, title_rect)

        # Draw "Press Start" text
        start_text = self.small_font.render("Press Enter to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(self.game.screen_width / 2, self.game.screen_height / 2 + 50))
        self.screen.blit(start_text, start_rect)

        pygame.display.flip()
