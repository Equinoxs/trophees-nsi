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
				closest_vector = self.closest_vector_to(map_object.get_position())
				if abs(closest_vector.get_y()) > 1:
					return closest_vector.get_y() < 0
				else:
					return closest_vector.get_x() > 0
			case 'base':
				closest_vector = self.closest_vector_to_polygon(map_object)
				if abs(closest_vector.get_y()) > 1:
					return closest_vector.get_y() < 0
				else:
					return closest_vector.get_x() > 0
			case 'ridge':
				closest_vector = self.closest_vector_to_polygon(map_object)
				if abs(closest_vector.get_y()) > 1:
					return closest_vector.get_y() < 0
				else:
					return closest_vector.get_x() > 0

	def closest_vector_to_polygon(self, map_object: MapObject):
		if len(self.hitbox) == 0:
			return -map_object.closest_vector_to(self.position)

		possibilities = []
		for i in range(len(self.hitbox)):
			possibility = -map_object.closest_vector_to(self.hitbox[i] + self.position)
			possibilities.append(possibility)

		for i in range(len(map_object.get_hitbox())):
			possibility = self.closest_vector_to(map_object.get_hitbox()[i] + map_object.get_position())
			possibilities.append(possibility)

		possibilities = sorted(possibilities, key=lambda p: p.get_squared_norm())
		return possibilities[0]
