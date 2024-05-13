import pygame
from Player import *
from Level import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.caption = pygame.display.set_caption('Enigma Escape')
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font('Font/joystix monospace.otf', 40)
        self.background = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
        self.background.fill(BLACK)
        self.level = 1
        self.player = Player(self, 1, 19)
        self.bottom = 0
        
        self.level1 = Level1(self, self.player)
        self.level1_1 = Level1_1(self, self.player)
        self.running = True

        self.open_sound = pygame.mixer.Sound('Sound Effect/qubodup-DoorOpen01.flac')

    def new(self):
        # a new game starts
        self.playing = True

    def main(self):
        #game loop 

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(mouse_pos)
                
                mouse_pos = pygame.mouse.get_pos()
                
            self.screen.blit(self.background,(0,0))

            if self.level == 1 and not self.level1.finished:
                self.bottom = self.level1.bottom
                game_background = pygame.image.load(self.level1.image).convert_alpha()
                self.screen.blit(game_background,(200,0))
                self.level1.restrict()
            
            if self.level == 1.1 and not self.level1_1.finished:
                self.bottom = self.level1_1.bottom
                game_background = pygame.image.load(self.level1_1.image).convert_alpha()
                self.screen.blit(game_background,(0,0))
                self.level1_1.restrict()

            if self.level1.finished:
                self.level = 1.1

            self.screen.blit(self.player.image, self.player.rect)
            self.player.movement(self.bottom)
            self.player.update(self.bottom)
            self.clock.tick(FPS)
            pygame.display.update()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        self.intro = True
        self.bottom = 664
        title1 = self.title_font.render('Enigma Escape', True, WHITE)
        title1_rect = title1.get_rect(x=420,y=60)
        title2 = self.title_font.render('Jaxon Journey', True, WHITE)
        title2_rect = title2.get_rect(x=415,y=115)
        intro_background = pygame.image.load('start.png').convert_alpha()

        play_button = Button(830, 310, 100, 50, WHITE, BLACK, 'Play', 32)

        quit_button = Button(340, 310, 100, 50, WHITE, BLACK, 'Quit', 32)

        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: 
                    # QUIT BUTTON
                    if event.key == pygame.K_RETURN and (self.player.rect.x >= 249 and self.player.rect.x <= 523):  # Ketika tombol "Enter" ditekan
                        self.intro = False
                        self.running = False
                        pygame.quit()
                        sys.exit()

                    # START BUTTON
                    if event.key == pygame.K_RETURN and (self.player.rect.x >= 746 and self.player.rect.x <= 1011):  # Ketika tombol "Enter" ditekan
                        self.intro = False
                        self.player.rect.x = 607

            self.screen.blit(intro_background, (0,0))
            self.screen.blit(title1, title1_rect)
            self.screen.blit(title2, title2_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.screen.blit(self.player.image, self.player.rect)

            # Movement Player
            self.player.movement(self.bottom)
            self.player.update(self.bottom)
            if self.player.rect.right >= 1250:
                self.player.rect.right = 1250
            if self.player.rect.left <= 0:
                self.player.rect.left = 0
            if self.player.rect.bottom >= self.bottom:
                self.player.rect.bottom = self.bottom
                self.player.gravity = 0
                
            self.clock.tick(FPS)
            pygame.display.update()

class Button:
    def __init__ (self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('Font/joystix monospace.otf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

game = Game()
game.intro_screen()
game.new()
while game.running:
    game.main()
    game.game_over()

pygame.quit()
sys.exit()

