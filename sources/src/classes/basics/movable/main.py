from src.classes import Vector2, TimeHandler


class Movable:
	def __init__(self):
		self.speed_vector = Vector2(0, 0)

	def get_speed_vector(self):
		return self.speed_vector

	def apply_force(self, force: Vector2):
		if TimeHandler().is_running():
			self.speed_vector.add(force * TimeHandler().get_delta_time())

	def move(self, sprite_position: Vector2):
		sprite_position.add(Vector2(
			self.speed_vector.get_x() * TimeHandler().get_delta_time(),
			self.speed_vector.get_y() * TimeHandler().get_delta_time()
		))

	def update(self):
		self.move(self.position)
