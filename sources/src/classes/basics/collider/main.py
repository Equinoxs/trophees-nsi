from .. import Vector2


class Collider:
	def __init__(self, points: list[Vector2] = []):
		self.points = points  # La hitbox sous forme d'un polygone
		# exemple: un rectangle serait [(0, 0), (1, 0), (1, 1), (0, 1)]
		# Le premier point est toujours à l'origine, pour simplifier les calculs

	# représentons le joueur comme un point, si ce point est à moins de 50cm
	# d'un segment d'une hitbox, une collision sera détectée
	def collides_with_player(self, point):
		if len(self.points) == 0:
			return False

		closest_vector = None
		for i in range(0, len(self.points) - 1):
			# Posons
			OA = self.points[i]
			OB = self.points[i - 1]
			OP = point
			PA = OA - OP
			AB = OB - OA  # D'après la relation de Chasles
			if PA.get_norm() > 20:
				return False

			# Calculons le projeté orthogonal de PA sur AB
			orthogonal_projected = AB.orthogonal_projection(PA) + OP
			t = orthogonal_projected.get_norm() / AB.get_norm()
			if t <= 0:
				if PA.get_norm() < closest_vector.get_norm():
					closest_vector = PA
			if t >= 1:
				PB = PA + AB
				if PB.get_norm() < closest_vector.get_norm():
					closest_vector = PB

			orthogonal_vector = OP - orthogonal_projected
			if orthogonal_vector.get_norm() < closest_vector.get_norm():
				closest_vector = orthogonal_vector

		if closest_vector.get_norm() < 0.5:
			return closest_vector.normalize()
		else:
			return False
