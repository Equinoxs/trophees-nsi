from src.classes import Vector2, DataHandler, Player, Camera


class Collider:
	def __init__(self, hitbox: list[list[int]]):
		self.hitbox = hitbox
		if not hasattr(self, 'hitbox_closed'):
			self.hitbox_closed = True
		if not hasattr(self, 'hitbox_action_radius'):
			self.hitbox_action_radius = 5

	def get_hitbox(self):
		return self.hitbox

	def get_hitbox_action_radius(self):
		return self.hitbox_action_radius

	# Collision entre un point et une hitbox segmentée
	def closest_vector_to(self, point: Vector2):
		closest_squared_distance = float('inf')
		closest_vector = Vector2()

		if self.hitbox_closed:
			iterators = range(len(self.hitbox))
		else:
			iterators = range(1, len(self.hitbox))

		if len(self.hitbox) == 0:
			return point - self.position

		if len(self.hitbox) == 1:
			return point - (DataHandler().list_to_vector2(self.hitbox[0]) + self.position)

		for i in iterators:
			A = DataHandler().list_to_vector2(self.hitbox[i]) + self.position
			B = DataHandler().list_to_vector2(self.hitbox[i - 1]) + self.position
			possible_closest_vector = -point.closest_vector_to_segment(A, B)

			possible_closest_squared_distance = possible_closest_vector.get_squared_norm()
			if possible_closest_squared_distance < closest_squared_distance:
				closest_squared_distance = possible_closest_squared_distance
				closest_vector = possible_closest_vector

		return closest_vector

	def update(self) -> Vector2:
		closest_vector = self.closest_vector_to(Player().get_focus().get_position())

		if self.rendered and self != Player().get_focus() and closest_vector.get_norm() < self.hitbox_action_radius * Camera().get_zoom():
			object_s_reaction = closest_vector.copy().set_norm(closest_vector.orthogonal_projection(Player().get_focus().get_speed_vector() + self.speed_vector).get_norm())
			Player().get_focus().get_speed_vector().add(object_s_reaction)
		return closest_vector
