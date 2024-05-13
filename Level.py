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
        if self.player.rect.right >= 780:
            self.player.rect.right = 780
        if self.player.rect.left <= 200:
            self.player.rect.left = 200
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
            self.player.rect.right = 1250
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
