#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import MapObject, Vector2


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
				closest_vector = self.closest_vector_to(map_object.get_position())
				if abs(closest_vector.get_y()) > 1:
					return self.closest_vector_to(map_object.get_position()).get_y() < 0
				else:
					return closest_vector.get_x() > 0
			case 'base':
				return not map_object.goes_on_top_of(self)
			case 'ridge':
				ridge_hitbox = map_object.get_hitbox()
				closest_vector = self.closest_vector_to_segment(ridge_hitbox[0] + map_object.get_position(), ridge_hitbox[1] + map_object.get_position())
				if abs(closest_vector.get_y()) >= 0.9:
					return closest_vector.get_y() < 0
				else:
					return closest_vector.get_x() > 0

	def closest_vector_to_segment(self, vector1: Vector2, vector2: Vector2) -> Vector2:
		# Vérification de la hitbox
		hitbox = self.get_hitbox()
		if len(hitbox) != 2:
			raise ValueError("La hitbox doit contenir exactement deux vecteurs.")

		# Définition des coins de la hitbox
		vector3, vector4 = hitbox
		self_segment = vector4 - vector3

		# Ajustement des extrémités pour éviter des problèmes numériques
		vector3 = (vector3 + self.position + self_segment.normalize())  # 10e-2 → 1e-2 (meilleure lisibilité)
		vector4 = (vector4 + self.position - self_segment.normalize())

		other_segment = vector2 - vector1
		vector1 = (vector1 + other_segment.normalize())
		vector2 = (vector2 - other_segment.normalize())

		# Calcul des vecteurs possibles
		possibilities = [
			-vector1.closest_vector_to_segment(vector3, vector4),
			-vector2.closest_vector_to_segment(vector3, vector4),
			vector3.closest_vector_to_segment(vector1, vector2),
			vector4.closest_vector_to_segment(vector1, vector2)
		]

		# Retourner le plus court vecteur directement
		return min(possibilities, key=lambda v: v.get_squared_norm())