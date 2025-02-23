from src.classes import PillarObject


class Door(PillarObject):
	def __init__(self, data):
		self.image_type = 'door'
		super().__init__(data)
		self.must_render = False

	def render(self):
		return
