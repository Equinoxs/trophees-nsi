class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y

	def set_all(self, x, y):
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_norm(self):
		return (self.x ** 2 + self.y ** 2) ** (1/2)

	def normalize(self): # règle la norme du vecteur à 1
		norm = self.get_norm()
		if norm != 0:
			self.x /= norm
			self.y /= norm

	def distance_to(self, vector2):
		return ((self.x - vector2.get_x()) ** 2 + (self.y - vector2.get_y()) ** 2) ** (1/2)

	def add(self, vector2):
		self.x += vector2.get_x()
		self.y += vector2.get_y()
