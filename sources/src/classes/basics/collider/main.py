import json
import os

from src.classes import Vector2


class Collider:
	def __init__(self, image_path: str):
		self.image_path = image_path
  
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../assets/images', image_path, image_path + '.json')
		with open(path, 'r') as file:
			data = json.load(file)
		self.hitbox = data['hitbox']

	# représentons le joueur comme un point, si ce point est à moins de 50cm
	# d'un segment d'une hitbox, une collision sera détectée
	def collides_with_player(self, point):
		if len(self.hitbox) == 0:
			return False

		closest_vector = Vector2(1_000, 1_000)
		for i in range(0, len(self.hitbox) - 1):
			# Posons
			OA = self.hitbox[i]
			OB = self.hitbox[i - 1]
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
