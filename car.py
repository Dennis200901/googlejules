import pygame
import math

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Topdown_vehicle_sprites_pack/Black_viper.png').convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0

        self.max_speed = 5
        self.acceleration = 0.2
        self.deceleration = 0.1
        self.steering = 3

    def update(self, keys):
        # Input handling
        if keys[pygame.K_UP]:
            self.velocity.x += self.acceleration
        elif keys[pygame.K_DOWN]:
            self.velocity.x -= self.acceleration
        else:
            # Apply deceleration when no acceleration key is pressed
            if self.velocity.x > 0:
                self.velocity.x = max(0, self.velocity.x - self.deceleration)
            else:
                self.velocity.x = min(0, self.velocity.x + self.deceleration)

        # Clamp speed
        self.velocity.x = max(-self.max_speed / 2, min(self.max_speed, self.velocity.x))

        # Steering
        if self.velocity.x != 0:
            if keys[pygame.K_LEFT]:
                self.angle += self.steering
            if keys[pygame.K_RIGHT]:
                self.angle -= self.steering

        # Update position
        self.position.x += self.velocity.x * math.cos(math.radians(self.angle))
        self.position.y -= self.velocity.x * math.sin(math.radians(self.angle))

        # Update rect and image rotation
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
