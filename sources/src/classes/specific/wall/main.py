import pygame
import math

from src.classes import MapObject, DataHandler, Vector2, Camera


class Wall(MapObject):
	def __init__(self, data):
		self.image_type = 'wall'
		self.wall_type = data['wall_type']
		self.wall_height = data['wall_height']
		self.wall_width = data['wall_width']
		self.boundaries = data['boundaries']
  
		image_data, front_path, side_path, top_path = DataHandler().load_wall_images(self.wall_type)
		self.original_front_image = pygame.image.load(front_path)
		self.original_side_image = pygame.image.load(side_path)
		self.original_top_image = pygame.image.load(top_path)
		self.image = pygame.Surface((0, 0))
		self.image_data = image_data
		self.segments = []

		self.position = self.boundaries[0].copy()
		self.relative_boundaries = []
		self.calculate_wall_image()

		data['position'] = self.position
		self.image_data['hitbox'] = self.relative_boundaries
		self.image_data['animations'] = {}
		self.hitbox_closed = False
		super().__init__(data)

	def calculate_wall_image(self):

		for i in range(1, len(self.boundaries)):

			# --- Détermination des caractéristiques de la tranche ---
			p1 = self.boundaries[i - 1]
			p2 = self.boundaries[i]
			p1_to_p2 = p2 - p1
			front_width = int(p1_to_p2.get_norm())
   
			if p1_to_p2.get_x() * p1_to_p2.get_y() < 0:
				direction = -1  # coins haut-droit et bas-gauche
			else:
				direction = 1

			# Calcul du vecteur normal dirigé vers le haut (ne marche pas)
			normal_vector = Vector2(-p1_to_p2.get_y(), p1_to_p2.get_x())
			normal_vector.set_norm(self.wall_width)
			if normal_vector.get_y() > 0:
				normal_vector *= -1
   
			# --- Positions ---
			min_x = min(p1.get_x(), p2.get_x())
			if self.position.get_x() > min_x:
				self.position.set_x(min_x)
			min_y = min(p1.get_y(), p2.get_y())
			if self.position.get_y() > min_y:
				self.position.set_y(min_y + normal_vector.get_y())

			segment_position = p1.copy()
			min_x2 = min(p1.get_x(), p2.get_x())
			if segment_position.get_x() > min_x2:
				segment_position.set_x(min_x2)
			min_y2 = min(p1.get_y(), p2.get_y())
			if segment_position.get_y() > min_y2:
				segment_position.set_y(min_y2 + normal_vector.get_y())

			# --- Création des faces du mur ---
			# Face supérieure (top)
			top_image = self.fill_surface(self.original_top_image, front_width, self.wall_width)
			angle = math.acos(p1_to_p2.get_x() / front_width) / math.pi * 180
			if direction == -1 and angle > 90 or direction == 1 and angle <= 90:
				angle *= -1
			top_image_perspective = pygame.transform.rotate(top_image, angle)
   
			# Face avant (front)
			front_image_perspective = pygame.Surface((0, 0), pygame.SRCALPHA)
			if p1_to_p2.get_x() != 0:
				front_image = self.fill_surface(self.original_front_image, front_width, self.wall_height)
				front_image = pygame.transform.scale(front_image, (abs(p1_to_p2.get_x()), self.wall_height))
				front_image_perspective = self.skew_image(front_image, 0, abs(p1_to_p2.get_y()) * direction)

			# Face latérale (side)
			side_image_perspective = pygame.Surface((0, 0))
			if p1_to_p2.get_y() != 0:
				side_image = self.fill_surface(self.original_side_image, self.wall_width, self.wall_height)
				side_scaled_width = int(abs(normal_vector.copy().normalize().get_x()) * self.wall_width)
				side_image = pygame.transform.scale(side_image, (side_scaled_width, self.wall_height))
				side_image_perspective = self.skew_image(side_image, 0, normal_vector.get_y() * direction)

			# --- Assemblage de l'image du mur ---
			max_width = front_image_perspective.get_width() + side_image_perspective.get_width()
			max_height = front_image_perspective.get_height() - normal_vector.get_y()

			wall_image = pygame.Surface((max_width, max_height), pygame.SRCALPHA)
			wall_image.fill((0, 0, 0, 0))

			# Blit des différentes parties
			wall_image.blit(top_image_perspective, (0, max_height - self.wall_height - top_image_perspective.get_height() + 1))

			if direction == -1:
				wall_image.blit(side_image_perspective, (0, max_height - side_image_perspective.get_height()))
				wall_image.blit(front_image_perspective, (side_image_perspective.get_width(), -normal_vector.get_y()))
			else:
				wall_image.blit(front_image_perspective, (0, -normal_vector.get_y()))
				wall_image.blit(side_image_perspective, (front_image_perspective.get_width(), max_height - side_image_perspective.get_height()))

			# Sauvegarde de l'image finale
			self.segments.append({'position': segment_position, 'image': wall_image})
		self.relative_boundaries = [vector - self.position for vector in self.boundaries]

	def is_point_behind_wall(self, point: Vector2):
		behind = False
		for i in range(1, len(self.boundaries)):
			continue
		return behind

	def render(self):
		for wall_segment in self.segments:
			x, y = wall_segment['position'].convert_to_tuple()
			Camera().draw(wall_segment['image'], (x, y - self.wall_height))
