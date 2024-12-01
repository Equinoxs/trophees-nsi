import pygame.font

from src.classes import Player, SoundMixer, DEBUG, LogHandler

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
		self.camera.center = (self.zoom * self.player_pos.get_x(), self.zoom * (self.player_pos.get_y() - height / 2))
		# Remplir l'écran de noir
		self.screen.fill((0,) * 3)
		for element in elements:
			element.render()
		if DEBUG:
			screen_width, screen_height = self.screen.get_size()

			pygame.font.init()
			font = pygame.font.Font(pygame.font.get_default_font(), 50)
			# Texte DEBUG
			text_surface = font.render("DEBUG", True, (255, 0, 0))
			text_width, _ = text_surface.get_size()
			self.screen.blit(text_surface, (screen_width - text_width, 0))

			font = pygame.font.Font(pygame.font.get_default_font(), 15)

			# Infos Channels
			for idx, text in enumerate(SoundMixer().generate_debug_data()):
				self.screen.blit(font.render(text, True, (255, 0, 0)), (0, 15*idx))

			# Log
			log = LogHandler().get_log()[::-1]
			longest_text_surface = font.render(max(log, key=len), False, (0, 0, 0))
			longest_text_width, _ = longest_text_surface.get_size()
			del longest_text_surface
			bg_surface = pygame.Surface(pygame.Rect(screen_width-longest_text_width, screen_height-len(log)*15, screen_width, screen_height).size, pygame.SRCALPHA)
			bg_surface.fill((0, 0, 0, 192))
			self.screen.blit(bg_surface, (screen_width-longest_text_width, screen_height-len(log)*15))

			for idx, text in enumerate(log):
				text_surface = font.render(text, True, (0, 255, 0))
				text_width, _ = text_surface.get_size()
				self.screen.blit(text_surface, (screen_width-text_width, screen_height-15*(1+idx)))
