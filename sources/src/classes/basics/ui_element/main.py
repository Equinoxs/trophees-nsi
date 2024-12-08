import pygame


class UIElement:
	def __init__(self, data):
		self.rect = pygame.Rect(data.get('x', 0), data.get('y', 0), data.get('width', 100), data.get('height', 50))
		self.label = data.get('label', '')
		self.color = tuple(data.get('color', (255, 255, 255)))
		self.text_color = tuple(data.get('text_color', (0, 0, 0)))
		self.font = pygame.font.Font(None, data.get('font_size', 24))
		self._text_surface = None
		self._text_rect = None

	def get_rect(self):
		return self.rect

	def update(self):
		return

	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
		if not self._text_surface:
			self._text_surface = self.font.render(self.label, True, self.text_color)
			self._text_rect = self._text_surface.get_rect(center=self.rect.center)
		screen.blit(self._text_surface, self._text_rect)
