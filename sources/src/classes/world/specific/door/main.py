from src.classes import PillarObject, Player


class Door(PillarObject):
	def __init__(self, data):
		self.image_type = 'door'
		super().__init__(data)
		self.must_render = False
		self.belongs_to_building = False

	def you_belong_to_building(self):
		self.belongs_to_building = True

	def update(self):
		if self.is_interaction_available() and self.interaction_marker is not None and not Player().get_map().get_allow_map_change():
			self.set_interaction_available(False)
		elif not self.is_interaction_available() and self.interaction_marker is None and Player().get_map().get_allow_map_change():
			self.set_interaction_available(True)
		super().update()

	def render(self):
		return

	def get_data(self):
		if not self.belongs_to_building:
			return super().get_data()
		return None
