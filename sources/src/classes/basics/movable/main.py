from .. import Vector2
from .....main import time_handler

class Movable:
	def __init__(self):
		self.speed_vector = Vector2(0, 0)

	def apply_force(self, force: Vector2):
		if time_handler.is_running():
			self.speed_vector.add(Vector2(
				force.get_x() * time_handler.get_delta_time(),
				force.get_y() * time_handler.get_delta_time()
			))

	def move(self, sprite_position: Vector2):
		sprite_position.add(Vector2(
			self.speed_vector.get_x() * time_handler.get_delta_time(),
			self.speed_vector.get_y() * time_handler.get_delta_time()
		))
