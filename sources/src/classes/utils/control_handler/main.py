class ControlHandler:
	def __init__(self):
		self.resetEvents()
		self.events = {}

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
