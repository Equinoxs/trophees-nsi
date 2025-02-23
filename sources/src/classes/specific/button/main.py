import pygame

from src.classes import UIElement, ButtonActions, ControlHandler


class Button(UIElement):
	def __init__(self, data):
		UIElement.__init__(self, data)
		self.action_name = data['action']

	def update(self):
		super().update()
		if ControlHandler().is_clicked(self):
			ControlHandler().consume_event('clicked')
			ButtonActions().do(self.action_name)
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return True
		else:
			return False
