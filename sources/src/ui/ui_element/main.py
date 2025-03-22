import pygame

from src import GameLoop, Vector2, DataHandler, SCREEN_WIDTH, SCREEN_HEIGHT


class UIElement:
	def __init__(self, data: dict):
		classes_data = DataHandler().load_menus()['classes']
		while 'class' in set(data.keys()):  # Pour que les classes puissent utiliser des classes
			class_names = data.pop('class')
			class_names = class_names.split(' ')
			class_names.reverse()
			for class_name in class_names:  # Pour pouvoir utiliser plusieurs classes en meme temps séparés d'un espace
				class_properties = classes_data.get(class_name, {})
				copy = class_properties.copy()
				copy.update(data)
				data.clear()
				data.update(copy)

		# Données de bases
		self.border_radius = data.get('border_radius', 0)
		self.id = data.get('id', None)
		self.return_line = data.get('return_line', False)
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
		if data.get('font_family') == 'basic':
			self.font = pygame.font.Font(None, data.get('font_size', 35))
		else:
			self.font = DataHandler().load_font(data.get('font_family', 'default'), data.get('font_size', 24))

		# --- Compréhension des dimensions de l'élément ---
		self.surface_width = data.get('width', SCREEN_WIDTH)
		self.surface_height = data.get('height', SCREEN_HEIGHT)
		self.calculate_text_surface(self.surface_width)

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

		self.update_rect()

	def get_position(self):
		return self.position

	def set_color(self, new_color):
		self.color = new_color
		if type(self.color) == list:
			self.color = tuple(self.color)

	def get_id(self):
		return self.id

	def get_label(self):
		return self.label

	def set_label(self, new_label: str):
		self.label = str(new_label)
		self.calculate_text_surface(self.surface_width)

	def get_rect(self):
		return self.rect

	def get_image(self):
		return self.image

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
			if self.surface_width == 'auto':
				width = self._text_surface.get_width() + 10  # 10px de padding horizontal
			else:
				width = self.surface_width
			if self.surface_height == 'auto':
				height = self._text_surface.get_height() + 10  # 10px de padding vertical
			else:
				height = self.surface_height

		self.rect = pygame.Rect(pos_x, pos_y, width, height)
		self.calculate_text_rect()

	def calculate_text_surface(self, width: str):
		if self.return_line:
			if width == 'auto':
				raise ValueError('Cannot set "width" prop to "auto" when setting "return_line" to true.')

			words = self.label.split()  # Découper en mots
			lines = []
			current_line = ""

			for word in words:
				test_line = current_line + " " + word if current_line else word
				test_surface = self.font.render(test_line, True, self.text_color)

				if test_surface.get_width() > width:  # Dépassement de la ligne
					lines.append(current_line)  # Valider la ligne actuelle
					current_line = word  # Commencer une nouvelle ligne
				else:
					current_line = test_line  # Ajouter le mot

			if current_line:  # Ajouter la dernière ligne
				lines.append(current_line)

			# Créer une surface assez grande pour contenir tout le texte
			line_height = self.font.get_height()
			text_height = line_height * len(lines)
			self._text_surface = pygame.Surface((width, text_height), pygame.SRCALPHA)

			# Remplir la surface avec les lignes de texte
			y = 0
			for line in lines:
				text_surface = self.font.render(line, True, self.text_color)
				self._text_surface.blit(text_surface, (0, y))  # Aligné à gauche
				y += line_height  # Espacement entre les lignes
		else:
			self._text_surface = self.font.render(self.label, True, self.text_color)

	def calculate_text_rect(self):
		match self.text_align:
			case 'center':
				self._text_rect = self._text_surface.get_rect(center=self.rect.center)
			case 'left':
				self._text_rect = self._text_surface.get_rect(topleft=self.rect.topleft)
			case 'right':
				self._text_rect = self._text_surface.get_rect(topright=self.rect.topright)
			case 'mid_left':
				self._text_rect = self._text_surface.get_rect(midleft=(self.rect.centerx-180, self.rect.centery))
			case _:
				raise ValueError('Invalid text_align value')

	def render_text(self, surface = 'menu'):
		if self.label != '':
			GameLoop().get_camera().draw(self._text_surface, self._text_rect.topleft, surface)

	def update(self):
		self.update_rect()

	def render(self, surface = 'menu', render_surface = False):
		self.update_rect()

		if self.color != 'transparent':
			pygame.draw.rect(GameLoop().get_camera().get_surface(surface), self.color, self.rect, border_radius=self.border_radius)

		if self.border_length > 0:
			pygame.draw.rect(GameLoop().get_camera().get_surface(surface), self.border_color, self.rect, width=self.border_length, border_radius=self.border_radius)

		self.render_text(surface)

		if self.image is not None:
			GameLoop().get_camera().draw(self.image, (self.rect.x, self.rect.y), surface)

		if render_surface:
			GameLoop().get_camera().draw(self.surface, (self.rect.x, self.rect.y), surface)
