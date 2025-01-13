import pygame

from src.classes import GameLoop, Vector2, DataHandler, SCREEN_WIDTH, SCREEN_HEIGHT


class UIElement:
	def __init__(self, data):
		classes_data = DataHandler().load_menus()['classes']
		while 'class' in set(data.keys()):  # Pour que les classes puissent utiliser des classes
			class_names = data.pop('class')
			class_names = class_names.split(' ')
			class_names.reverse()
			for class_name in class_names:  # Pour pouvoir utiliser plusieurs classes en meme temps séparés d'un espace
				class_properties = classes_data.get(class_name, {})
				data = {**class_properties, **data}

		# Données de bases
		self.border_radius = data.get('border_radius', 0)
		self.label = data.get('label', '')
		self.position = Vector2(data.get('x', 0), data.get('y', 0))
		self.color = tuple(data.get('color', (0,) * 4))
		self.text_color = tuple(data.get('text_color', (0, 0, 0)))

		# Les images
		self.image_path = data.get('image', None)
		self.original_image = None
		self.image = None
		self.image_height = data.get('image_height', None)
		if self.image_path is not None:
			self.original_image = pygame.image.load(DataHandler().load_ui_elements_image(self.image_path))
			self.image = pygame.transform.scale(self.original_image, (self.image_height / self.original_image.get_height() * self.original_image.get_width(), self.image_height))

		# Les bordures
		self.border_length = data.get('border_length', 0)
		self.border_color = tuple(data.get('border_color', (0,) * 3))

		width = data.get('width', SCREEN_WIDTH)
		height = data.get('height', SCREEN_HEIGHT)
		self.font = pygame.font.Font(None, data.get('font_size', 24))
		self._text_surface = self.font.render(self.label, True, self.text_color)

		# --- Compréhension des dimensions de l'élément ---
		if width == 'auto':
			width = self._text_surface.get_width() + 10  # 10px de padding horizontal
		if height == 'auto':
			height = self._text_surface.get_height() + 10  # 10px de padding vertical

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
		# Mise à jour du rect basé sur la position et la surface
		self.rect = pygame.Rect(self.position.get_x(), self.position.get_y(), self.surface.get_width(), self.surface.get_height())
		self._text_rect = self._text_surface.get_rect(center=self.rect.center)

	def get_rect(self):
		return self.rect

	def update(self):
		pass

	def render(self):
		self.update_rect()
		pygame.draw.rect(GameLoop().get_camera().get_surface('menu'), self.color, self.rect, border_radius=self.border_radius)
		if self.border_length > 0:
			pygame.draw.rect(GameLoop().get_camera().get_surface('menu'), self.border_color, self.rect, width=self.border_length, border_radius=self.border_radius)
		GameLoop().get_camera().draw(self._text_surface, self._text_rect.topleft, 'menu')
		if self.image is not None:
			GameLoop().get_camera().draw(self.image, self.position, 'menu')
