import pygame 
from config import*

class NPC:
  def __init__(self,position,dialog_text):
      self.image = pygame.image.load('Level/npc.png').convert_alpha()
      self.img_resized= pygame.transform.scale(self.image, (200,200))
      self.rect = self.img_resized.get_rect(topleft=position)
      self.dialog_text = dialog_text
      self.dialog_bg_image = pygame.image.load('Level/brown_age_by_darkwood67.jpg').convert_alpha()
      self.dialog_bg_image = pygame.transform.scale(self.dialog_bg_image, (300, 200))  # Resize dialog background
      self.dialog_rect = self.dialog_bg_image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))  # Center dialog window
      self.font = pygame.font.Font('Font/joystix monospace.otf', 12)
      self.showing_dialog = False
    
  def draw(self, screen):
      screen.blit(self.img_resized, self.rect.topleft)
      if self.showing_dialog:
          screen.blit(self.dialog_bg_image, self.dialog_rect.topleft)
          self.draw_text(screen, self.dialog_text, self.font, (0, 0, 0), self.dialog_rect)

  def draw_text(self, screen, text, font, color, rect):
      lines = self.wrap_text(text, font, rect.width)
      y_offset = rect.y + 10
      for line in lines:
          text_surface = font.render(line, True, color)
          text_rect = text_surface.get_rect(center=(rect.centerx, y_offset))
          screen.blit(text_surface, text_rect.topleft)
          y_offset += font.get_linesize() + 5
        
  def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
        return lines

  def toggle_dialog(self):
        self.showing_dialog = not self.showing_dialog

    
