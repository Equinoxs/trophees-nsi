import pygame

from src.classes import Button, GameLoop


class MiniMap(Button):
	def __init__(self, data):
		data['action'] = 'open_map'
		data['color'] = (0,) * 4
		Button.__init__(self, data)

	def update(self):
		super().update()
		self.surface = GameLoop().get_camera().get_surface('mini_map')
		self.surface = pygame.transform.scale(self.surface, (self.rect.height / self.surface.get_height() * self.surface.get_width(), self.rect.height))
		self.update_rect()

	def render(self):
		GameLoop().get_camera().draw(self.surface, self.position, 'menu')