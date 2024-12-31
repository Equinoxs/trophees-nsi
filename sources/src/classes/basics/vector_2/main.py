import math


class Vector2:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y

	def set_all(self, x, y):
		self.x = x
		self.y = y

	def copy(self, position = None):
		if position is not None:
			self.x = position.get_x()
			self.y = position.get_y()
			return self
		else:
			return Vector2(self.x, self.y)

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
		return self
   
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
		return self

	def orthogonal_projection(self, vector2):
		self_dot_self = self.scalar_product(self)
		if self_dot_self != 0:
			t = self.scalar_product(vector2) / self.scalar_product(self)
			orthogonal_projected = self * t
			return orthogonal_projected  # projeté orthogonal de vector2 sur self
		else:
			return Vector2(0, 0)

	def convert_to_tuple(self):
		return (self.x, self.y)

	def angle_to(self, vector):
		norm_self = self.get_norm()
		norm_vector = vector.get_norm()

		if norm_self == 0 or norm_vector == 0:
			return 0
		
		scalar_product = self.scalar_product(vector)
		cos_theta = scalar_product / (norm_self * norm_vector)
		cos_theta = max(-1, min(1, cos_theta))
		
		return math.acos(cos_theta)

	def angle(self):
		norm = self.get_norm()
		if norm == 0:
			return 0
		angle = math.acos(self.x / norm)
		if math.sin(self.y / norm) < 0:
			angle *= -1
		return angle

	def signed_angle_to(self, vector):
		signed_angle = vector.angle() - self.angle()

		# Pour obtenir la mesure principale de l'angle
		if signed_angle > math.pi:
			signed_angle -= 2 * math.pi
		elif signed_angle < -math.pi:
			signed_angle += 2 * math.pi

		return signed_angle

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

	def __repr__(self):
		return f"<Vector2({self.x}, {self.y})>"