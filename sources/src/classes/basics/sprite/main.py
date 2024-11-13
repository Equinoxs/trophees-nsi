import pygame
import json
import os

from src.classes import Vector2


class Sprite:
	def __init__(self, position: Vector2, image_path: str):
		self.position = position

		png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../assets/images', image_path + '.png')
		json_path = os.path.join('/'.join(png_path.split('/')[0:-1]), 'info.json')
		self.original_image = pygame.image.load(png_path)
		self.image = pygame.image.load(png_path)
		self.image_path = image_path
		with open(json_path, 'r') as file:
			data = json.load(file)

		self.image_data = data  # les infos de l'image
		self.magnification_coeff = 1  # image x fois plus grande
		self.frame_index = -1  # première frame au début
		self.go_next_frame()

	def get_position(self):
		return self.position

	def get_image(self):
		return self.image

	def go_next_frame(self, coeff=1):
		# Récupérer la taille de l'image
		if self.frame_index == len(self.image_data['widths']) - 1:
			self.frame_index = 0
		else:
			self.frame_index += 1
  
		_, height = self.image.get_size()
		# print("LEFT", self.image_data['widths'][0:self.frame_index], len(self.image_data['widths']))
		left = sum(self.image_data['widths'][0:self.frame_index])
		# print("WIDTHS", self.image_data['widths'], self.frame_index)
		right = int((left + self.image_data['widths'][self.frame_index]) * coeff)
		if right % 2 == 0:
			right -= 1
		# print("RIGHT", (left + self.image_data['widths'][self.frame_index]))

		# Rogner l'image (subsurface)
		# print("SUBSURFACE", (left, 0, right - left, height))
		self.image = self.original_image.subsurface((left, 0, right - left, height))

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
