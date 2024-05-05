import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.jump_speed = -10 
        self.jump_height = 100 
        self.jump_count = 0 
        self.speed_x = 0
        self.speed_y = 0

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed_x = -PLAYER_SPEED
        elif keystate[pygame.K_d]:
            self.speed_x = PLAYER_SPEED
        else:
            self.speed_x = 0
        
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

        if keystate[pygame.K_SPACE] and self.jump_count < 2:  # Batasi jumlah lompatan
            self.jump()

        self.rect.x += self.x_change
        self.speed_y += PLAYER_GRAVITY
        self.rect.y += self.speed_y

        if self.rect.bottom > WIN_HEIGHT - 105:
            self.rect.bottom = WIN_HEIGHT - 105
            self.speed_y = 0
            self.jump_count = 0  # Setel ulang jumlah lompatan

        self.rect.x += self.speed_x
        
    def jump(self):
        if self.jump_count < 2:  # Batasi jumlah lompatan
            self.speed_y = self.jump_speed
            self.jump_count += 1
