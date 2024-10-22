from typing import Callable

from ...basics import MapObject, Vector2, MapElement, Map
from .....main import control_handler, time_hander


class Player(MapObject):
	def __init__(self, map: Map, position: Vector2, image_path: str, z_index: int = 0):
		MapObject.__init__(self, position, image_path, z_index)
		self.map = map

	def change_map(self, map: Map):
		self.map = map

	def update(self):
		MapObject.update(self)

		if control_handler.is_activated('go_forward'):
			self.speed_vector.set_y(-1)
		elif control_handler.is_activated('go_backward'):
			self.speed_vector.set_y(1)
		else:
			self.speed_vector.set_y(0)

		if control_handler.is_activated('go_left'):
			self.speed_vector.set_x(-1)
		elif control_handler.is_activated('go_right'):
			self.speed_vector.set_x(1)
		else:
			self.speed_vector.set_x(0)

		self.speed_vector.normalize()
		self.move(self.position)
		self.map.update(self)
