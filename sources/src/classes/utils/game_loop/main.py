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
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.running = True
			pygame.init()
			TimeHandler().set_clock(pygame.time.Clock())
			self.screen = pygame.display.set_mode((1280, 720))

			self.saved_data = SaveHandler().load_save()
			self.player = Player(Map(self.saved_data['maps'][self.saved_data["player"]["current_map_name"]]['elements']), self.saved_data['player']['current_npc_name'])

			self.control_handler = ControlHandler() # pour ne pas réinitialiser ControlHandler à chaque tour de boucle

			while self.running:
				self.update()
				pygame.display.flip()  # Rafraîchit l'écran

			pygame.quit()

	def update(self):
		self.control_handler.handleEvents(pygame)
		if self.control_handler.is_activated('quit'):
			self.running = False
			
		TimeHandler().update()
		self.player.update()
