from src.classes import ui_element
import pygame

class Button:
    def __init__(self, x, y, width, height, label, action, color=(0, 128, 255), text_color=(255, 255, 255), text_font=None, font_size=36):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.action = action
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(text_font, font_size) if text_font else pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        self.action()
