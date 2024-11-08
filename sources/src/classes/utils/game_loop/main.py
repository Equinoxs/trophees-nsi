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
				self.saved_data['map']['width'],
				self.saved_data['map']['height'],
				self.saved_data['map']['elements'] # TODO: faire une compréhension de liste pour caster en le type spécifique du MapElement
			),
			# Convertir la position sous forme de list en Vector2
			Vector2(
				self.saved_data['player']['position'][0],
				self.saved_data['player']['position'][1]
    		),
			self.saved_data['player']['image_path'],
			self.saved_data['player']['z_index']
		)

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
