from typing import Callable

from .. import MapElement, Collider, Interactable, Movable, Vector2


class MapObject(MapElement, Collider, Interactable, Movable):
	def __init__(self, position: Vector2, image_path: str, frame: tuple[int, int] = (0, 10_000), z_index: int = 0, interaction: Callable = None, points: list[Vector2] = []):
		MapElement.__init__(self, position, image_path, frame, z_index)
		Interactable.__init__(self, interaction)
		Collider.__init__(self, points)
		Movable.__init__(self)

	def update(self, player):
		MapElement.update(self)

		if self.must_interact():
			self.interaction(self, player)

		collision = self.collides_with_player(player.position)
		if collision.isinstance(Vector2):
			player.speed_vector -= collision.set_norm(collision.orthogonal_projection(player.speed_vector).get_norm())