import pygame.font

from src.classes import Player, DEBUG, LogHandler, TimeHandler, SoundMixer


class Camera:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, screen = None):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.screen = screen
			self.frame = self.screen.get_rect()
			self.camera = self.frame.copy()
			self.player_pos = Player().get_focus().get_position()
			self.zoom = 1
			elements = Player().get_map().get_elements()
			for element in elements:
				element.set_magnification(element.get_magnification() * self.zoom)

	def get_zoom(self):
		return self.zoom

	def get_screen(self):
		return self.screen

	def get_camera(self):
		return self.camera

	def update(self):
		elements = Player().get_map().get_elements()
		width, height = Player().get_focus().get_image().get_size()
		screen_width, screen_height = self.screen.get_size()

		self.camera.center = (self.zoom * self.player_pos.get_x(), self.zoom * (self.player_pos.get_y() - height / 2))
		# Remplir l'écran de noir
		self.screen.fill((0,) * 3)
		for element in elements:
			element.render()
		if not TimeHandler().is_running():
			fg_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
			fg_surface.fill((0, 0, 0, 192))
			self.screen.blit(fg_surface, (0, 0, screen_width, screen_height))

		if DEBUG:
			LogHandler().render(self.screen, SoundMixer())
