import pygame

from src.classes import ControlHandler, TimeHandler, SaveHandler, Player


class GameLoop:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		self.running = True
		TimeHandler().set_clock(pygame.time.Clock())

		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
  
		self.saved_data = SaveHandler().get_data_from_last_save()
		self.player = Player(self.saved_data['player']['position'], self.saved_data['player']['image'], self.saved_data['player']['z_index'])

		while self.running:
			self.update()
			pygame.display.flip()  # Rafraîchit l'écran

		pygame.quit()

	def update(self):
		ControlHandler().handleEvents(pygame)
		if ControlHandler().is_activated('quit'):
			self.running = False

		TimeHandler().update()
		self.player.update()
