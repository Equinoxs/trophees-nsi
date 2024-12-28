from src.classes import MapObject


class RidgeObject(MapObject):
	def __init__(self, data):
		self.object_type = 'ridge'
		super().__init__(data)
