import pygame

from src.classes import Camera, DEBUG


class GameLoop:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, control_handler = None, time_handler = None, save_handler = None, player = None, sound_mixer = None):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			pygame.init()
			self.screen = pygame.display.set_mode((1280, 720), flags=pygame.SCALED, vsync=1)
			self.running = True
			self.time_handler = time_handler
			self.time_handler.set_clock(pygame.time.Clock())
			self.save_handler = save_handler
			self.saved_data = self.save_handler.load_save()
			self.player = player
			self.camera = Camera(self.screen)
			self.control_handler = control_handler
			self.sound_mixer = sound_mixer

			while self.running:
				self.update()
				pygame.display.flip()  # Rafraîchit l'écran

			pygame.quit()

	def get_player(self):
		return self.player

	def get_camera(self):
		return self.camera

	def update(self):
		self.control_handler.handle_events(pygame)
		if self.control_handler.is_activated('quit'):
			self.running = False

		if DEBUG and self.control_handler.is_activated('debug_pause'):
			return

		self.time_handler.update()
		self.player.update()
		self.camera.update()
