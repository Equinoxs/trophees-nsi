from typing import Callable

from src.classes import MapElement, Collider, Interactable, Movable, Vector2, Player


class MapObject(MapElement, Collider, Interactable, Movable):
	def __init__(self, position: Vector2, image_path: str, z_index: int = 0, interaction: Callable = None):
		MapElement.__init__(self, position, image_path, z_index)
		Interactable.__init__(self, interaction)
		Collider.__init__(self, image_path)
		Movable.__init__(self)

	def update(self):
		MapElement.update(self)

		if self.must_interact(self.position, Player().focus.get_position()):
			self.interaction(self)

		collision = self.collides_with_player(Player().focus.get_position())
		if isinstance(collision, Vector2):
			Player().get_focus().apply_force(collision.set_norm(collision.orthogonal_projection(Player().focus.speed_vector).get_norm()))
		self.move(self.position)