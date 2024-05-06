import pygame
from sprites import *
from config import *
import sys
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.caption = pygame.display.set_caption('Enigma Escape')
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        bg_music_path = os.path.join(os.path.dirname(__file__), 'class room', 'Factory.ogg')
        pygame.mixer.music.load(bg_music_path)
        pygame.mixer.music.play(-1)

        self.player = Player(self, 1, 6)

    def events(self):  
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
         # Load background image
        bg_path = os.path.join(os.path.dirname(__file__), 'class room', 'start.png')
        background_image = pygame.image.load(bg_path).convert()
        self.screen.blit(background_image, (0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

game = Game()
game.intro_screen()
game.new()
while game.running:
    game.main()
    game.game_over()

pygame.quit()
sys.exit()

