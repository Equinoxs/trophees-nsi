from src.classes import Vector2, DataHandler, Player


class Collider:
	def __init__(self, hitbox: list[list[int]]):
		if hasattr(self, 'boundaries'):
			self.hitbox = self.boundaries
		else:
			self.hitbox = hitbox

	# Collision entre un point et une hitbox segmentée
	def closest_vector_to(self, position: Vector2):
		if len(self.hitbox) == 0 or self == Player().get_focus():
			return Vector2(10, 10)  # Pas de hitbox, pas de collision

		closest_distance = float('inf')
		closest_vector = None
		point = Player().get_focus().get_position()

		for i in range(len(self.hitbox)):
			# Points du segment
			A = DataHandler().list_to_vector2(self.hitbox[i]) + position
			B = DataHandler().list_to_vector2(self.hitbox[i - 1]) + position
			AB = B - A
			AP = point - A

			# Longueur du segment AB
			AB_norm = AB.get_norm()
			if AB_norm == 0:  # Si les deux points sont confondus, ignorer le segment
				continue

			# Projection de AP sur AB
			t = AP.scalar_product(AB) / (AB_norm ** 2)  # t = ratio scalaire de la projection
			if t < 0:  # Projection avant A
				projection = A
			elif t > 1:  # Projection après B
				projection = B
			else:  # Projection sur le segment
				projection = A + AB * t

			# Distance entre le point et le segment
			distance_vector = point - projection
			distance = distance_vector.get_norm()

			if distance < closest_distance:
				closest_distance = distance
				closest_vector = distance_vector

		# Si la hitbox est un seul point (pas de segment)
		if len(self.hitbox) == 1:
			point_in_hitbox = DataHandler().list_to_vector2(self.hitbox[0])
			distance_vector = point - (point_in_hitbox + position)
			distance = distance_vector.get_norm()
			if distance < closest_distance:
				closest_distance = distance
				closest_vector = distance_vector

		if closest_vector is None:
			return Vector2(10, 10)
		else:
			return closest_vector
