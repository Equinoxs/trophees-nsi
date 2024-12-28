from src.classes import GameLoop


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
			self.coeff = 1  # Un coeff de 2 fait écouler le temps 2 fois plus lentement
			self.running = True
			self.chrono_tags = {}

	# Renvoie le temps depuis que le chrono tag a été créé
	# S'il vient d'être créé, on renverra 0
	def add_chrono_tag(self, chrono_tag, reset=False):
		if chrono_tag not in self.chrono_tags or reset:
			self.chrono_tags[chrono_tag] = 0
		return self.chrono_tags[chrono_tag]

	def remove_chrono_tag(self, chrono_tag):
		if chrono_tag in self.chrono_tags:
			del self.chrono_tags[chrono_tag]

	def set_clock(self, pygame_clock):
		self.clock = pygame_clock

	def update(self):
		if self.clock:
			self.dt = self.clock.tick() / 1000 / self.coeff
		if not GameLoop().is_game_paused():
			for key in self.chrono_tags:
				self.chrono_tags[key] += self.dt

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
