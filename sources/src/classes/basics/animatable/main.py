from src.classes import TimeHandler


class Animatable:
	def __init__(self, animation_scheme: list[float] = []):
		self.running = True
		self.scheme = animation_scheme
		self.dt = 0
		self.index = 0
		self.infinite = True

	def stop(self):
		self.running = False

	def resume(self):
		self.running = True

	def animation_must_update(self):  # Renvoie vrai si le MapElement doit etre animé
		self.dt += TimeHandler().get_delta_time()
		if len(self.scheme) == 0:
			return False  # pas d'animation

		if not self.running:
			return False

		if self.dt < self.scheme[self.index + 1]:
			return False  # trop tôt

		if self.index == len(self.scheme) - 1:
			self.index = 0  # si la dernière image est affiché, on revient au début
			if not self.infinite:
				self.running = False
				return False
		else:
			self.index += 1  # sinon, on passe à la suivante
		return True
