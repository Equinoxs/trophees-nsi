from src.classes import MapObject


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
				return self.position.y > map_object.get_position().get_y()
			case 'base':
				return self.position.y > map_object.get_position().get_y()
			case 'ridge':
				return map_object.closest_vector_to(self.hitbox[0]).get_y() > 0
