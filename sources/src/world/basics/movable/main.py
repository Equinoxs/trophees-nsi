#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import Vector2, TimeHandler


class Movable:
	def __init__(self):
		self.speed_vector = Vector2(0, 0)
		self.has_moved = True

	def get_has_moved(self):
		return self.has_moved

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
		if self.speed_vector.get_squared_norm() == 0:
			self.has_moved = False
		else:
			self.move(self.position)
			self.has_moved = True
