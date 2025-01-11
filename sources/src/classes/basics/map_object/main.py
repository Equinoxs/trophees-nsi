from src.classes import MapElement, Collider, Interactable, Movable, SideEffectsManager


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
		SideEffectsManager.update(self)
		closest_vector = Collider.update(self)
		Interactable.update(self, closest_vector)
		Movable.update(self)
