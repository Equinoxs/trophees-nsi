#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import PillarObject, Player, ControlHandler, MenuHandler, Camera


class InventoryItem(PillarObject):
	def __init__(self, data: dict):
		self.image_type = 'item'
		super().__init__(data)
		self.pickup_marker = None
		self.index_position = data.get('index_position', None)

	def get_index_position(self):
		return self.index_position

	def set_index_position(self, index_position):
		self.index_position = index_position

	def remove_pickup_marker(self):
		if self.pickup_marker is not None:
			MenuHandler().remove_marker(self.pickup_marker)
			self.pickup_marker = None

	def update(self):
		super().update()

		distance = Player().get_focus().get_position().distance_to(self.position)
		if distance <= 100 and self.pickup_marker is None and Player().get_focus().get_inventory() is None:
			data = {
				'label': ControlHandler().get_key_letter('pick_drop'),
				'border_radius': 10,
				'position': Player().get_focus().get_position(),
				'width': 'auto',
				'height': 'auto',
				'border_length': 1,
				'border_color': (255,) * 3,
				'text_color': (255,) * 3,
				'color': (0, 0, 0, 200),
				'x_offset': -50
			}
			self.pickup_marker = MenuHandler().add_marker(data)

		elif distance > 100 and self.pickup_marker is not None:
			self.remove_pickup_marker()

	def render(self):
		width, height = self.image.get_size()
		x, y = self.position.convert_to_tuple()
		self.position.set_all(x - width / 2 / Camera().get_zoom(), y - height / 2 / Camera().get_zoom())
		super().render()
		self.position.set_all(x, y)

	def __del__(self):
		super().__del__()
		self.remove_pickup_marker()
