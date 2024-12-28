from src.classes import MapObject


class PillarObject(MapObject):
	def __init__(self, data):
		self.object_type = 'pillar'
		super().__init__(data)
