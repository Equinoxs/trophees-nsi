import pygame

from src.classes import GameLoop, Vector2, SCREEN_WIDTH, SCREEN_HEIGHT


class UIElement:
	def __init__(self, data):
		# Données de bases
		self.border_radius = data.get('border_radius', 0)
		self.label = data.get('label', '')
		self.position = Vector2(data.get('x', 0), data.get('y', 0))
		self.color = tuple(data.get('color', (255,) * 4))
		self.text_color = tuple(data.get('text_color', (0, 0, 0)))

		width = data.get('width', SCREEN_WIDTH)
		height = data.get('height', SCREEN_HEIGHT)
		self.font = pygame.font.Font(None, data.get('font_size', 24))
		self._text_surface = self.font.render(self.label, True, self.text_color)
  
		# --- Compréhension des dimensions de l'élément ---
		if width == 'auto' :
			width = self._text_surface.get_width() + 10  # 10px de margin horizontal
		if height == 'auto' :
			height = self._text_surface.get_height() + 10  # 10px de margin vertical

		self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
		self.surface.fill(self.color)

		# --- Compréhension des positions de l'élément ---
		if self.position.get_x() == 'center':
			self.position.set_x((SCREEN_WIDTH - self.surface.get_width()) // 2)
		if self.position.get_x() < 0:
			self.position.set_x(SCREEN_WIDTH + self.position.get_x() - self.surface.get_width())
   
		if self.position.get_y() == 'center':
			self.position.set_y((SCREEN_HEIGHT - self.surface.get_height()) // 2)
		if self.position.get_y() < 0:
			self.position.set_y(SCREEN_HEIGHT + self.position.get_y() - self.surface.get_height())
   
		self.rect = pygame.Rect(self.position.get_x(), self.position.get_y(), self.surface.get_width(), self.surface.get_height())
		self._text_rect = self._text_surface.get_rect(center=self.rect.center)

	def update_rect(self):
		self.rect = pygame.Rect(self.position.get_x(), self.position.get_y(), self.surface.get_width(), self.surface.get_height())

	def get_rect(self):
		return self.rect

	def update(self):
		pass

	def render(self):
		pygame.draw.rect(GameLoop().get_camera().get_surface('menu'), self.color, self.rect, border_radius=self.border_radius)
		GameLoop().get_camera().draw(self._text_surface, self._text_rect.topleft, 'menu')
