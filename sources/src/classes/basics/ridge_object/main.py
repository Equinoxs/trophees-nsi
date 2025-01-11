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
				return self.closest_vector_to(map_object.get_hitbox()[0]).get_y() < 0
			case 'ridge':
				ridge_hitbox = map_object.get_hitbox()
				segments_distance, segments_dx, segments_dy = self.segments_distance_squared(self.hitbox[0], self.hitbox[1],
																		  ridge_hitbox[0], ridge_hitbox[1], True)
				if segments_distance == 0:
					print("MapObject's HitBox (" + map_object.get_name() + ")", map_object.get_hitbox(), "My HitBox (" + self.name + ")", self.hitbox)
				return segments_dy < 0
				min_x = min(self.hitbox[0].get_x(), self.hitbox[1].get_x())
				max_x = max(self.hitbox[0].get_x(), self.hitbox[1].get_x())
				if min_x <= ridge_hitbox[0].get_x() <= max_x and min_x <= ridge_hitbox[1].get_x() <= max_x:
					return self.closest_vector_to((ridge_hitbox[0] + ridge_hitbox[1]) * 0.5).get_y() < 0
				else:
					return False

	def segments_distance_squared(self, p1: Vector2, q1: Vector2, p2: Vector2, q2: Vector2, return_xy: bool = False):
		# https://paulbourke.net/geometry/pointlineplane/
		# https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments
		if self.segments_intersect(p1, q1, p2, q2):
			if not return_xy:
				return 0
			else:
				return (0, 0, 0)
		# par déf, la distance est toujours positive et f:x->x^2 est strictement croissante sur R+
		# donc on peut comparer les carrés des distances
		distances = [self.point_segment_distance_squared(p1, p2, q2, True, True), self.point_segment_distance_squared(q1, p2, q2, True, True),
					 self.point_segment_distance_squared(p2, p1, q1, True, False), self.point_segment_distance_squared(q2, p1, q1, True, False)]
		# print([x for x in distances])
		if not return_xy:
			return min(distances)
		else:
			min_distance = distances[0]
			for d in distances[1:]:
				if d[0] < min_distance[0]:
					min_distance = d
			return min_distance

	def orientation(self, p: Vector2, q: Vector2, r: Vector2):
		# 0 : colinéaires ; 1 : sens indirect ; 2 : sens direct
		val = (float(p.get_x() - p.get_y()) * (r.get_x() - q.get_x())) - (
					float(q.get_x() - p.get_x()) * (r.get_y() - q.get_y()))
		if val > 0:
			return 1
		elif val < 0:
			return 2
		else:
			return 0

	def belongs_to_segment(self, p: Vector2, q: Vector2, r: Vector2) -> bool:
		# renvoie True si q appartient à [pr]
		return max(p.get_x(), r.get_x()) >= q.get_x() >= min(p.get_x(), r.get_x()) and max(p.get_y(),
																						   r.get_y()) >= q.get_y() >= min(
			p.get_y(), r.get_y())

	def segments_intersect(self, p1: Vector2, q1: Vector2, p2: Vector2, q2: Vector2) -> bool:
		o1 = self.orientation(p1, q1, p2)
		o2 = self.orientation(p1, q1, q2)
		o3 = self.orientation(p2, q2, p1)
		o4 = self.orientation(p2, q2, q1)

		if o1 != o2 and o3 != o4:
			return True

		# p1, q1, p2 colinéaires et p2 sur [p1q1]
		if o1 == 0 and self.belongs_to_segment(p1, p2, q1):
			return True

		# p1, q1, q2 colinéaires et q2 sur [p1q1]
		if o2 == 0 and self.belongs_to_segment(p1, q2, q1):
			return True

		# p2, q2, p1 colinéaires et p1 sur [p2q2]
		if o3 == 0 and self.belongs_to_segment(p2, p1, q2):
			return True

		# p2, q2, q1 colinéaires et q1 sur [p2q2]
		if o4 == 0 and self.belongs_to_segment(p2, q1, q2):
			return True

		return False

	def point_segment_distance_squared(self, pp: Vector2, p: Vector2, q: Vector2, return_xy: bool = False, opposite: bool = False):
		# pp : point, [pq] : segment
		segment_dx = q.get_x() - p.get_x()
		segment_dy = q.get_y() - p.get_y()
		norm = segment_dx**2 + segment_dy**2
		# print(segment_dx, segment_dy)
		u = ((pp.get_x() - p.get_x()) * segment_dx + (pp.get_y() - p.get_y()) * segment_dy) / norm

		if u < 0:
			# point en dehors de [pq]
			dx = pp.get_x() - p.get_x()
			dy = pp.get_y() - p.get_y()
		elif u > 1:
			dx = pp.get_x() - q.get_x()
			dy = pp.get_y() - q.get_y()
		else:
			dx = pp.get_x() - (p.get_x() + u * segment_dx)
			dy = pp.get_y() - (p.get_y() + u * segment_dy)

		if opposite:
			dx = -dx
			dy = -dy

		if not return_xy:
			return dx**2 + dy**2
		else:
			return (dx**2 + dy**2, dx, dy)
