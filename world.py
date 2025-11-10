import pygame

# Define tile size
TILE_SIZE = 64

class World:
    def __init__(self):
        self.tile_map = [
            'BBBBBBBBBBBBBBBBBBBB',
            'BRRRRRRRRRRRRRRRRRRB',
            'BRBBBRBBBRBBBRBBBRRB',
            'BRBRRRBRRRBRRRBRRRRB',
            'BRBRBBBRBBBRBBBRBBRB',
            'BRRRRRRRRRRRRRRRRRRB',
            'BRBBBRBBBRBBBRBBBRRB',
            'BRRBRRRBRRBRRBRRRBRB',
            'BRBBRBBRBBRBBRBBRBBRB',
            'BRRRRRRRRRRRRRRRRRRB',
            'BBBBBBBBBBBBBBBBBBBB',
        ]

        self.tile_width = len(self.tile_map[0])
        self.tile_height = len(self.tile_map)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

        self.road_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.road_tile.fill((100, 100, 100)) # Dark grey for road
        self.building_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.building_tile.fill((50, 50, 50)) # Darker grey for building

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
