from src.classes import DataHandler
class ControlHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.events = {
				'pause': False,
				'quit': False,
				'interacted': False,
				'go_forward': False,
				'go_backward': False,
				'go_right': False,
				'go_left': False,
				'sprint': False,
				'debug_pause': False
			}
			save = DataHandler().load_save()
			self.keybinds = save["keybinds"]

	def handle_events(self, pygame):
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					self.events['quit'] = True
				case pygame.KEYDOWN | pygame.KEYUP:
					for action in self.keybinds:
						if self.keybinds[action] == event.key:
							self.events[action] = True if event.type == pygame.KEYDOWN else False
							break


	def is_activated(self, event):
		if self.events[event]:
			return True
		else:
			return False

	def finish_event(self, event):
		self.events[event] = False