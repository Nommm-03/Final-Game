import pygame
from config import *

class Player():
    def _init_(self, game, x, y):

        self.game = game

        self.x = (WIN_WIDTH/2)
        self.y = 680
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.gravity = 0

        self.images = {
            'idle': pygame.image.load('chara1.png'),
            'walk': [
                pygame.image.load('chara2.png'),
                pygame.image.load('chara3.png')
            ]
        }
        self.image = self.images['idle']
        self.image_index = 0
        self.animation_time = 200
        self.last_update = pygame.time.get_ticks()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.jump_sound = pygame.mixer.Sound ('Sound Effect/SFX_Jump_01.wav')
        self.jump_sound.set_volume(0.2)

    def update(self, bottom):
        self.movement(bottom)

        self.rect.x += self.x_change

        self.gravity += 1
        self.rect.y += self.gravity

        self.x_change = 0

    def movement(self, bottom):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.animate('walk', current_time)
        elif keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.animate('walk', current_time)
        else:
            self.image = self.images['idle']

        if keys[pygame.K_SPACE] and self.rect.bottom >= bottom:
            self.jump_sound.play()
            self.gravity -= 15

    def animate(self, animation_type, current_time):
        if current_time - self.last_update > self.animation_time:
            self.image_index = (self.image_index + 1) % len(self.images[animation_type])
            self.image = self.images[animation_type][self.image_index]
            self.last_update = current_time
