from src.classes import MapObject


class PillarObject(MapObject):
	def __init__(self, data):
		self.object_type = 'pillar'
		super().__init__(data)

	def get_object_type(self):
		return self.object_type

	def goes_on_top_of(self, map_object: MapObject):
		object_type = map_object.get_object_type()
		match object_type:
			case 'pillar':
				delta = map_object.get_position().get_y() - self.position.y
				if delta != 0:
					return delta < 0
				else:
					return map_object.get_position().get_x() - self.position.get_x() > 0
			case 'base':
				return not map_object.goes_on_top_of(self)
			case 'ridge':
				return not map_object.goes_on_top_of(self)
