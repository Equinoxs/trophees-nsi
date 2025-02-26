from src.classes import MapElement, Collider, Interactable, Movable, SideEffectsManager


class MapObject(MapElement, Collider, Interactable, Movable, SideEffectsManager):
	def __init__(self, data: dict):
		MapElement.__init__(self, data)
		Interactable.__init__(self, data['interaction'], data.get('mission', None))
		if hasattr(self, 'hitbox'):
			Collider.__init__(self, self.hitbox)
		else:
			Collider.__init__(self, self.image_data.get('hitbox', []))
		Movable.__init__(self)
		SideEffectsManager.__init__(self, data.get('side_effects', []))

	def catch_event(self, event):
		super().catch_event(event)
		Interactable.catch_event(self, event)

	def update(self):
		# Mise à jour de l'élément de la carte
		MapElement.update(self)
		SideEffectsManager.update(self)
		closest_vector = Collider.update(self)
		Interactable.update(self, closest_vector)
		Movable.update(self)

	def __del__(self):
		MapElement.__del__(self)
		Interactable.__del__(self)
