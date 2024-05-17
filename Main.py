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
        self.level = '1'
        self.player = Player(self, 1, 19)
        self.bottom = 0
        
        self.level1 = Level1(self, self.player)
        self.level1_1 = Level1_1(self, self.player)
        self.level1_1_1 = Level1_1_1(self, self.player)
        self.level2 = Level2(self, self.player)
        self.level3 = Level3(self, self.player)
        self.level4 = Level4(self, self.player)
        self.level5 = Level5(self, self.player)
        self.end = LevelEnd(self, self.player)
        self.running = True

        # self.open_sound = pygame.mixer.Sound('Sound Effect/qubodup-DoorOpen01.flac')

    def new(self):
        # a new game starts
        self.playing = True

    def main(self):
        # game loop 
        while self.playing:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(mouse_pos)
                if event.type == pygame.KEYDOWN:
                    if self.level == '1-1-1':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 782 and self.player.rect.left <= 1103):
                            self.level1_1_1.finished = True
                            self.player.rect.x = 200
                    elif self.level == '2':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 877 and self.player.rect.left <= 1143):
                            self.level2.finished = True
                            self.player.rect.left = 0
                    elif self.level == '3':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 537 and self.player.rect.left <= 709 and self.player.rect.bottom <= 344):
                            self.level3.finished = True
                            self.player.rect.x = 651
                            self.player.rect.bottom = 250
                    elif self.level == '4':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 239 and self.player.rect.left <= 571 and self.player.rect.bottom <= 600):
                            self.level4.finished = True

            self.screen.blit(self.background, (0, 0))

            if self.level == '1' and not self.level1.finished:
                self.bottom = self.level1.bottom
                game_background = pygame.image.load(self.level1.image).convert_alpha()
                self.screen.blit(game_background, (200, 0))
                self.level1.restrict()

            if self.level == '1-1' and not self.level1_1.finished:
                self.bottom = self.level1_1.bottom
                game_background = pygame.image.load(self.level1_1.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level1_1.restrict()

            if self.level == '1-1-1' and not self.level1_1_1.finished:
                self.bottom = self.level1_1_1.bottom
                game_background = pygame.image.load(self.level1_1_1.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level1_1_1.restrict()

            if self.level == '2' and not self.level2.finished:
                self.bottom = self.level2.bottom
                game_background = pygame.image.load(self.level2.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level2.restrict()

            if self.level == '3' and not self.level3.finished:
                self.bottom = self.level3.bottom
                game_background = pygame.image.load(self.level3.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level3.restrict()

            if self.level == '4' and not self.level4.finished:
                self.bottom = self.level4.bottom
                game_background = pygame.image.load(self.level4.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level4.restrict()
            
            if self.level == '5' and not self.level5.finished:
                self.bottom = self.level5.bottom
                game_background = pygame.image.load(self.level5.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level5.restrict()

            if self.level1.finished:
                self.level = '1-1'
            if self.level1_1.finished:
                self.level = '1-1-1'
            if self.level1_1_1.finished:
                self.level = '2'
            if self.level2.finished:
                self.level = '3'
            if self.level3.finished:
                self.level = '4'
            if self.level4.finished:
                self.level = '5'

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
        self.bottom = 665
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

