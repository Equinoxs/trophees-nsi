from src.classes import MapObject


class BaseObject(MapObject):
	def __init__(self, data):
		self.object_type = 'base'
		super().__init__(data)
