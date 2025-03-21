import pygame

from src import MapElement, Vector2, Player, Camera


class GroundSurface(MapElement):
	def __init__(self, data):
		if not hasattr(self, 'image_type'):
			self.image_type = 'ground_surface'
		data['position'] = Vector2()
		super().__init__(data)

		self.boundaries: list[Vector2] = data['boundaries']
		self.required_level = data['required_level']
		self.does_player_see = False
		self.ground_type = self.image_data['type']
  
		if len(self.boundaries) <= 2:
			self.access_overlay = None
			return

		self.pattern_image = self.image.copy()

		# Calcul de la largeur et de la hauteur maximales
		max_width, max_height = 0, 0
		relative_position = Vector2(float('inf'), float('inf'))
		for vector in self.boundaries:
			max_width = max(max_width, vector.get_x())
			relative_position.set_x(min(relative_position.get_x(), vector.get_x()))
			max_height = max(max_height, vector.get_y())
			relative_position.set_y(min(relative_position.get_y(), vector.get_y()))
		self.position.add(relative_position)
		self.positive_boundaries = [vector.copy().add(-relative_position) for vector in self.boundaries]
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
			[vector.convert_to_tuple() for vector in self.positive_boundaries]
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
		inside = False
		n = len(self.boundaries)
		
		for i in range(n):
			px1, py1 = self.boundaries[i].convert_to_tuple()
			px2, py2 = self.boundaries[(i + 1) % n].convert_to_tuple()

			# Vérifie si le point est entre les y des deux sommets
			if (py1 <= y < py2) or (py2 <= y < py1):
				# Évite la division par zéro pour les segments verticaux
				if px1 == px2:
					intersection_x = px1
				else:
					# Calcule l'intersection avec la ligne horizontale passant par y
					a = (py2 - py1) / (px2 - px1)
					intersection_x = px1 + (y - py1) / a

				# Si le point est à gauche de l'intersection, change l'état
				if x < intersection_x:
					inside = not inside

		return inside

	def set_magnification(self, magnification_coeff):
		super().set_magnification(magnification_coeff)
		if self.access_overlay is not None:
			width, height = self.access_overlay.get_size()
			self.access_overlay = pygame.transform.scale(self.access_overlay, (int(width * magnification_coeff), int(height * magnification_coeff)))

	def update(self):
		if Player().get_level() < self.required_level:
			self.does_player_see = False
		else:
			self.does_player_see = True

	def render(self):
		rendered = super().render()
		if not self.does_player_see and rendered and self.access_overlay is not None:
			Camera().draw(self.access_overlay, self.position)

	def get_data(self):
		data = super().get_data()
		if 'position' in data:
			del data['position'] # pas besoin dans la sauvegarde
		return data