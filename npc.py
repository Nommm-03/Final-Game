import pygame 
from config import*

class NPC:
  def _init_(self,position,dialog_text):
      self.image = pygame.image.load('Level/npc.png').convert_alpha()
      self.img_resized= pygame.transform.scale(self.image, (200,200))
      self.rect = self.img_resized.get_rect(topleft=position)
      self.dialog_text = dialog_text
      self.dialog_bg_image = pygame.image.load('Level/brown_age_by_darkwood67.jpg').convert_alpha()
      self.dialog_bg_image = pygame.transform.scale(self.dialog_bg_image, (300, 200))  # Resize dialog background
      self.dialog_rect = self.dialog_bg_image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))  # Center dialog window
      self.font = pygame.font.Font('Font/joystix monospace.otf', 12)
      self.showing_dialog = False
