import pygame

from src.classes import Vector2, ControlHandler, TimeHandler, SaveHandler, Player, Map


class GameLoop:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		self.running = True
		pygame.init()
		TimeHandler().set_clock(pygame.time.Clock())
		self.screen = pygame.display.set_mode((1280, 720))

		self.saved_data = SaveHandler().load_save()
		self.player = Player(
			Map(
				self.saved_data['map']['image_path'],
				self.saved_data['map']['elements']
			),
			self.saved_data['player']['npc_name']
		)

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
