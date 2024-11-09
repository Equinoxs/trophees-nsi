class TimeHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True  # Empêche une nouvelle initialisation
			self.clock = None
			self.dt = 0  # Temps écoulé depuis le dernier rafraîchissement en seconde
			self.coeff = 1  # Un coeff de 2 fait écouler le temps 2 fois plus vite
			self.running = True

	def set_clock(self, pygame_clock):
		self.clock = pygame_clock

	def update(self):
		if self.clock:
			self.dt = self.clock.tick(60) / 1000 / self.coeff

	def set_coeff(self, coeff):
		if coeff > 0:  # S'assurer que le coefficient est positif
			self.coeff = coeff

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True

	def get_delta_time(self):
		return self.dt

	def is_running(self):
		return self.running
