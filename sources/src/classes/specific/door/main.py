from src.classes import PillarObject


class Door(PillarObject):
	def __init__(self, data):
		self.image_type = 'door'
		super().__init__(data)
		self.must_render = False
		self.belongs_to_building = False

	def you_belong_to_building(self):
		self.belongs_to_building = True

	def render(self):
		return

	def get_data(self):
		if not self.belongs_to_building:
			return super().get_data()
		return None
