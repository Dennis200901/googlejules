import pygame
from collectible import Collectible
from traffic_light import TrafficLight
from settings import TILE_SIZE

class World:
    def __init__(self):
        self.tile_map = []
        with open('map.txt', 'r') as f:
            for line in f:
                self.tile_map.append(line.strip())

        self.tile_width = len(self.tile_map[0])
        self.tile_height = len(self.tile_map)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

        self.road_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.road_tile.fill((100, 100, 100)) # Dark grey for road
        self.building_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.building_tile.fill((50, 50, 50)) # Darker grey for building
        self.sidewalk_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.sidewalk_tile.fill((150, 150, 150)) # Light grey for sidewalk

        self.solids = pygame.sprite.Group()
        self.traffic_lights = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()

        for row_index, row in enumerate(self.tile_map):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if tile == 'B':
                    solid = pygame.sprite.Sprite()
                    solid.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    self.solids.add(solid)
                elif tile == 'T':
                    light = TrafficLight(x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                    self.traffic_lights.add(light)

        for _ in range(20): # More collectibles for a larger map
            self.collectibles.add(Collectible(self))


    def draw(self, screen, camera):
        for row_index, row in enumerate(self.tile_map):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                if tile == 'R':
                    screen.blit(self.road_tile, camera.apply(rect))
                elif tile == 'B':
                    screen.blit(self.building_tile, camera.apply(rect))
                elif tile == 'S' or tile == 'T': # Draw sidewalk under traffic lights
                    screen.blit(self.sidewalk_tile, camera.apply(rect))

        for light in self.traffic_lights:
            screen.blit(light.image, camera.apply(light))
