import pygame

from src.classes import GameLoop, DEBUG, SCREEN_WIDTH, SCREEN_HEIGHT


class LogHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.log = []
			self.length = 10

	def add(self, *args):
		log = ''
		for idx, arg in enumerate(args):
			log += str(arg)
			if idx != len(args) - 1:
				log += ' '
		if DEBUG:
			print(log)
		self.log.append(log)

	def set_length(self, length):
		self.length = length

	def get_log(self):
		return ['==== Log ===='] + self.log[-self.length:]

	def render(self):
		if not DEBUG:
			return

		pygame.font.init()
		font = pygame.font.Font(pygame.font.get_default_font(), 50)

		# Texte DEBUG
		text_surface = font.render('DEBUG', True, (255, 0, 0))
		text_width, _ = text_surface.get_size()
		GameLoop().get_camera().draw(text_surface, (SCREEN_WIDTH - text_width, 0), 'log_handler')
		font = pygame.font.Font(pygame.font.get_default_font(), 15)

		# Infos Channels
		for idx, text in enumerate(GameLoop().get_sound_mixer().generate_debug_data()):
			GameLoop().get_camera().draw(font.render(text, True, (255, 0, 0)), (0, 15*idx), 'log_handler')

		# Log
		log = LogHandler().get_log()[::-1]
		longest_text_surface = font.render(max(log, key=len), False, (0, 0, 0))
		longest_text_width, _ = longest_text_surface.get_size()
		del longest_text_surface

		bg_surface = pygame.Surface(pygame.Rect(SCREEN_WIDTH - longest_text_width, SCREEN_HEIGHT - len(log)*15, SCREEN_WIDTH, SCREEN_HEIGHT).size, pygame.SRCALPHA)
		bg_surface.fill((0, 0, 0, 192))
		GameLoop().get_camera().draw(bg_surface, (SCREEN_WIDTH - longest_text_width, SCREEN_HEIGHT - len(log)*15), 'log_handler')
		for idx, text in enumerate(log):
			text_surface = font.render(text, True, (0, 255, 0))
			text_width, _ = text_surface.get_size()
			GameLoop().get_camera().draw(text_surface, (SCREEN_WIDTH - longest_text_width, SCREEN_HEIGHT-15*(1+idx)), 'log_handler')