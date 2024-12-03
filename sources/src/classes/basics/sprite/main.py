import pygame
import json
import os

from src.classes import Vector2, DataHandler


class Sprite:
	def __init__(self, position: Vector2, image_path: str):
		self.position = position

		data, png_path = DataHandler().load_image(image_path)

		self.original_image = pygame.image.load(png_path)
		self.image = pygame.image.load(png_path)
		self.image_path = image_path

		self.image_data = data  # les infos de l'image
		self.magnification_coeff = 1  # image x fois plus grande
		self.vertical_flip = False
		self.horizontal_flip = False
		self.go_to_frame(0, 'walking')  # à rendre ça dynamique

	def switch_horizontal_flip(self):
		self.horizontal_flip = not self.horizontal_flip
		self.image = pygame.transform.flip(self.image, True, self.vertical_flip)

	def switch_vertical_flip(self):
		self.vertical_flip = not self.vertical_flip
		self.image = pygame.transform.flip(self.image, self.horizontal_flip, True)

	def get_position(self):
		return self.position

	def get_image(self):
		return self.image

	def get_image_data(self):
		return self.image_data

	def go_to_frame(self, frame_index, animation_name, coeff=1):
		width, height = self.image.get_size()
		if self.image_data['animations'] == {}:
			return
		left = sum(frame["width"] for frame in self.image_data['animations'][animation_name]['widths'][0:frame_index])

		top = 0
		for animation_key, val in self.image_data['animations'].items():
			if animation_key == animation_name:
				subsurface_height = val["height"]
				break
			top += val["height"]

		if len(self.image_data['animations'][animation_name]['widths']) == 0:
			subsurface_width = width
		else:
			subsurface_width = int((self.image_data['animations'][animation_name]['widths'][frame_index]["width"]) * coeff)

		# Ajuster pour éviter les erreurs liées à des tailles impaires
		subsurface_width += subsurface_width % 2 - 1
		subsurface_height += subsurface_height % 2 - 1

		# Rogner l'image (subsurface)
		self.image = self.original_image.subsurface((left, top, subsurface_width, subsurface_height))

		# Réappliquer les inversions d'axes
		self.image = pygame.transform.flip(self.image, self.horizontal_flip, self.vertical_flip)

	def get_magnification(self):
		return self.magnification_coeff

	def set_magnification(self, magnification_coeff):
		width, height = self.image.get_size()

		# Redimensionner l'image (scale)
		self.image = pygame.transform.scale(self.image, (width * magnification_coeff, height * magnification_coeff))
		self.magnification_coeff = magnification_coeff

	def rotate(self, angle):
		# Rotation de l'image
		self.image = pygame.transform.rotate(self.image, angle)

	def move_to(self, position: Vector2):
		self.position.copy(position)
