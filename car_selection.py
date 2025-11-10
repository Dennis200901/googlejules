import pygame
from game_play import GamePlay

class CarSelection:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 30)

        # Define car data
        self.cars = [
            {'name': 'Black Viper', 'image': 'Topdown_vehicle_sprites_pack/Black_viper.png', 'speed': 6, 'accel': 0.3, 'steer': 4},
            {'name': 'Audi', 'image': 'Topdown_vehicle_sprites_pack/Audi.png', 'speed': 5, 'accel': 0.2, 'steer': 3},
            {'name': 'Sedan', 'image': 'Topdown_vehicle_sprites_pack/Car.png', 'speed': 4, 'accel': 0.15, 'steer': 2.5},
            {'name': 'Taxi', 'image': 'Topdown_vehicle_sprites_pack/taxi.png', 'speed': 4.5, 'accel': 0.18, 'steer': 2.8},
            {'name': 'Mini Van', 'image': 'Topdown_vehicle_sprites_pack/Mini_van.png', 'speed': 3.5, 'accel': 0.1, 'steer': 2},
            {'name': 'Mini Truck', 'image': 'Topdown_vehicle_sprites_pack/Mini_truck.png', 'speed': 3, 'accel': 0.08, 'steer': 1.8},
            {'name': 'Truck', 'image': 'Topdown_vehicle_sprites_pack/truck.png', 'speed': 2.5, 'accel': 0.05, 'steer': 1.5},
        ]

        self.car_images = [pygame.image.load(car['image']).convert_alpha() for car in self.cars]
        self.selected_index = 0

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
                if event.key == pygame.K_RIGHT:
                    self.selected_index = (self.selected_index + 1) % len(self.cars)
                if event.key == pygame.K_LEFT:
                    self.selected_index = (self.selected_index - 1) % len(self.cars)
                if event.key == pygame.K_RETURN:
                    self.running = False
                    selected_car_data = self.cars[self.selected_index]
                    self.game.state_stack.append(GamePlay(self.game, selected_car_data))

    def draw(self):
        self.screen.fill((30, 30, 30))

        # Title
        title = self.font.render("Select Your Car", True, (255, 255, 255))
        self.screen.blit(title, (self.game.screen_width/2 - title.get_width()/2, 50))

        # Display cars
        x_start = 100
        y_pos = self.game.screen_height / 2 - 50
        spacing = 100

        for i, img in enumerate(self.car_images):
            x = x_start + i * spacing
            if i == self.selected_index:
                # Highlight selected car
                pygame.draw.rect(self.screen, (255, 255, 0), (x - 5, y_pos - 5, img.get_width() + 10, img.get_height() + 10), 2)
            self.screen.blit(img, (x, y_pos))

        # Car Name and Stats
        selected_car = self.cars[self.selected_index]
        name_text = self.font.render(selected_car['name'], True, (255, 255, 255))
        self.screen.blit(name_text, (self.game.screen_width/2 - name_text.get_width()/2, y_pos + 150))

        stats_text = f"Speed: {selected_car['speed']} | Acceleration: {selected_car['accel']} | Steering: {selected_car['steer']}"
        stats_surf = self.small_font.render(stats_text, True, (255, 255, 255))
        self.screen.blit(stats_surf, (self.game.screen_width/2 - stats_surf.get_width()/2, y_pos + 200))

        pygame.display.flip()
