import pygame
import json
import os

from .. import Vector2


class Sprite:
	def __init__(self, position: Vector2, image_path: str):
		self.position = position
  
		path = os.path.join(os.path.abspath(__file__), '../../../../assets/images', image_path)
		self.image = pygame.image.load(os.path.join(path, image_path + '.png'))
		with open(os.path.join(path, image_path + '.json'), 'r') as file:
			data = json.load(file)
   
		self.image_data = data  # les infos de l'image
		self.magnification_coeff = 1  # image x fois plus grande
		self.frame_index = 0  # première frame au début

	def go_next_frame(self, coeff=1):
		# Récupérer la taille de l'image
		if self.frame_index == len(self.image_data['widths']):
			self.frame_index = 0
		else:
			self.frame_index += 1
  
		_, height = self.image.get_size()
		left = sum(self.data['widths'][0:self.index(-1)])
		right = (left + self.data['widths'][self.frame_index]) * coeff

		# Rogner l'image (subsurface)
		self.image = self.image.subsurface((left, 0, right - left, height))

	def set_magnification(self, magnification_coeff):
		width, height = self.image.get_size()

		# Redimensionner l'image (scale)
		self.image = pygame.transform.scale(self.image, width * magnification_coeff, height * magnification_coeff)
		self.magnification_coeff = magnification_coeff

	def rotate(self, angle):
		# Rotation de l'image
		self.image = pygame.transform.rotate(self.image, angle)

	def move(self, x, y):
		self.position.set_all(x, y)
