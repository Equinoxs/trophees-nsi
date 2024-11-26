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

		# Vérification des collisions
		width, height = Player().get_focus().get_image().get_size()
		closest_vector = self.closest_vector_to(Player().focus.get_position() + Vector2(width // 2, height), self.position)
  
		if closest_vector.get_norm() < 10 * Camera().get_zoom():

			object_s_reaction = closest_vector.set_norm(closest_vector.orthogonal_projection(Player().focus.speed_vector * 100 * Camera().get_zoom()).get_norm())
			Player().get_focus().apply_force(object_s_reaction)

		self.handle_interaction(closest_vector)

		self.move(self.position)