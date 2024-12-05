import pygame

from src.classes import DEBUG


class LogHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.log = []
			self.length = 10

	def add(self, *args):
		log = ""
		for idx, arg in enumerate(args):
			log += str(arg)
			if not idx == len(args)-1: log += " "
		if DEBUG:
			print(log)
		self.log.append(log)

	def set_length(self, length):
		self.length = length

	def get_log(self):
		return ['==== Log ===='] + self.log[-self.length:]
  
	def render(self, screen, sound_mixer):
		screen_width, screen_height = screen.get_size()
		pygame.font.init()
		font = pygame.font.Font(pygame.font.get_default_font(), 50)

		# Texte DEBUG
		text_surface = font.render("DEBUG", True, (255, 0, 0))
		text_width, _ = text_surface.get_size()
		screen.blit(text_surface, (screen_width - text_width, 0))
		font = pygame.font.Font(pygame.font.get_default_font(), 15)

		# Infos Channels
		for idx, text in enumerate(sound_mixer.generate_debug_data()):
			screen.blit(font.render(text, True, (255, 0, 0)), (0, 15*idx))

		# Log
		log = LogHandler().get_log()[::-1]
		longest_text_surface = font.render(max(log, key=len), False, (0, 0, 0))
		longest_text_width, _ = longest_text_surface.get_size()
		del longest_text_surface

		bg_surface = pygame.Surface(pygame.Rect(screen_width-longest_text_width, screen_height-len(log)*15, screen_width, screen_height).size, pygame.SRCALPHA)
		bg_surface.fill((0, 0, 0, 192))
		screen.blit(bg_surface, (screen_width-longest_text_width, screen_height-len(log)*15))
		for idx, text in enumerate(log):
			text_surface = font.render(text, True, (0, 255, 0))
			text_width, _ = text_surface.get_size()
			screen.blit(text_surface, (screen_width-longest_text_width, screen_height-15*(1+idx)))