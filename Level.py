import pygame
from key import *

class Level1:
    def __init__(self, game, player):
        self.image = 'Level/lv1.png'
        self.game = game
        self.player = player
        self.bottom = 732
        self.finished = False
        self.has_key = False
        self.key = Key((250, 550))

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 787:
            self.player.rect.right = 787
        if self.player.rect.left <= 200:
            self.player.rect.left = 0
            self.finished = True

        # Batasan Dataran Tinggi dan Rendah
        if self.player.rect.left >= 200 and self.player.rect.left <= 350:
            self.bottom = 595
        if self.player.rect.left >= 468 and self.player.rect.right <= 780:
            self.bottom = 732

        # Batasan Bidang Miring
        if self.player.rect.left >= 346 and self.player.rect.left < 362:
            self.bottom = 597
        if self.player.rect.left >= 362 and self.player.rect.left < 378:
            self.bottom = 611
        if self.player.rect.left >= 378 and self.player.rect.left < 395:
            self.bottom = 634
        if self.player.rect.left >= 395 and self.player.rect.left < 410:
            self.bottom = 649
        if self.player.rect.left >= 410 and self.player.rect.left < 431:
            self.bottom = 665
        if self.player.rect.left >= 431 and self.player.rect.left < 443:
            self.bottom = 688
        if self.player.rect.left >= 443 and self.player.rect.left < 460:
            self.bottom = 703
        if self.player.rect.left >= 460 and self.player.rect.left < 468:
            self.bottom = 717
            
    def draw_key(self):
        self.key.draw(self.game.screen)
        self.key.collect(self.player.rect)
        if self.key.collected and not self.has_key:
            self.has_key = True
            self.game.notification_start_time = pygame.time.get_ticks()
            self.game.notification_message = "Kunci telah didapatkan!"

class Level1_1:
    def __init__(self, game, player):
        self.image = 'Level/lv1-1.png'
        self.game = game
        self.player = player
        self.bottom = 665
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.finished = True
            self.player.rect.left = 0
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

class Level1_1_1:
    def __init__(self, game, player):
        self.image = 'Level/lv1-1-1.png'
        self.game = game
        self.player = player
        self.bottom = 665
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

class Level2:
    def __init__(self, game, player):
        self.image = 'Level/lv2.png'
        self.game = game
        self.player = player
        self.bottom = 665
        self.finished = False
        self.has_key = False
        self.solved = False
        self.key = Key((764, 615))
        self.show_puzzle = False
        self.question = "K = 5   YGZA JOZGSHGN YGZA?"
        self.options = ["1. JAGX", "2. ZOMG", "3. KTGS"]
        self.puzzle_bg_image = pygame.image.load('Level/brown_age_by_darkwood67.jpg').convert()

    def puzzle(self):
        if 484 <= self.player.rect.right < 764:
            self.show_puzzle = True
            
    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
            
    def draw_puzzle(self):
        puzzle_width = 400
        puzzle_height = 300
        puzzle_surface = pygame.Surface((puzzle_width, puzzle_height))
        bg_image_resized = pygame.transform.scale(self.puzzle_bg_image, (puzzle_width, puzzle_height))
        puzzle_surface.blit(bg_image_resized, (0, 0))
        question_text = self.game.quiz_font.render(self.question, True, (255, 255, 255))
        puzzle_surface.blit(question_text, (puzzle_width // 2 - question_text.get_width() // 2, 50))

        for i, option in enumerate(self.options):
            option_text = self.game.quiz_font.render(option, True, (255, 255, 255))
            puzzle_surface.blit(option_text, (puzzle_width // 2 - option_text.get_width() // 2, 150 + i * 50))

        # Posisi di tengah layar
        screen_width, screen_height = self.game.screen.get_size()
        pos_x = (screen_width - puzzle_width) // 2
        pos_y = (screen_height - puzzle_height) // 2
        self.game.screen.blit(puzzle_surface, (pos_x, pos_y))

    def draw_key(self):
        self.key.draw(self.game.screen)
        self.key.collect(self.player.rect)
        if self.key.collected and not self.has_key:
            self.has_key = True
            self.game.notification_start_time = pygame.time.get_ticks()
            self.game.notification_message = "Kunci telah didapatkan!"

class Level3:
    def __init__(self, game, player):
        self.image = 'Level/lv3.png'
        self.game = game
        self.player = player
        self.bottom = 405
        self.finished = False
        self.has_key = False
        self.key = Key((300, 400))

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
        # Left Side
        if self.player.rect.left < 272:
            self.bottom = 405
        elif self.player.rect.left >= 272 and self.player.rect.left < 356:
            self.bottom = 445
        elif self.player.rect.left >= 356 and self.player.rect.right < 458:
            self.bottom = 483
        elif self.player.rect.left >= 445 and self.player.rect.right <= 801 and self.player.rect.bottom <= 344:
            self.bottom = 344
        if self.player.rect.right >= 460 and self.player.rect.left < 700 and self.player.rect.top >= 375 and self.player.rect.bottom <= 483:
            self.player.rect.right = 460
        if self.player.rect.right >= 448 and self.player.rect.left < 800 and self.player.rect.bottom >= 345 and self.player.rect.top <= 373:
            self.player.rect.right = 448
        if self.player.rect.top <= 375 and self.player.rect.right >= 373 and self.player.rect.right <= 375:
            self.player.rect.top = 375

        # right side
        if self.player.rect.right > 976:
            self.bottom = 405
        elif self.player.rect.right > 894 and self.player.rect.right <= 976:
            self.bottom = 445
        elif self.player.rect.left > 791 and self.player.rect.right <= 894:
            self.bottom = 483
        if self.player.rect.left <= 791 and self.player.rect.right > 500 and self.player.rect.top >= 375 and self.player.rect.bottom <= 483:
            self.player.rect.left = 791
        if self.player.rect.left <= 802 and self.player.rect.right > 500 and self.player.rect.bottom >= 345 and self.player.rect.top <= 373:
            self.player.rect.left = 802
        if self.player.rect.top <= 375 and self.player.rect.left >= 791 and self.player.rect.left <= 802:
            self.player.rect.top = 375
            
    def draw_key(self):
        self.key.draw(self.game.screen)
        self.key.collect(self.player.rect)
        if self.key.collected and not self.has_key:
            self.has_key = True
            self.game.notification_start_time = pygame.time.get_ticks()
            self.game.notification_message = "Kunci telah didapatkan!"

class Level4:
    def __init__(self, game, player):
        self.image = 'Level/lv4.png'
        self.game = game
        self.player = player
        self.bottom = 256
        self.finished = False
        self.has_key = False
        self.key = Key((550, 650))

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

        if self.player.rect.bottom >= 665:
            self.bottom = 256
            self.player.rect.bottom = 256
            self.player.rect.x = 651

        if 528 <= self.player.rect.right <= 778 and self.player.rect.bottom <= 258:
            self.bottom = 258
        elif 477 <= self.player.rect.left <= 669 and self.player.rect.bottom >= 270:
            self.bottom = 708
        elif 219 <= self.player.rect.left <= 477:
            self.bottom = 592
        elif 0 < self.player.rect.left < 118:
            self.bottom = 480
        elif 668 <= self.player.rect.right < 749:
            self.bottom = 592
        elif self.player.rect.right >= 749 and self.player.rect.bottom > 543:
            self.player.rect.right = 749
        elif 749 < self.player.rect.right < 821:
            self.bottom = 543
        elif self.player.rect.right >= 821 and self.player.rect.bottom > 483:
            self.player.rect.right = 821
        elif 821 < self.player.rect.right < 893:
            self.bottom = 483
        elif self.player.rect.right >= 893 and self.player.rect.bottom > 442:
            self.player.rect.right = 893
        elif 893 < self.player.rect.right < 977:
            self.bottom = 442
        elif self.player.rect.right >= 977 and self.player.rect.bottom > 406:
            self.player.rect.right = 977
        elif 977 < self.player.rect.right <= 1250:
            self.bottom = 406    

        if self.player.rect.left >= 119 and self.player.rect.left < 126:
            self.bottom = 480
        if self.player.rect.left >= 126 and self.player.rect.left < 134:
            self.bottom = 488
        if self.player.rect.left >= 134 and self.player.rect.left < 145:
            self.bottom = 496
        if self.player.rect.left >= 145 and self.player.rect.left < 150:
            self.bottom = 509
        if self.player.rect.left >= 150 and self.player.rect.left < 156:
            self.bottom = 514
        if self.player.rect.left >= 156 and self.player.rect.left < 163:
            self.bottom = 521
        if self.player.rect.left >= 163 and self.player.rect.left < 170:
            self.bottom = 527
        if self.player.rect.left >= 170 and self.player.rect.left < 178:
            self.bottom = 536
        if self.player.rect.left >= 178 and self.player.rect.left < 188:
            self.bottom = 544
        if self.player.rect.left >= 188 and self.player.rect.left < 200:
            self.bottom = 554
        if self.player.rect.left >= 200 and self.player.rect.left < 207:
            self.bottom = 566
        if self.player.rect.left >= 207 and self.player.rect.left < 213:
            self.bottom = 573
        if self.player.rect.left >= 213 and self.player.rect.left < 215:
            self.bottom = 579
        if self.player.rect.left >= 215 and self.player.rect.left < 219:
            self.bottom = 581
            
    def draw_key(self):
        self.key.draw(self.game.screen)
        self.key.collect(self.player.rect)
        if self.key.collected and not self.has_key:
            self.has_key = True
            self.game.notification_start_time = pygame.time.get_ticks()
            self.game.notification_message = "Kunci telah didapatkan!"

class Level5:
    def __init__(self, game, player):
        self.image = 'Level/lv5.png'
        self.game = game
        self.player = player
        self.bottom = 587
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 15:
            self.player.rect.left = 15

        if self.player.rect.bottom >= 649:
            self.bottom = 588
            self.player.rect.bottom = 587
            self.player.rect.x = 32

        # platform 2
        elif self.player.rect.right >= 482 and self.player.rect.left <= 727 and self.player.rect.bottom <= 147:
            self.bottom = 147

        # Platform 1
        elif self.player.rect.right >= 348 and self.player.rect.left <= 577 and self.player.rect.bottom <= 399:
            self.bottom = 399
        
        # Land
        elif 0 > self.player.rect.left <= 271:
            self.bottom = 588
        elif self.player.rect.left > 271 and self.player.rect.right < 462:
            self.bottom = 688
        elif self.player.rect.right >= 462 and self.player.rect.right < 570:
            self.bottom = 594
        elif self.player.rect.right >= 570 and self.player.rect.bottom > 543:
            self.player.rect.right = 570
        elif self.player.rect.right > 570 and self.player.rect.right < 665:
            self.bottom = 543
        elif self.player.rect.right >= 665 and self.player.rect.bottom > 480:
            self.player.rect.right = 665
        elif self.player.rect.right > 665 and self.player.rect.right < 764:
            self.bottom = 480
        elif self.player.rect.right >= 764 and self.player.rect.bottom > 444:
            self.player.rect.right = 764
        elif self.player.rect.right > 764 and self.player.rect.right < 875:
            self.bottom = 442
        elif self.player.rect.right >= 875 and self.player.rect.bottom > 409:
            self.player.rect.right = 875
        elif self.player.rect.right > 875 and self.player.rect.right < 1250:
            self.bottom = 409

class Level5_5:
    def __init__(self, game, player):
        self.image = 'Level/lv5-5.png'
        self.game = game
        self.player = player
        self.bottom = 670
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

        
class LevelEnd:
    def __init__(self, game, player):
        self.image = 'Level/end.jpg'
        self.game = game
        self.player = player
        self.bottom = 670
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
