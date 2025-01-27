from src.classes import PillarObject


class Door(PillarObject):
	def __init__(self, data):
		self.image_type = 'door'
		super().__init__(data)

	def render(self):
		return
