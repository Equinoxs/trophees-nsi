import pygame

from src.classes import DataHandler


class ControlHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			save = DataHandler().load_save()
			self.events = { 'quit': False }
			self.keybinds = save['keybinds']
			for action in self.keybinds:
				self.events[action] = False
			self.mouse_position = None

	def handle_events(self):
		self.mouse_position = pygame.mouse.get_pos()
		self.finish_event('clicked')
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					self.events['quit'] = True
				case pygame.KEYDOWN | pygame.KEYUP:
					for action in self.keybinds:
						if self.keybinds[action] == event.key:
							if event.type == pygame.KEYDOWN:
								self.activate_event(action)
							else:
								self.finish_event(action)
				case pygame.MOUSEBUTTONDOWN:
					self.activate_event('clicked')
					


	def is_activated(self, event: str):
		if self.events[event] and event in self.events:
			return True
		else:
			return False

	def is_clicked(self, button):
		if self.is_activated('clicked') and button.get_rect().collidepoint(self.mouse_position):
			return True
		else:
			return False

	def activate_event(self, event: str):
		self.events[event] = True

	def finish_event(self, event: str):
		self.events[event] = False