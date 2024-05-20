import pygame
from Player import *
from Level import *
from npc import *
from config import *
from Enemy_Moving import *
from Enemy_Follow import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.caption = pygame.display.set_caption('Enigma Escape')
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font('Font/joystix monospace.otf', 40)
        self.quiz_font = pygame.font.Font('Font/joystix monospace.otf', 15)
        self.background = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
        self.background.fill(BLACK)
        self.level = '1'

        self.player = Player(self, 1, 19)
        self.bottom = 0
        
        # Monster Level 1
        self.enemy_moving1 = Enemy(self, 7, 1, 60, -1, 'Enemy/Monster1.png',size=(100, 100))
        self.enemy_moving2 = Enemy(self, 7, 1, 60, -1, 'Enemy/Monster1.png', size=(100, 100))

        # Monster Level 2
        self.enemy_moving3 = Enemy(self, 18, 1, 15, -1, 'Enemy/Monster2.png', size=(100, 100))

        # Monster Level 3
        self.enemy_moving4 = Enemy(self, 14, 1, 8, 1, 'Enemy/Monster2.png', size=(100, 100))
        self.enemy_moving5 = Enemy(self, 14, 1, 10, -1, 'Enemy/Monster2.png', size=(100, 100))

        # Monster Level 4
        self.enemy_moving6 = Enemy(self, 14, 1, 13, -1, 'Enemy/Monster2.png', size=(100, 100))
        self.enemy_follow1 = Ghost(self, 100, 100, self.player, 4, 'Enemy/Ghost1.png')
        self.enemy_follow2 = Ghost(self, 589, 519, self.player, 3, 'Enemy/Ghost2.png')

        # Monster Level 5
        self.enemy_moving7 = Enemy(self, 6, 1, 25, 1, 'Enemy/Monster1.png', size=(100, 100))
        self.enemy_moving8 = Enemy(self, 14, 1, 13, 1, 'Enemy/Monster2.png', size=(100, 100))
        self.enemy_follow3 = Ghost(self, 63, 68, self.player, 2, 'Enemy/Ghost1.png')
        self.enemy_follow4 = Ghost(self, 1126, 77, self.player, 3, 'Enemy/Ghost1.png')
        self.enemy_follow5 = Ghost(self, 1058, 624, self.player, 4, 'Enemy/Ghost2.png')

        self.level1 = Level1(self, self.player)
        self.level1_1 = Level1_1(self, self.player)
        self.level1_1_1 = Level1_1_1(self, self.player)
        self.level2 = Level2(self, self.player)
        self.level3 = Level3(self, self.player)
        self.level4 = Level4(self, self.player)
        self.level5 = Level5(self, self.player)
        self.level5_5 = Level5_5(self, self.player)
        self.end = LevelEnd(self, self.player)
        self.running = True

        self.bg_music = pygame.mixer.music.load('Level/Factory.ogg')
        pygame.mixer.music.play(-1)

        self.opening_quiz_sound = pygame.mixer.Sound('Sound Effect/Page Turning Sfx.wav')
        self.wrong_sound = pygame.mixer.Sound('Sound Effect/wrong_sound_effect.mp3')
        self.correct_sound = pygame.mixer.Sound('Sound Effect/correct_sound_effect.mp3')
        self.open_sound = pygame.mixer.Sound('Sound Effect/qubodup-DoorOpen01.flac')
        self.notification_sound = pygame.mixer.Sound('Sound Effect/Tolling Bell-Bright.mp3')
        self.notification_start_time = None
        self.notification_message = ""
        self.has_notified = False
        self.sound_played = False

        self.npc1 = NPC((680, 530), "Selamat datang di Enigmatic Journey, Tujuan utamamu disini adalah untuk menemukan kunci di setiap levelnya. untuk level pertama, kamu akan diberi petunjuk-petunjuk yang akan kamu butuhkan untuk keluar dari mansion ini.")
        self.npc2 = NPC((236, 470), "Di dalam mansion ini, kamu akan menemui banyak rintangan seperti puzzle, kuis, dan monster. Lewati semua rintangan itu untuk lanjut ke ruangan selanjutnya!")
        self.npc3 = NPC((603,470), "Jika kamu sudah memiliki kunci emas, kamu bisa memasuki pintu untuk menuju ruangan selanjutnya.")
        self.npc4 = NPC((120,215), "")
        self.npc5 = NPC((1108, 212), "Terkadang kamu harus berani mati untuk mencapai tujuanmu.")

    def show_notification(self, message, duration=2000):
        if self.notification_start_time is None:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.notification_start_time < duration:
            font = pygame.font.Font('Font/joystix monospace.otf', 40)
            text_surface = font.render(message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIN_WIDTH // 2, 100))  # Posisikan di tengah, dengan y=100
            self.screen.blit(text_surface, text_rect.topleft)

        else:
            self.notification_start_time = None
            self.notification_message = ""

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
                    if self.level == '1' and event.key == pygame.K_RETURN and 742 <= self.player.rect.right and self.player.rect.left <= 791:
                        self.opening_quiz_sound.play()
                        self.npc1.toggle_dialog()
                    if self.level == '1-1' and event.key == pygame.K_RETURN and 293 <= self.player.rect.right and self.player.rect.left <= 358:
                        self.opening_quiz_sound.play()
                        self.npc2.toggle_dialog()
                    if self.level == '1-1-1':
                        if event.key == pygame.K_RETURN and 669 <= self.player.rect.right and self.player.rect.left <= 715:
                            self.npc3.toggle_dialog()
                            self.opening_quiz_sound.play()
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 782 and self.player.rect.left <= 1103) and self.level1.has_key:
                            self.open_sound.play()
                            self.has_notified = False
                            self.level1_1_1.finished = True
                            self.player.rect.x = 200
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 782 and self.player.rect.left <= 1103) and not self.level1.has_key:
                            self.notification_start_time = pygame.time.get_ticks()
                            self.notification_message = "Butuh Kunci!"
                            self.notification_sound.play()
                    elif self.level == '2':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 877 and self.player.rect.left <= 1143) and self.level2.has_key:
                            self.open_sound.play()
                            self.has_notified = False
                            self.level2.finished = True
                            self.player.rect.left = 0
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 877 and self.player.rect.left <= 1143) and not self.level2.has_key:
                            self.notification_start_time = pygame.time.get_ticks()
                            self.notification_message = "Butuh Kunci!"
                            self.notification_sound.play()
                        if event.key == pygame.K_RETURN and (484 <= self.player.rect.right < 764):
                            self.level2.puzzle()
                        if self.level2.show_puzzle:
                            if not self.sound_played:
                                self.opening_quiz_sound.play()
                                self.sound_played = True
                            if event.key == pygame.K_ESCAPE:
                                self.opening_quiz_sound.play()
                                self.level2.show_puzzle = False
                                self.sound_played = False
                            elif event.key == pygame.K_1:
                                self.opening_quiz_sound.play()
                                self.correct_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Benar! Kunci telah didrop."
                                self.level2.solved = True
                                self.level2.show_puzzle = False
                            elif event.key == pygame.K_2:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                            elif event.key == pygame.K_3:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                    elif self.level == '3':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 537 and self.player.rect.left <= 709 and self.player.rect.bottom <= 500) and self.level3.has_key:
                            self.open_sound.play()
                            self.has_notified = False
                            self.level3.finished = True
                            self.player.rect.x = 651
                            self.player.rect.bottom = 250
                        elif event.key == pygame.K_RETURN and (self.player.rect.right >= 537 and self.player.rect.left <= 709 and self.player.rect.bottom <= 500) and not self.level3.has_key:
                            self.notification_start_time = pygame.time.get_ticks()
                            self.notification_message = "Butuh Kunci!"
                            self.notification_sound.play()
                        if event.key == pygame.K_RETURN and (175 <= self.player.rect.right < 297):
                            self.level3.puzzle()
                        if self.level3.show_puzzle:
                            if not self.sound_played:
                                self.opening_quiz_sound.play()
                                self.sound_played = True
                            if event.key == pygame.K_ESCAPE:
                                self.opening_quiz_sound.play()
                                self.level3.show_puzzle = False
                                self.sound_played = False
                            elif event.key == pygame.K_1:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                            elif event.key == pygame.K_2:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                            elif event.key == pygame.K_3:
                                self.opening_quiz_sound.play()
                                self.correct_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Benar! Kunci telah didrop."
                                self.level3.solved = True
                                self.level3.show_puzzle = False
                                self.sound_played = False
                    elif self.level == '4':
                        if event.key == pygame.K_RETURN and self.player.rect.right >= 1162:
                            self.npc5.toggle_dialog()
                            self.opening_quiz_sound.play()
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 239 and self.player.rect.left <= 425) and self.level4.has_key:
                            self.has_notified = False
                            self.open_sound.play()
                            self.level4.finished = True
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 239 and self.player.rect.left <= 425)and not self.level4.has_key:
                            self.notification_start_time = pygame.time.get_ticks()
                            self.notification_message = "Butuh Kunci!"
                            self.notification_sound.play()
                    elif self.level == '5':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 1013 and self.player.rect.left <= 1168 and self.player.rect.bottom >= 405) and self.level5.has_key:
                            self.level5.finished = True
                            self.open_sound.play()
                            self.has_notified = False
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 1013 and self.player.rect.left <= 1168 and self.player.rect.bottom >= 405) and not self.level5.has_key:
                            self.notification_start_time = pygame.time.get_ticks()
                            self.notification_message = "Butuh Kunci!"
                            self.notification_sound.play()
                        if event.key == pygame.K_RETURN and ((394 <= self.player.rect.right < 530 and self.player.rect.bottom >= 380) or (540 <= self.player.rect.right < 668 and self.player.rect.bottom >= 135)):
                            self.level5.puzzle()
                        if self.level5.show_puzzle_1:
                            if not self.sound_played:
                                self.opening_quiz_sound.play()
                                self.sound_played = True
                            if event.key == pygame.K_ESCAPE:
                                self.opening_quiz_sound.play()
                                self.level5.show_puzzle_1 = False
                                self.sound_played = False
                            elif event.key == pygame.K_1:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                            elif event.key == pygame.K_2:
                                self.opening_quiz_sound.play()
                                self.correct_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Benar! Kunci telah didrop."
                                self.level5.quiz1_solved = True
                                self.level5.show_puzzle_1 = False
                                self.sound_played = False
                            elif event.key == pygame.K_3:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                        if self.level5.show_puzzle_2 and self.level5.has_silver_key:
                            if not self.sound_played:
                                self.opening_quiz_sound.play()
                                self.sound_played = True
                            if event.key == pygame.K_ESCAPE:
                                self.opening_quiz_sound.play()
                                self.level5.show_puzzle_2 = False
                                self.sound_played = False
                            elif event.key == pygame.K_1:
                                self.opening_quiz_sound.play()
                                self.correct_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Benar! Kunci telah didrop."
                                self.level5.quiz2_solved = True
                                self.level5.show_puzzle_2 = False
                            elif event.key == pygame.K_2:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                            elif event.key == pygame.K_3:
                                self.wrong_sound.play()
                                self.notification_start_time = pygame.time.get_ticks()
                                self.notification_message = "Jawaban Salah!"
                    elif self.level == '5-5':
                        if event.key == pygame.K_RETURN and (self.player.rect.right >= 152 and self.player.rect.left <= 473 and self.player.rect.bottom <= 675):
                            self.level5_5.finished = True
                            self.player.rect.x = 622

            self.screen.blit(self.background, (0, 0))

            if self.level == '1' and not self.level1.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 1"
                    self.has_notified = True
                self.bottom = self.level1.bottom
                game_background = pygame.image.load(self.level1.image).convert_alpha()
                self.screen.blit(game_background, (200, 0))
                self.level1.restrict()
                self.level1.draw_key()
                self.npc1.draw(self.screen)

            if self.level == '1-1' and not self.level1_1.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 1.1"
                    self.has_notified = True
                self.bottom = self.level1_1.bottom
                game_background = pygame.image.load(self.level1_1.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.enemy_moving1.rect.bottom = 665
                self.enemy_moving2.rect.bottom = 665
                self.enemy_moving1.update()
                self.enemy_moving1.draw(self.screen)
                self.enemy_moving2.update()
                self.enemy_moving2.draw(self.screen)
                self.level1_1.restrict()
                self.level1_1.collision(self.enemy_moving1)
                self.level1_1.collision(self.enemy_moving2)
                self.npc2.draw(self.screen)

            if self.level == '1-1-1' and not self.level1_1_1.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 1.1.1"
                    self.has_notified = True
                self.bottom = self.level1_1_1.bottom
                game_background = pygame.image.load(self.level1_1_1.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level1_1_1.restrict()
                self.npc3.draw(self.screen)

            if self.level == '2' and not self.level2.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 2"
                    self.level2.key.collected = False
                    self.has_notified = True
                self.bottom = self.level2.bottom
                game_background = pygame.image.load(self.level2.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.enemy_moving3.rect.bottom = 665
                self.enemy_moving3.update()
                self.enemy_moving3.draw(self.screen)
                self.level2.collision(self.enemy_moving3)
                self.level2.restrict()
                if self.level2.show_puzzle and not self.level2.solved:
                    self.level2.draw_puzzle()
                if self.level2.solved:
                    self.level2.draw_key()

            if self.level == '3' and not self.level3.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 3"
                    self.has_notified = True
                self.bottom = self.level3.bottom
                game_background = pygame.image.load(self.level3.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.enemy_moving4.rect.bottom = 343
                self.enemy_moving4.update()
                self.enemy_moving4.draw(self.screen)
                self.enemy_moving5.rect.bottom = 343
                self.enemy_moving5.update()
                self.enemy_moving5.draw(self.screen)
                self.level3.collision(self.enemy_moving4)
                self.level3.collision(self.enemy_moving5)
                self.level3.restrict()
                self.npc4.draw(self.screen)
                if self.level3.show_puzzle and not self.level3.solved:
                    self.level3.draw_puzzle()
                if self.level3.solved:
                    self.level3.draw_key()

            if self.level == '4' and not self.level4.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 4"
                    self.has_notified = True
                self.bottom = self.level4.bottom
                game_background = pygame.image.load(self.level4.image).convert_alpha()
                self.level4.restrict()
                self.level4.draw_key()
                self.screen.blit(game_background, (0, 0))
                self.enemy_moving6.rect.bottom = 590
                self.enemy_moving6.update()
                self.enemy_moving6.draw(self.screen)
                self.enemy_follow1.update()
                self.enemy_follow1.draw(self.screen)
                self.enemy_follow2.update()
                self.enemy_follow2.draw(self.screen)
                self.level4.collision(self.enemy_moving6)
                self.level4.collision(self.enemy_follow1)
                self.level4.collision(self.enemy_follow2)
                self.npc5.draw(self.screen)

            if self.level == '5' and not self.level5.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 5"
                    self.has_notified = True
                self.bottom = self.level5.bottom
                game_background = pygame.image.load(self.level5.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level5.restrict()

                if not (self.level5.show_puzzle_1 or self.level5.show_puzzle_2):
                    self.enemy_moving7.rect.bottom = 405
                    self.enemy_moving7.update()
                    self.enemy_moving7.draw(self.screen)
                    self.enemy_moving8.rect.bottom = 405
                    self.enemy_moving8.update()
                    self.enemy_moving8.draw(self.screen)
                    self.enemy_follow3.update()
                    self.enemy_follow3.draw(self.screen)
                    self.enemy_follow4.update()
                    self.enemy_follow4.draw(self.screen)
                    self.enemy_follow5.update()
                    self.enemy_follow5.draw(self.screen)
                    self.level5.collision(self.enemy_moving7)
                    self.level5.collision(self.enemy_moving8)
                    self.level5.collision(self.enemy_follow3)
                    self.level5.collision(self.enemy_follow4)
                    self.level5.collision(self.enemy_follow5)
                
                if self.level5.show_puzzle_1 and not self.level5.quiz1_solved:
                    self.level5.draw_puzzle(self.level5.question_1, self.level5.options_1)
                if self.level5.show_puzzle_2 and not self.level5.quiz2_solved:
                    self.level5.draw_puzzle(self.level5.question_2, self.level5.options_2)
                if self.level5.quiz1_solved or self.level5.quiz2_solved:
                    self.level5.draw_key()
            
            if self.level == '5-5' and not self.level5_5.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "ROOM 5.5"
                    self.has_notified = True
                self.bottom = self.level5_5.bottom
                game_background = pygame.image.load(self.level5_5.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.level5_5.restrict()

            if self.level == 'End' and not self.end.finished:
                if not self.has_notified:
                    self.notification_start_time = pygame.time.get_ticks()
                    self.notification_message = "END"
                    self.has_notified = True
                self.bottom = self.end.bottom
                game_background = pygame.image.load(self.end.image).convert_alpha()
                self.screen.blit(game_background, (0, 0))
                self.end.restrict()

            if self.notification_start_time:
                self.show_notification(self.notification_message)

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
            if self.level5.finished:
                self.level = '5-5'
            if self.level5_5.finished:
                self.level = 'End'

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
        title1 = self.title_font.render('Enigmatic Escape', True, WHITE)
        title1_rect = title1.get_rect(x=420,y=60)
        title2 = self.title_font.render('Jaxon Journey', True, WHITE)
        title2_rect = title2.get_rect(x=415,y=115)
        intro_background = pygame.image.load('Level/start.png').convert_alpha()

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
                        self.open_sound.play()
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

