import pygame

# Inisialisasi Pygame
pygame.init()

# Mengatur jendela full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Memuat gambar
gambar = pygame.image.load("GAME/lv5.png")

# Mendapatkan ukuran gambar
gambar_width, gambar_height = gambar.get_size()

# Mendapatkan ukuran layar
screen_width, screen_height = screen.get_size()

# Menghitung koordinat tengah layar
x_tengah = (screen_width - gambar_width) // 2
y_tengah = (screen_height - gambar_height) // 2

# Memuat musik
pygame.mixer.music.load("GAME/Socapex - Dark ambiance.mp3")
pygame.mixer.music.play(-1)  # Putar musik secara terus-menerus

# Game loop
running = True
while running:
    # Menangani event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar di tengah layar
    screen.blit(gambar, (x_tengah, y_tengah))
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()