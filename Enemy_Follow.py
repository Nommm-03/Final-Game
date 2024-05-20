import pygame
import math

pygame.init()

class Ghost:
    def __init__(self, game, x, y, player, speed, bitmap):
        super().__init__()
        # Load ghost image
        original_image = pygame.image.load(bitmap).convert_alpha()
        # Adjust the size of the image
        scaled_width = 100  # Adjust this value as needed for the desired width
        scaled_height = 100  # Adjust this value as needed for the desired height
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        self.speed = speed

    def update(self):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.center)