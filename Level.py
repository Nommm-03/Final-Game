import pygame

class Level1:
    def __init__(self, game, player):
        self.image = 'Level/lv1.png'
        self.game = game
        self.player = player
        self.bottom = 732
        self.finished = False

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

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

class Level3:
    def __init__(self, game, player):
        self.image = 'Level/lv3.png'
        self.game = game
        self.player = player
        self.bottom = 405
        self.finished = False

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


class Level4:
    def __init__(self, game, player):
        self.image = 'Level/lv4.png'
        self.game = game
        self.player = player
        self.bottom = 256
        self.finished = False

    def restrict(self):
        # Batasan Tepi
        if self.player.rect.bottom >= self.bottom:
            self.player.rect.bottom = self.bottom
        if self.player.rect.right >= 1250:
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

        if 528 <= self.player.rect.right <= 778 and self.player.rect.bottom <= 258:
            self.bottom = 258
        elif 477 <= self.player.rect.left <= 669 and self.player.rect.bottom >= 270:
            self.bottom = 708
        elif 463 <= self.player.rect.x <= 681 and self.player.rect.bottom >= 700:
            self.bottom = 256
            self.player.rect.x = 651
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
        if self.player.rect.left <= 0:
            self.player.rect.left = 0

        if self.player.rect.right >= 529 and self.player.rect.left <= 778 and self.player.rect.bottom <= 258:
            self.bottom = 258
        
class LevelEnd:
    def __init__(self, game, player):
        self.image = 'Level/end.png'
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
