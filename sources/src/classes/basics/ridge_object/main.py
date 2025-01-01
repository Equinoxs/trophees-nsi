from src.classes import MapObject


class RidgeObject(MapObject):
	def __init__(self, data):
		self.object_type = 'ridge'
		super().__init__(data)

	def get_object_type(self):
		return self.object_type

	def goes_on_top_of(self, map_object: MapObject):
		object_type = map_object.get_object_type()
		match object_type:
			case 'pillar':
				return self.closest_vector_to(map_object.get_position()).get_y() < 0
			case 'base':
				return self.closest_vector_to(map_object.get_hitbox()[0]).get_y() < 0
			case 'ridge':
				ridge_hitbox = map_object.get_hitbox()
				min_x = min(self.hitbox[0].get_x(), self.hitbox[1].get_x())
				max_x = max(self.hitbox[0].get_x(), self.hitbox[1].get_x())
				if min_x <= ridge_hitbox[0].get_x() <= max_x and min_x <= ridge_hitbox[1].get_x() <= max_x:
					return self.closest_vector_to((ridge_hitbox[0] + ridge_hitbox[1]) * 0.5).get_y() < 0
				else:
					return False
