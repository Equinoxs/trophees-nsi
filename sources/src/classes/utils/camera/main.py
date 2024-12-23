import pygame

from src.classes import Player, MenuHandler, LogHandler, SoundMixer, GameLoop


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

	def get_frame(self):
		return self.frame

	def get_camera(self):
		return self.camera

	def update(self):
		_, height = Player().get_focus().get_image().get_size()
		self.camera.center = (self.zoom * self.player_pos.get_x(), self.zoom * (self.player_pos.get_y() - height / 2))
		self.screen.fill((0,) * 3)  # Couleur de fond = noir

		for element in Player().get_map().get_elements():
			element.render()
		LogHandler().render(self.screen, SoundMixer())
		if GameLoop().is_game_paused():
			overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
			overlay.fill((0, 0, 0, 100))
			self.screen.blit(overlay, (0, 0))
		MenuHandler().render(self.screen)
