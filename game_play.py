import pygame
from car import Car
from world import World
from camera import Camera
from ui import UI
from collectible import Collectible

class GamePlay:
    def __init__(self, game, selected_car_data):
        self.game = game
        self.screen = game.screen

        # Create game objects
        self.world = World()
        self.player_car = Car(400, 300, selected_car_data, self.world)
        self.camera = Camera(self.world.width, self.world.height)
        self.ui = UI(self.world, self.player_car)

        # Game state
        self.score = 0

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collectibles = self.world.collectibles
        self.all_sprites.add(self.player_car)
        self.all_sprites.add(self.collectibles)
        self.all_sprites.add(self.world.traffic_lights)


    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game.state_stack.pop()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player_car.update(keys)
        self.world.traffic_lights.update()
        self.camera.update(self.player_car)

        # Check for collisions
        collided_collectibles = pygame.sprite.spritecollide(self.player_car, self.collectibles, True)
        for collectible in collided_collectibles:
            self.score += 10
            new_collectible = Collectible(self.world)
            self.collectibles.add(new_collectible)
            self.all_sprites.add(new_collectible)

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.world.draw(self.screen, self.camera)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        self.ui.draw(self.screen, self.score, self.player_car.velocity.x)
        pygame.display.flip()
