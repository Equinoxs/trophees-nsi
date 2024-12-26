import pygame
import math

from src.classes import MapObject, DataHandler, Vector2


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
		self.image_data = image_data
  
		self.position = Vector2(0, 0)
		self.calculate_wall_image()

		data['position'] = self.position
		self.image_data['hitbox'] = self.boundaries
		self.image_data['animations'] = {}
		super().__init__(data)

	def calculate_wall_image(self):
		self.position = self.boundaries[0].copy()
		self.position.set_y(self.position.get_y() - self.wall_height)

		for i in range(1, len(self.boundaries)):
			p1 = self.boundaries[i - 1]
			p2 = self.boundaries[i]
			p1_to_p2 = p2 - p1
			front_width = int(p1_to_p2.get_norm())

			# Pour le calcul de la position
			if p1_to_p2.get_y() < 0:
				self.position.set_y(self.position.get_y() - p1_to_p2.get_y())
   
			if p1_to_p2.get_x() * p1_to_p2.get_y() < 0:
				direction = -1  # coins haut-droit et bas-gauche
			else:
				direction = 1

			# Calcul du vecteur normal dirigé vers le haut (ne marche pas)
			normal_vector = Vector2(-p1_to_p2.get_y(), p1_to_p2.get_x())
			normal_vector.set_norm(self.wall_width)
			if normal_vector.get_y() > 0:
				normal_vector *= -1
   
			# --- Création des faces du mur ---
			# Face supérieure (top)
			top_image = self.fill_surface(self.original_top_image, front_width, self.wall_width)
			top_image = pygame.transform.scale(top_image, (abs(p1_to_p2.get_x()), -normal_vector.get_y()))
			top_image_perspective = self.skew_image(top_image, -normal_vector.get_x(), p1_to_p2.get_y())
   
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
			wall_image.blit(top_image_perspective, (0, 0))

			if direction == -1:
				wall_image.blit(side_image_perspective, (0, max_height - side_image_perspective.get_height()))
				wall_image.blit(front_image_perspective, (side_image_perspective.get_width(), max_height - front_image_perspective.get_height()))
			else:
				wall_image.blit(front_image_perspective, (0, max_height - front_image_perspective.get_height()))
				wall_image.blit(side_image_perspective, (front_image_perspective.get_width(), max_height - side_image_perspective.get_height()))

			# Sauvegarde de l'image finale
			self.image = wall_image
