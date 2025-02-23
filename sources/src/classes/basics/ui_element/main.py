import pygame
import os
from src.classes import GameLoop, Vector2, DataHandler, SCREEN_WIDTH, SCREEN_HEIGHT


class UIElement:
	def __init__(self, data: dict):
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
		self.text_align = data.get('text_align', 'center')
		self.position = Vector2(data.get('x', 0), data.get('y', 0))
		self.color = data.get('color', 'transparent')
		if type(self.color) == list:
			self.color = tuple(self.color)
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

		# Le texte
		self.font = DataHandler().load_font(data.get('font_family', 'default'), data.get('font_size', 24))
		self.calculate_text_surface()

		# --- Compréhension des dimensions de l'élément ---
		self.surface_width = data.get('width', SCREEN_WIDTH)
		self.surface_height = data.get('height', SCREEN_HEIGHT)

		if self.surface_width == 'auto':
			width = self._text_surface.get_width() + 10  # 10px de padding horizontal
		else:
			width = self.surface_width
		if self.surface_height == 'auto':
			height = self._text_surface.get_height() + 10  # 10px de padding vertical
		else:
			height = self.surface_height

		self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
		if type(self.color) == tuple:
			self.surface.fill(self.color)

		self.rect = None
		self.update_rect()

	def update_rect(self):
		pos_x = self.position.get_x()
		pos_y = self.position.get_y()

		if pos_x == 'center':
			pos_x = (SCREEN_WIDTH - self.surface.get_width()) // 2
		if pos_x < 0:
			pos_x = SCREEN_WIDTH + pos_x - self.surface.get_width()

		if pos_y == 'center':
			pos_y = (SCREEN_HEIGHT - self.surface.get_height()) // 2
		if pos_y < 0:
			pos_y = SCREEN_HEIGHT + pos_y - self.surface.get_height()

		if self.image is not None:
			width = max(self.surface.get_width(), self.image.get_width())
			height = max(self.surface.get_height(), self.image.get_height())
		else:
			width = self.surface.get_width()
			height = self.surface.get_height()

		self.rect = pygame.Rect(pos_x, pos_y, width, height)
		self.calculate_text_rect()

	def set_label(self, new_label: str):
		self.label = str(new_label)
		self.calculate_text_surface()

	def get_rect(self):
		return self.rect

	def get_image(self):
		return self.image

	def get_position(self):
		return self.position

	def update(self):
		self.update_rect()

	def render(self, surface = 'menu', render_surface = False):
		self.update_rect()

		if self.color != 'transparent':
			pygame.draw.rect(GameLoop().get_camera().get_surface(surface), self.color, self.rect, border_radius=self.border_radius)

		if self.border_length > 0:
			pygame.draw.rect(GameLoop().get_camera().get_surface(surface), self.border_color, self.rect, width=self.border_length, border_radius=self.border_radius)

		self.render_text()

		if self.image is not None:
			GameLoop().get_camera().draw(self.image, (self.rect.x, self.rect.y), surface)

		if render_surface:
			GameLoop().get_camera().draw(self.surface, (self.rect.x, self.rect.y), surface)

	def render_text(self, surface = 'menu'):
		if self.label != '':
			GameLoop().get_camera().draw(self._text_surface, self._text_rect.topleft, surface)

	def calculate_text_surface(self):
		self._text_surface = self.font.render(self.label, True, self.text_color)

	def calculate_text_rect(self):
		match self.text_align:
			case 'center':
				self._text_rect = self._text_surface.get_rect(center=self.rect.center)
			case 'left':
				self._text_rect = self._text_surface.get_rect(topleft=self.rect.topleft)
			case 'right':
				self._text_rect = self._text_surface.get_rect(topright=self.rect.topright)
			case _:
				raise ValueError('Invalid text_align value')
