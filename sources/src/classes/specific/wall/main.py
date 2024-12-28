from src.classes import WallSegment


class Wall:
	def __init__(self, data, map):
		self.segments = []
		self.data = data
		self.boundaries = self.data['boundaries']
		self.initialize_segments(map)

	def initialize_segments(self, map):
		for i in range(1, len(self.boundaries)):
			self.data['segment'] = self.boundaries[i - 1 : i + 1]
			segment = WallSegment(self.data)
			self.segments.append(segment)
			map.add(segment)
