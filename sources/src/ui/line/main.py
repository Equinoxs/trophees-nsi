#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame

from src import UIElement, Vector2, GameLoop


class Line(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.start_pos: Vector2 = data.get('start_pos', Vector2())
		self.end_pos: Vector2 = data.get('end_pos', Vector2())
		self.color: tuple = data.get('color', (255, 255, 255, 255))
		self.width: int = data.get('width', 1)

	def set_color(self, new_color: tuple):
		self.color = new_color

	def set_width(self, new_width: int):
		self.width = new_width

	def get_start_pos(self):
		return self.start_pos

	def get_end_pos(self):
		return self.end_pos

	def update(self):
		pass

	def render(self):
		pygame.draw.line(GameLoop().get_camera().get_surface('menu'), self.color, self.start_pos.convert_to_tuple(), self.end_pos.convert_to_tuple(), self.width)
