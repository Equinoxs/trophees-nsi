from src.classes import DataHandler, Player, Camera, Furniture, Vector2
from copy import deepcopy


class Table(Furniture):
	def __init__(self, data: dict):
		self.image_type = 'table'
		super().__init__(data)
		self.item_positions = DataHandler().list_transform(data.get('item_positions', []))
		self.items = deepcopy(data.get('items', []))

	def take_item(self, item, index_position: int):
		item.set_index_position(index_position)
		self.items.append(item)

	def release_item(self, item):
		self.items.remove(item)
		item.remove_pickup_marker()
		Player().get_map().add_element_ref(item, Player().get_map().get_index_of(self))

	def get_item_positions(self):
		return self.item_positions

	def get_item_position(self, item_ref):
		return self.item_positions[item_ref.get_index_position()] + self.position

	def get_items(self):
		return self.items

	def item_position_taken(self, index_position):
		for item in self.items:
			if item.get_index_position() == index_position:
				return True
		return False

	def update(self):
		super().update()
		if len(self.items) > 0 and type(self.items[0]) == dict:
			for i in range(len(self.items)):
				if 'index_position' not in self.items[i]:
					self.items[i]['index_position'] = i
				self.items[i] = Player().get_map().add_element(DataHandler().normalize_data(self.items[i]))
				Player().get_map().remove_element(self.items[i])
		for item in self.items:
			item.get_position().copy(self.get_item_position(item))
			item.update()

	def render(self):
		super().render()
		if len(self.items) > 0 and type(self.items[0]) != dict:
			for item in self.items:
				Camera().draw(item.get_image(), self.get_item_position(item) - Vector2(item.get_image().get_width() / 2 / Camera().get_zoom(), item.get_image().get_height() / 2 / Camera().get_zoom()), 'map')

	def get_data(self):
		data = super().get_data()
		data['items'] = []
		for item in self.items:
			if type(item) == dict:
				data['items'].append(item)
			else:
				data['items'].append(item.get_data())
		return data
