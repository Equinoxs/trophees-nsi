#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame
import math

from src import RidgeObject, Vector2, DataHandler


class WallSegment(RidgeObject):
	def __init__(self, data):
		self.initialized = False

		self.image_type = 'wall'
		self.wall_type = data['wall_type']
		self.wall_height = data['wall_height']
		self.wall_width = data['wall_width']
		self.boundaries = [data['segment'][0], data['segment'][-1]]
		self.stickers = data['segment'][1:-1]
		self.before_angle = data['before_angle']
		self.after_angle = data['after_angle']

		image_data, front_data, side_data, top_data = DataHandler().load_wall_images(self.wall_type)
		self.original_front_image = pygame.image.load(front_data['path']).convert_alpha()

		if side_data:
			self.original_side_image = pygame.image.load(side_data['path']).convert_alpha()
		else:
			self.original_side_image = pygame.Surface((10, 10), pygame.SRCALPHA)
			self.original_side_image.fill((0,) * 4)

		if top_data:
			self.original_top_image = pygame.image.load(top_data['path'])
		else:
			self.original_top_image = pygame.Surface((10, 10), pygame.SRCALPHA)
			self.original_top_image.fill((0,) * 4)

		self.image_data = image_data

		if front_data['height'] is not None:
			self.original_front_image = pygame.transform.scale(self.original_front_image, (
				int(front_data['height'] / self.original_front_image.get_height() * self.original_front_image.get_width()),
				front_data['height']
			))
		if side_data and side_data['height'] is not None:
			self.original_side_image = pygame.transform.scale(self.original_side_image, (
				int(side_data['height'] / self.original_side_image.get_height() * self.original_side_image.get_width()),
				side_data['height']
			))
		if top_data and top_data['height'] is not None:
			self.original_top_image = pygame.transform.scale(self.original_top_image, (
				int(top_data['height'] / self.original_top_image.get_height() * self.original_top_image.get_width()),
				top_data['height']
			))

		if self.wall_height is None:
			self.wall_height = image_data['height']
		if not side_data:
			self.wall_width = 1
		elif self.wall_width is None:
			self.wall_width = image_data['width']

		self.front_image_perspective = None
		self.side_image_perspective = None
		self.top_image_perspective = None

		self.position = self.boundaries[0].copy()
		self.normal_vector = None
		self.p1_to_p2 = None
		self.front_width = None
		self.direction = None
		self.before_angle_vector = None
		self.after_angle_vector = None

		if self.wall_width > 0:
			self.calculate_wall_image()

		data['position'] = self.position
		self.hitbox = [vector - self.position for vector in self.boundaries]
		self.image_data['animations'] = {}
		self.original_image = None
		self.hitbox_closed = False
		self.hitbox_action_radius = data.get('hitbox_action_radius', 20)

		super().__init__(data)

		if self.wall_width == 0:
			self.must_render = False

	def calculate_front_image_perspective(self):
		self.front_image_perspective = pygame.Surface((0, self.front_width + self.wall_height + abs(self.p1_to_p2.orthogonal_projection(self.after_angle_vector).get_y()) + abs(self.p1_to_p2.orthogonal_projection(self.before_angle_vector).get_y())), pygame.SRCALPHA).convert_alpha()
		if self.p1_to_p2.get_x() != 0:
			front_image = self.fill_surface(self.original_front_image, self.front_width, self.wall_height)
			front_image = pygame.transform.scale(front_image, (abs(self.p1_to_p2.get_x()), self.wall_height))
			self.front_image_perspective = self.skew_image(front_image, 0, abs(self.p1_to_p2.get_y()) * self.direction)

			if self.p1_to_p2.get_x() < 0:
				sense = -1
			else:
				sense = 1
   
			for sticker in self.stickers:
				sticker_data, sticker_image = DataHandler().load_sticker_data(sticker['sticker'], sticker.get('height', None))
				sticker_vector = self.p1_to_p2.copy().set_norm(sticker_image.get_width())
				sticker_image = pygame.transform.scale(sticker_image, (abs(sticker_vector.get_x()), sticker_image.get_height()))
				sticker_image = self.skew_image(sticker_image, 0, abs(sticker_vector.get_y()) * self.direction)

				x_offset = sticker.get('x_offset', 0)
				if x_offset == 'middle':
					x_offset = (self.front_width - sticker_image.get_width()) / 2
				if x_offset < 0:
					x_offset = self.front_width - sticker_image.get_width() + x_offset

				y_offset = sticker.get('y_offset', sticker_data.get('top', 0))
				if y_offset == 'middle':
					y_offset = (self.wall_height - sticker_image.get_height()) / 2
				if y_offset < 0:
					y_offset = self.wall_height - sticker_image.get_height() + y_offset

				offset_vector = self.p1_to_p2.copy().set_norm(x_offset) + Vector2(0, y_offset)
				offset_vector.set_x(offset_vector.get_x() * sense)
				self.front_image_perspective.blit(sticker_image, (offset_vector).int().convert_to_tuple())

	def calculate_side_image_perspective(self):
		self.side_image_perspective = pygame.Surface((0, self.wall_height - 2 * self.normal_vector.get_y())).convert_alpha()
		if self.p1_to_p2.get_y() != 0:
			side_image = self.fill_surface(self.original_side_image, self.wall_width, self.wall_height)
			side_scaled_width = int(abs(self.normal_vector.copy().normalize().get_x()) * self.wall_width)
			side_image = pygame.transform.scale(side_image, (side_scaled_width, self.wall_height))
			self.side_image_perspective = self.skew_image(side_image, 0, 2 * self.normal_vector.get_y() * self.direction)

	def calculate_top_image_perspective(self):
		top_image = self.fill_surface(self.original_top_image, self.front_width, self.wall_width)
		angle = math.acos(self.p1_to_p2.get_x() / self.front_width) / math.pi * 180
		if self.direction == -1 and angle > 90 or self.direction == 1 and angle <= 90:
			angle *= -1
		self.top_image_perspective = pygame.transform.rotate(top_image, angle)

	def calculate_before_angle_vector(self):
		angle = self.before_angle / 2
		composant_p1_to_p2 = self.p1_to_p2.copy().set_norm(math.sin(angle) * self.wall_width / 2)
		self.before_angle_vector = self.normal_vector.copy().set_norm(self.wall_width / 2) + composant_p1_to_p2
		if self.before_angle_vector.angle_to(self.normal_vector) > math.pi / 2:
			self.before_angle_vector *= -1

	def calculate_after_angle_vector(self):
		angle = self.after_angle / 2
		composant_p1_to_p2 = self.p1_to_p2.copy().set_norm(math.sin(angle) * self.wall_width / 2)
		self.after_angle_vector = self.normal_vector.copy().set_norm(self.wall_width / 2) + composant_p1_to_p2
		if self.after_angle_vector.angle_to(self.normal_vector) > math.pi / 2:
			self.after_angle_vector *= -1


	def calculate_wall_image(self):
		# --- Détermination des caractéristiques de la tranche ---
		p1 = self.boundaries[0]
		p2 = self.boundaries[1]
		self.p1_to_p2 = p2 - p1
		self.front_width = int(self.p1_to_p2.get_norm())

		if self.front_width == 0:
			return

		if self.p1_to_p2.get_x() * self.p1_to_p2.get_y() < 0:
			self.direction = -1  # coins haut-droit et bas-gauche
		else:
			self.direction = 1

		# Calcul du vecteur normal dirigé vers le haut (ne marche pas)
		self.normal_vector = Vector2(-self.p1_to_p2.get_y(), self.p1_to_p2.get_x())
		self.normal_vector.set_norm(self.wall_width / 2)
		if self.normal_vector.get_y() > 0:
			self.normal_vector *= -1
		elif self.normal_vector.get_y() == 0 and self.normal_vector.get_x() < 0:
			self.normal_vector *= -1

		# Calcul des vecteurs avant et arrière
		self.calculate_before_angle_vector()
		self.calculate_after_angle_vector()

		# Création de quelques références pour simplifier la logique du code
		if self.p1_to_p2.get_y() < 0:
			top_angle_vector = self.after_angle_vector
			bottom_angle_vector = self.before_angle_vector
		else:
			top_angle_vector = self.before_angle_vector
			bottom_angle_vector = self.after_angle_vector
		if self.p1_to_p2.get_x():
			left_angle_vector = self.after_angle_vector
			right_angle_vector = self.before_angle_vector
		else:
			left_angle_vector = self.before_angle_vector
			right_angle_vector = self.after_angle_vector

		self.position.set_x(min(p1.get_x(), p2.get_x()) - abs(left_angle_vector.get_x()))
		self.position.set_y(min(p1.get_y(), p2.get_y()) - abs(top_angle_vector.get_y()))

		# --- Création des faces du mur ---
		self.calculate_front_image_perspective()
		self.calculate_side_image_perspective()
		self.calculate_top_image_perspective()

		# --- Assemblage de l'image du mur ---
		max_width = self.front_image_perspective.get_width() + self.side_image_perspective.get_width()
		max_height = self.front_image_perspective.get_height() - 2 * self.normal_vector.get_y()
		self.image = pygame.Surface((max_width, max_height), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))

		self.image.blit(self.top_image_perspective, (0, max_height - self.wall_height - self.top_image_perspective.get_height() + 1))
		if self.direction == -1:
			self.image.blit(self.side_image_perspective, (0, max_height - self.side_image_perspective.get_height()))
			self.image.blit(self.front_image_perspective, (self.side_image_perspective.get_width(), -2 * self.normal_vector.get_y()))
		else:
			self.image.blit(self.front_image_perspective, (0, -2 * self.normal_vector.get_y()))
			self.image.blit(self.side_image_perspective, (self.front_image_perspective.get_width(), max_height - self.side_image_perspective.get_height()))

	def render(self):
		y = self.position.get_y()
		self.position.set_y(y - self.wall_height)
		super().render()
		self.position.set_y(y)

	def get_data(self):
		return None
