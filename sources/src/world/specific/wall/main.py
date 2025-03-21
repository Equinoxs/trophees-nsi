from copy import deepcopy

from src import WallSegment, Vector2


class Wall:
	def __init__(self, data, map):
		self.segments = []
		self.data = data
		self.original_data = deepcopy(data)
		self.name = self.data['name']
		self.boundaries: list = self.data['boundaries']
		self.initialize_segments(map)

	def get_name(self):
		return self.name

	def initialize_segments(self, map):
		i = 0
		prev_segment = []
		while i + 1 < len(self.boundaries):
			segment = []
			segment.append(self.boundaries[i])
			i += 1
			while not isinstance(self.boundaries[i], Vector2):
				segment.append(self.boundaries[i])
				i += 1
			segment.append(self.boundaries[i])

			self.data['segment'] = segment

			before_angle = 0
			if len(prev_segment) > 0:
				before_angle = (segment[-1] - segment[0]).signed_angle_to(prev_segment[-1] - prev_segment[0])
			after_angle = 0
			if i + 1 < len(self.boundaries):
				j = i
				while not isinstance(self.boundaries[j], Vector2):
					j += 1
				after_angle = (segment[-1] - segment[0]).signed_angle_to(self.boundaries[j] - segment[-1])

			self.data['before_angle'] = before_angle
			self.data['after_angle'] = after_angle

			self.data['name'] = self.name + '_' + str(i)

			prev_segment = segment[:]
			wall_segment = WallSegment(self.data)
			self.segments.append(wall_segment)
			map.add(wall_segment)

	def get_data(self):
		if 'position' in self.original_data:
			del self.original_data['position']
		return self.original_data
