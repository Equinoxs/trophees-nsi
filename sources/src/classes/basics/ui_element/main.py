import pygame

from src.classes import GameLoop, Vector2


class UIElement:
	def __init__(self, data):
		self.position = Vector2(data.get('x', 0), data.get('y', 0))
		self.surface = pygame.Surface((data.get('width', 100), data.get('height', 50)), pygame.SRCALPHA)
		self.rect = pygame.Rect(self.position.get_x(), self.position.get_y(), self.surface.get_width(), self.surface.get_height())
		self.label = data.get('label', '')
		self.color = tuple(data.get('color', (255,) * 4))
		self.text_color = tuple(data.get('text_color', (0, 0, 0)))
		self.font = pygame.font.Font(None, data.get('font_size', 24))
		self.surface.fill(self.color)
		self._text_surface = None

	def get_rect(self):
		return self.rect

	def update(self):
		pass

	def render(self):
		pygame.draw.rect(GameLoop().get_camera().get_surface('menu'), self.color, self.rect)
		if not self._text_surface:
			self._text_surface = self.font.render(self.label, True, self.text_color)
			self._text_surface.get_rect(center=self.rect.center)
		GameLoop().get_camera().draw(self._text_surface, self.position, 'menu')
