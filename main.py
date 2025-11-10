import pygame
from car import Car
from world import World
from camera import Camera
from ui import UI
from collectible import Collectible

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GTA 2 Style Car Game")

# Create game objects
world = World()
player_car = Car(400, 300)
camera = Camera(world.width, world.height)
ui = UI(world, player_car)

# Game state
score = 0

# Create sprite groups
all_sprites = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

all_sprites.add(player_car)

# Create some collectibles
for _ in range(5):
    collectible = Collectible(world)
    collectibles.add(collectible)
    all_sprites.add(collectible)

# Game loop variable
running = True
clock = pygame.time.Clock()

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update
    player_car.update(keys)
    camera.update(player_car)

    # Check for collisions
    collided_collectibles = pygame.sprite.spritecollide(player_car, collectibles, True)
    for collectible in collided_collectibles:
        score += 10
        new_collectible = Collectible(world)
        collectibles.add(new_collectible)
        all_sprites.add(new_collectible)

    # Draw
    screen.fill((50, 50, 50)) # Background color

    # Draw the world with camera offset
    world.draw(screen, camera)

    # Draw all sprites with camera offset
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))

    # Draw the UI
    ui.draw(screen, score, player_car.velocity.x)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
