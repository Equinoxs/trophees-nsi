from typing import Callable

from src.classes import MapElement, Collider, Interactable, Movable, Vector2, Player, Camera


class MapObject(MapElement, Collider, Interactable, Movable):
	def __init__(self, position: Vector2, image_path: str, z_index: int = 0, interaction: str = ''):
		MapElement.__init__(self, position, image_path, z_index)
		Interactable.__init__(self, interaction)
		Collider.__init__(self, image_path)
		Movable.__init__(self)

	def update(self):
		# Mise à jour de l'élément de la carte
		MapElement.update(self)

		# Vérification si le joueur doit interagir avec l'objet
		if self.must_interact(self.position, Player().focus.get_position()):
			self.interaction(Player())

		width, height = Player().get_focus().get_image().get_size()
		collision = self.collides_with_player(Player().focus.get_position() + Vector2(width // 2, 0.8 * height))
		if isinstance(collision, Vector2):
			object_s_reaction = collision.set_norm(collision.orthogonal_projection(Player().focus.speed_vector * 100 * Camera().get_zoom()).get_norm())
			Player().get_focus().apply_force(object_s_reaction)

		self.move(self.position)