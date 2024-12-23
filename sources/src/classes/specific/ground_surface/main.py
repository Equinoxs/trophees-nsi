import pygame

from src.classes import MapElement, Vector2, Player, Camera


class GroundSurface(MapElement):
	def __init__(self, data):
		self.image_type = 'ground_surface'
		super().__init__(data)
		self.boundaries: list[Vector2] = data['boundaries']
		self.pattern_image = self.image.copy()
		self.required_level = data['required_level']
		self.does_player_see = False
		self.ground_type = self.image_data['type']

		# Calcul de la largeur et de la hauteur maximales
		max_width, max_height = 0, 0
		relative_position = Vector2(0, 0)
		for vector in self.boundaries:
			max_width = max(max_width, vector.get_x())
			relative_position.set_x(min(relative_position.get_x(), vector.get_x()))
			max_height = max(max_height, vector.get_y())
			relative_position.set_y(min(relative_position.get_y(), vector.get_y()))
		self.position.add(relative_position)
		self.boundaries = [vector.add(relative_position * -1) for vector in self.boundaries]
		max_width -= relative_position.get_x()
		max_height -= relative_position.get_y()

		# Création des surfaces nécessaires
		mask_surface = pygame.Surface((max_width, max_height), pygame.SRCALPHA)
		big_rectangle = pygame.Surface((max_width, max_height), pygame.SRCALPHA)

		# Remplissage du grand rectangle avec l'image du motif
		pattern_width, pattern_height = self.pattern_image.get_size()
		for x in range(0, max_width, pattern_width):
			for y in range(0, max_height, pattern_height):
				big_rectangle.blit(self.pattern_image, (x, y))

		# Création du masque à partir des frontières
		mask_surface.fill((0, 0, 0, 0))
		pygame.draw.polygon(
			mask_surface, (255, 255, 255, 255),
			[(vector.get_x(), vector.get_y()) for vector in self.boundaries]
		)

		# Application du masque pour générer l'image finale
		masked_surface = pygame.Surface((max_width, max_height), pygame.SRCALPHA)
		masked_surface.blit(big_rectangle, (0, 0))
		masked_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
		self.image = masked_surface
		self.access_overlay = self.image.copy()
		filter_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
		filter_surface.fill((0, 0, 0, 200))
		self.access_overlay.blit(filter_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

	def catch_event(self, event):
		MapElement.catch_event(self, event)
		if event == 'player_level_change':
			if Player().get_level() < self.required_level:
				self.does_player_see = False
			else:
				self.does_player_see = True

	def get_ground_type(self):
		return self.ground_type

	def point_in_boundaries(self, point):
		x, y = point.convert_to_tuple()
		n = len(self.boundaries)
		inside = False

		px1, py1 = self.boundaries[0].convert_to_tuple()
		for i in range(1, n + 1):
			px2, py2 = self.boundaries[i % n].convert_to_tuple()

			# Vérifie si le point est dans la plage de y des deux sommets
			if min(py1, py2) < y <= max(py1, py2):
				# Calcule l'intersection sur l'axe X avec la frontière du polygone
				if px1 != px2:  # Évite une division par zéro
					xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
				else:
					xinters = px1

				# Vérifie si le point est à gauche ou sur l'intersection
				if x <= xinters:
					inside = not inside

			px1, py1 = px2, py2

		return inside

	def update(self):
		if Player().get_level() < self.required_level:
			self.does_player_see = False
		else:
			self.does_player_see = True

	def render(self):
		super().render()
		if not self.does_player_see:
			Camera().get_screen().blit(
				self.access_overlay,
				(
					Camera().get_zoom() * (self.position.x - Camera().get_camera().x),
					Camera().get_zoom() * (self.position.y - Camera().get_camera().y)
				)
			)
