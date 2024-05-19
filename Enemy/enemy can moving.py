import pygame

# Window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF

DARK_BLUE = (3, 5, 54)

class Enemy:
    def __init__(self, x, y, pace, bitmap, turn_after=100, speed=1, size=None):
        """Create a new Enemy at (x,y) position with given bitmap.
        It moves pace pixels left and right."""
        self.image = pygame.image.load(bitmap).convert_alpha()
        
        # Resize the image if size is provided
        if size:
            self.image = pygame.transform.scale(self.image, size)
        
        self.rect = self.image.get_rect(center=(x, y))
        self.pace_size = pace
        self.pace_count = 0
        self.direction = -1
        self.turn_after = turn_after
        self.speed = speed
        self.pace_time = 0

    def update(self):
        """Implement the movement algorithm."""
        time_now = pygame.time.get_ticks()
        if time_now > self.pace_time + self.speed:
            self.pace_time = time_now

            # Move in the current direction
            self.pace_count += 1
            self.rect.x += self.direction * self.pace_size

            # Change direction if walked enough paces or hit screen edge
            if self.pace_count >= self.turn_after or \
                    self.rect.x <= 0 or \
                    self.rect.x >= WINDOW_WIDTH - self.rect.width:
                self.direction *= -1
                self.pace_count = 0

    def draw(self, surface):
        """Draw the enemy on the given surface."""
        surface.blit(self.image, self.rect.topleft)

### Initialization
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("Movement Algorithm Example")

### Enemy Instance
pos_x = WINDOW_WIDTH // 2
pos_y = WINDOW_HEIGHT // 2
pace_size = 7
enemy = Enemy(pos_x, pos_y, pace_size, "ENEMY/Monster1.png", size=(100, 100))

### Main Loop
clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the window
    enemy.update()
    window.fill(DARK_BLUE)
    enemy.draw(window)
    pygame.display.flip()

    # Clamp FPS
    clock.tick_busy_loop(100)

pygame.quit()
