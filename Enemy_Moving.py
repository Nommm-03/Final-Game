import pygame

class Enemy:
    def __init__(self, game, pace, speed, turn_after, direction, bitmap, size=None):
        self.image = pygame.image.load(bitmap).convert_alpha()
        
        # Resize the image if size is provided
        if size:
            self.image = pygame.transform.scale(self.image, size)
        
        self.rect = self.image.get_rect()
        self.pace_size = pace
        self.pace_count = 0
        self.direction = direction
        self.speed = speed
        self.turn_after = turn_after
        self.pace_time = 0
        self.game = game

    def update(self):
        """Implement the movement algorithm."""
        time_now = pygame.time.get_ticks()
        if time_now > self.pace_time + self.speed:
            self.pace_time = time_now

            # Move in the current direction
            self.rect.x += self.direction * self.pace_size

            # Change direction if walked enough paces or hit screen edge
            if self.pace_count >= self.turn_after:
                self.direction *= -1
                self.pace_count = 0
            
            self.pace_count += 1

    def draw(self, surface):
        """Draw the enemy on the given surface."""
        surface.blit(self.image, self.rect.topleft)
