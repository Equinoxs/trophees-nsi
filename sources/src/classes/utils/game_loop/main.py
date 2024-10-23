import pygame

from .....main import control_handler, time_handler, save_handler
from ...specific import Player

class GameLoop:
	def __init__(self):
		self.running = True
		time_handler.set_clock(pygame.time.Clock())

		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
  
		self.saved_data = save_handler.get_data_from_last_save()
		self.player = Player(self.saved_data['player']['position'], self.saved_data['player']['image'], self.saved_data['player']['z_index'])

		while self.running:
			self.update()
			pygame.display.flip()  # Rafraîchit l'écran

		pygame.quit()

	def update(self):
		control_handler.handleEvents(pygame)
		if control_handler.is_activated('quit'):
			self.running = False

		time_handler.update()
		self.player.update()
