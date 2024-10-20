class TimeHandler:
	def __init__(self):
		self.clock = 0
		self.dt = 0
		self.coeff = 1
		self.running = True

	def set_clock(self, pygame_clock):
		self.clock = pygame_clock

	def update(self):
		self.dt = self.clock.tick(60) / 100 / self.coeff
  
	def set_coeff(self, coeff):
		self.coeff = coeff

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True
