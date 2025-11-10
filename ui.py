import pygame

class UI:
    def __init__(self, world, player):
        # Font setup
        self.font = pygame.font.Font(None, 36) # Use default font, size 36
        self.world = world
        self.player = player

        # Minimap setup
        self.minimap_scale = 5
        self.minimap_width = self.world.tile_width * self.minimap_scale
        self.minimap_height = self.world.tile_height * self.minimap_scale
        self.minimap_surface = pygame.Surface((self.minimap_width, self.minimap_height))
        self.minimap_pos = (10, 100) # Position on the screen

    def draw_text(self, screen, text, x, y):
        text_surface = self.font.render(text, True, (255, 255, 255)) # White color
        screen.blit(text_surface, (x, y))

    def draw_minimap(self, screen):
        # Draw the world tiles on the minimap surface
        for row_index, row in enumerate(self.world.tile_map):
            for col_index, tile in enumerate(row):
                x = col_index * self.minimap_scale
                y = row_index * self.minimap_scale
                color = (100, 100, 100) if tile == 'R' else (50, 50, 50)
                pygame.draw.rect(self.minimap_surface, color, (x, y, self.minimap_scale, self.minimap_scale))

        # Draw the player on the minimap
        player_x = int(self.player.position.x / self.world.width * self.minimap_width)
        player_y = int(self.player.position.y / self.world.height * self.minimap_height)
        pygame.draw.circle(self.minimap_surface, (255, 0, 0), (player_x, player_y), 3) # Red circle for player

        # Draw the minimap surface onto the screen
        screen.blit(self.minimap_surface, self.minimap_pos)

    def draw(self, screen, score, speed):
        # Draw score
        self.draw_text(screen, f"Score: {score}", 10, 10)

        # Draw speed
        speed_text = f"Speed: {abs(speed):.1f}"
        self.draw_text(screen, speed_text, 10, 50)

        # Draw minimap
        self.draw_minimap(screen)
