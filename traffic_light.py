import pygame
from settings import TILE_SIZE

class TrafficLight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE // 4, TILE_SIZE // 4))
        self.rect = self.image.get_rect(center=(x, y))

        self.state = 'green'
        self.timer = 0
        self.green_duration = 300 # 5 seconds at 60 FPS
        self.red_duration = 300 # 5 seconds at 60 FPS

        self.update_color()

    def update(self):
        self.timer += 1
        if self.state == 'green' and self.timer > self.green_duration:
            self.state = 'red'
            self.timer = 0
            self.update_color()
        elif self.state == 'red' and self.timer > self.red_duration:
            self.state = 'green'
            self.timer = 0
            self.update_color()

    def update_color(self):
        if self.state == 'green':
            self.image.fill((0, 255, 0))
        else:
            self.image.fill((255, 0, 0))
