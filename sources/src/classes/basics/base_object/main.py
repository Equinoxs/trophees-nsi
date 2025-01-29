from src.classes import MapObject, Vector2


class BaseObject(MapObject):
	def __init__(self, data):
		self.object_type = 'base'
		super().__init__(data)

	def get_object_type(self):
		return self.object_type

	def goes_on_top_of(self, map_object: MapObject):
		object_type = map_object.get_object_type()
		match object_type:
			case 'pillar':
				return self.closest_vector_to(map_object.get_position()).get_y() < 0
			case 'base':
				# à faire en sorte que ça n'arrive jamais car ce n'est pas joli
				return self.position.y > map_object.get_position().get_y()
			case 'ridge':
				if len(self.hitbox) > 0:
					return map_object.closest_vector_to(self.hitbox[0]).get_y() > 0
				else:
					return map_object.closest_vector_to(self.position).get_y() > 0

