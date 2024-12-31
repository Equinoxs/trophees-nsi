import math

from src.classes import WallSegment


class Wall:
	def __init__(self, data, map):
		self.segments = []
		self.data = data
		self.name = self.data['name']
		self.boundaries: list = self.data['boundaries']
		self.initialize_segments(map)

	def initialize_segments(self, map):
		for i in range(1, len(self.boundaries)):
			self.data['segment'] = self.boundaries[i - 1 : i + 1]

			before_angle = 0
			if i > 1:
				before_angle = (self.boundaries[i] - self.boundaries[i - 1]).signed_angle_to(self.boundaries[i - 1] - self.boundaries[i - 2])
			after_angle = 0
			if i + 1 < len(self.boundaries):
				after_angle = (self.boundaries[i] - self.boundaries[i - 1]).signed_angle_to(self.boundaries[i + 1] - self.boundaries[i])

			self.data['name'] = self.name + '_' + str(i)
			self.data['before_angle'] = before_angle
			self.data['after_angle'] = after_angle
			print('')
			print(before_angle / math.pi * 180)
			print(self.boundaries[i] - self.boundaries[i - 1])
			print(after_angle / math.pi * 180)

			segment = WallSegment(self.data)
			self.segments.append(segment)
			map.add(segment)
