import pygame
import random
from settings import TILE_SIZE

class Collectible(pygame.sprite.Sprite):
    def __init__(self, world):
        super().__init__()

        self.world = world

        # Create a placeholder image for the money bundle
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
        self.image.fill((0, 255, 0)) # Green color for money

        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        # Find a random road tile to spawn on
        while True:
            row = random.randint(0, self.world.tile_height - 1)
            col = random.randint(0, self.world.tile_width - 1)
            if self.world.tile_map[row][col] == 'R':
                self.rect.centerx = col * TILE_SIZE + TILE_SIZE // 2
                self.rect.centery = row * TILE_SIZE + TILE_SIZE // 2
                break

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))
