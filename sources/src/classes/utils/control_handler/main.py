class ControlHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		self.events = {}
		self.resetEvents()

	def resetEvents(self):
		self.events = {
			'pause': False,
			'quit': False
		}

	def handleEvents(self, pygame):
		self.resetEvents()
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					self.events['quit'] = True
		
	def is_activated(self, event):
		if self.events[event]:
			return True
		else:
			return False
