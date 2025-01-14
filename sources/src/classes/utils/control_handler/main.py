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
			self.consumed_events = set()

	def handle_events(self):
		self.mouse_position = pygame.mouse.get_pos()
		self.finish_event('clicked')  # Réinitialiser l'état de clic à chaque frame
		
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					self.events['quit'] = True
				case pygame.KEYDOWN:
					for action in self.keybinds:
						if self.keybinds[action] == event.key:
							if action not in self.consumed_events:
								self.activate_event(action)
				case pygame.KEYUP:
					for action in self.keybinds:
						if self.keybinds[action] == event.key:
							self.finish_event(action)
							self.consumed_events.discard(action)
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

	def finish_event(self, event_name: str):
		self.events[event_name] = False

	def consume_event(self, event_name: str):
		self.consumed_events.add(event_name)
		self.finish_event(event_name)

	def get_key_letter(self, event_name: str):
		if event_name in self.keybinds:
			return pygame.key.name(self.keybinds[event_name])
		else:
			raise KeyError
