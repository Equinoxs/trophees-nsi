class TimeHandler:
	def __init__(self):
		self.clock = None
		self.dt = 0 # temps écoulé depuis le dernier rafraichissement en seconde
		self.coeff = 1 # un coeff égal à 2 va faire écouler le temps 2 fois plus vite
		self.running = True

	def set_clock(self, pygame_clock):
		self.clock = pygame_clock

	def update(self):
		self.dt = self.clock.tick(60) / 1000 / self.coeff
  
	def set_coeff(self, coeff):
		self.coeff = coeff

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True
  
	def get_delta_time(self):
		return self.dt

	def is_running(self):
		return self.running
