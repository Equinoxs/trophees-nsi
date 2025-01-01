from src.classes import MapElement, Collider, Interactable, Movable, SideEffectsManager, Player, Camera


class MapObject(MapElement, Collider, Interactable, Movable, SideEffectsManager):
	def __init__(self, data):
		MapElement.__init__(self, data)
		Interactable.__init__(self, data['interaction'])
		if hasattr(self, 'hitbox'):
			Collider.__init__(self, self.hitbox)
		else:
			Collider.__init__(self, self.image_data.get('hitbox', []))
		Movable.__init__(self)
		SideEffectsManager.__init__(self, data['side_effects'])

	def update(self):
		# Mise à jour de l'élément de la carte
		MapElement.update(self)

		closest_vector = self.closest_vector_to(Player().get_focus().get_position())
		self.handle_interaction(closest_vector)

		if self != Player().get_focus() and closest_vector.get_norm() < self.hitbox_action_radius * Camera().get_zoom():
			object_s_reaction = closest_vector.set_norm(closest_vector.orthogonal_projection(Player().get_focus().get_speed_vector() + self.speed_vector).get_norm())
			Player().get_focus().get_speed_vector().add(object_s_reaction)

		self.move(self.position)
		self.apply_side_effects()
