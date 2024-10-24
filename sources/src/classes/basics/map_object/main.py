from typing import Callable

from src.classes import MapElement, Collider, Interactable, Movable, Vector2


class MapObject(MapElement, Collider, Interactable, Movable):
	def __init__(self, position: Vector2, image_path: str, z_index: int = 0, interaction: Callable = None):
		MapElement.__init__(self, position, image_path, z_index)
		Interactable.__init__(self, interaction)
		Collider.__init__(self, image_path)
		Movable.__init__(self)

	def update(self, player):
		MapElement.update(self, player)

		if self.must_interact(self.position, player.get_position()):
			self.interaction(self, player)

		collision = self.collides_with_player(player.position)
		if isinstance(collision, Vector2):
			player.speed_vector -= collision.set_norm(collision.orthogonal_projection(player.speed_vector).get_norm())