import pygame
from config import *
import math
import random

class Player():
    def __init__(self, game, x, y):

        self.game = game

        self.x = (WIN_WIDTH/2)
        self.y = 680
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.gravity = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.jump_sound = pygame.mixer.Sound('Sound Effect/SFX_Jump_01.wav')
    
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 664:
            self.rect.bottom = 664

        self.x_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_SPACE] and self.rect.bottom >= 664:
            self.jump_sound.play()
            self.gravity -= 15
