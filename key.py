import pygame


class Key:
    def __init__(self, position):
        self.image = pygame.image.load('Level/goldenkey.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize key image
        self.rect = self.image.get_rect(topleft=position)
        self.collected = False
        self.collect_sound = pygame.mixer.Sound('Sound Effect/key2 pickup.wav')
        self.collect_sound.set_volume(1)


    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect.topleft)

    def collect(self, player_rect):
        if self.rect.colliderect(player_rect) and not self.collected:
            self.collect_sound.play()
            self.collected = True