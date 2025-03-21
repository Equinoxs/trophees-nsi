import pygame

from src import UIElement, ButtonActions, ControlHandler


class Button(UIElement):
	def __init__(self, data):
		UIElement.__init__(self, data)
		self.action_name = data['action']

	def get_action_name(self):
		return self.action_name

	def update(self):
		super().update()
		if ControlHandler().is_clicked(self):
			ControlHandler().consume_event('clicked')
			ButtonActions().do(self.action_name, self)
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return True
		else:
			return False
