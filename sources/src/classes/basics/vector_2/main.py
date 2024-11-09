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

	def copy(self, position):
		self.x = position.get_x()
		self.y = position.get_y()

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_norm(self):
		return (self.x ** 2 + self.y ** 2) ** (1/2)

	def normalize(self):  # règle la norme du vecteur à 1
		norm = self.get_norm()
		if norm != 0:
			self.x /= norm
			self.y /= norm
   
	def set_norm(self, norm):
		self.normalize()
		self.x *= norm
		self.y *= norm
		return self

	def scalar_product(self, vector_2):
		return self.x * vector_2.get_x() + self.y * vector_2.get_y()

	def distance_to(self, vector2):
		return ((self.x - vector2.get_x()) ** 2 + (self.y - vector2.get_y()) ** 2) ** (1/2)

	def add(self, vector2):
		self.x += vector2.get_x()
		self.y += vector2.get_y()

	def orthogonal_projection(self, vector2):
		t = self.scalar_product(vector2) / self.scalar_product(self)
		orthogonal_projected = t * self
		return orthogonal_projected

	def convert_to_tuple(self):
		return (self.x, self.y)

	def __add__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x + other.get_x(), self.y + other.get_y())
		return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x - other.get_x(), self.y - other.get_y())
		return NotImplemented

	def __mul__(self, scalar):
		if type(scalar) == float or type(scalar) == int:
			return Vector2(scalar * self.x, scalar * self.y)
		return NotImplemented
