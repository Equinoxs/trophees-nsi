from src.classes import MapObject, Vector2


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
				if len(map_object.get_hitbox()) > 0:
					return self.closest_vector_to(map_object.get_hitbox()[0]).get_y() < 0
				else:
					return map_object.get_position().get_y() - self.position.get_y() < 0
			case 'ridge':
				ridge_hitbox = map_object.get_hitbox()
				if len(ridge_hitbox) == 0:
					return map_object.get_position().get_y() - self.position.get_y() < 0
				closest_vector = self.closest_vector_to_segment(ridge_hitbox[0] + map_object.get_position(), ridge_hitbox[1] + map_object.get_position())
				if closest_vector.get_y() != 0:
					return closest_vector.get_y() < 0
				else:
					return closest_vector.get_x() < 0

	def closest_vector_to_segment(self, vector1: Vector2, vector2: Vector2) -> Vector2:
		# 4 possibilités pour ce vecteur. Une pour chaque coin, car le vecteur recherché
		# part ou arrive depuis ou vers une des quatre extrémités : on choisira le plus court
		vector3, vector4 = tuple(self.get_hitbox())
		self_segment = vector4 - vector3
		vector3 += self.position
		vector4 += self.position
		vector3 += self_segment.copy().normalize()
		vector4 -= self_segment.copy().normalize()

		other_segment = vector2 - vector1
		vector1 += other_segment.copy().normalize()
		vector2 -= other_segment.copy().normalize()

		possibilities = []

		possibilities.append(-vector1.closest_vector_to_segment(vector3, vector4))
		possibilities.append(-vector2.closest_vector_to_segment(vector3, vector4))
		possibilities.append(vector3.closest_vector_to_segment(vector1, vector2))
		possibilities.append(vector4.closest_vector_to_segment(vector1, vector2))

		possibilities.sort(key=lambda v: v.get_squared_norm())
		return possibilities[0]