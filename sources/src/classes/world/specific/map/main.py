from src.classes import DataHandler, GameLoop, SoundMixer, Building, Vector2, GroundSurface, Wall, MapObject, InventoryItem, Table, Tree
from src import classes


class Map:
	def __init__(self, map_name: str):
		self.elements = []
		self.walls = []
		self.load_elements_from(map_name)
		self.name = map_name
		self.allow_map_change = True

		# Fusionner les images des GroundSurface pour éviter des blits lors des rendus en temps réel
		for i in range(1, len(self.elements)):
			if not isinstance(self.elements[i], GroundSurface):
				break

			self.elements[0].get_image().blit(
				self.elements[i].get_image(),
				(self.elements[i].get_position() - self.elements[0].get_position()).convert_to_tuple()
			)
			self.elements[i].set_must_render(False)

		SoundMixer().play_music('On the Island - Godmode')

	def get_allow_map_change(self):
		return self.allow_map_change

	def set_allow_map_change(self, new_val: bool):
		self.allow_map_change = new_val

	def sort_once(self):
		began = False
		sorted = True
		for i in range(len(self.elements) - 1):
			if not self.elements[i].get_must_render():
				element = self.elements.pop(i)
				self.elements.insert(0, element)
			if not self.elements[-1].get_must_render():
				element = self.elements.pop(-1)
				self.elements.insert(0, element)
			if not isinstance(self.elements[i], MapObject) or (not began and not self.elements[i].get_must_render()):
				continue
			else:
				began = True
			if self.elements[i].goes_on_top_of(self.elements[i + 1]):
				self.elements[i], self.elements[i + 1] = self.elements[i + 1], self.elements[i]
				sorted = False  # Il y a eu un échange, donc la liste n'est pas encore triée
		return sorted

	def sort_elements(self):
		sorted = False
		while not sorted:
			sorted = self.sort_once()
		self.sort_once()


	def search_by_name(self, object_name: str):
		for element in self.elements:
			if element.get_name() == object_name:
				return element
		return None

	def add(self, element):
		self.elements.append(element)

	def remove_wall(self, wall_name: str):
		for index, wall in enumerate(self.walls):
			if wall.get_name() == wall_name:
				self.walls.pop(index)
		for i in range(len(self.elements) - 1, -1, -1):
			if wall_name == self.elements[i].get_name()[:len(wall_name)]:
				self.elements.pop(i)

	def remove(self, element_to_remove):
		for index, element in enumerate(self.elements):
			if element == element_to_remove:
				return self.elements.pop(index)

	def get_elements(self, walls=False):
		if walls:
			return self.elements + self.walls
		else:
			return self.elements
	def throw_event(self, event):
		for element in self.elements:
			element.catch_event(event)

	def load_elements_from(self, map_name):
		self.name = map_name
		self.elements = []
		self.walls = []
		elements = DataHandler().load_save()['maps'][self.name]['elements']
		for element in elements:
			self.add_element(element)
		self.sort_elements()

	def add_element(self, element_data: dict):
		element = None
		match element_data['type']:
				case 'Wall':
					wall = Wall(element_data, self)
					self.walls.append(wall)  # Ce n'est pas un MapElement

				case "Building":
					element = Building(element_data, self.add)

				case _:
					element_class = getattr(classes, element_data['type'], None)
					if element_class is None:
						raise ValueError('Element type must be a valid class')
					element = element_class(element_data)

		if element is not None:
			self.elements.append(element)
		return element

	def add_element_ref(self, element_ref, index = None):
		if index is None:
			self.elements.append(element_ref)
		else:
			self.elements.insert(index, element_ref)

	def get_index_of(self, element_ref):
		for idx, element in enumerate(self.elements):
			if element == element_ref:
				return idx

	def remove_element(self, element_ref):
		self.elements.remove(element_ref)

	def which_surface(self, position):
		for i in range(len(self.elements) - 1, -1, -1):
			if isinstance(self.elements[i], GroundSurface) and self.elements[i].point_in_boundaries(position):
				return self.elements[i].get_ground_type()
		return None

	def get_name(self):
		return self.name

	def find_closest_item(self, position: Vector2):
		closest_item = None
		closest_table = None
		closest_distance = 100
		for element in self.elements:
			distance = element.get_position().distance_to(position)
			if isinstance(element, InventoryItem) and distance <= closest_distance:
				closest_distance = distance
				closest_item = element
				closest_table = None
			elif isinstance(element, Table):
				for item in element.get_items():
					distance = element.get_item_position(item).distance_to(position)
					if distance <= closest_distance:
						closest_distance = distance
						closest_table = element
						closest_item = item
		return closest_item, closest_table

	def find_closest_item_place(self, position: Vector2):
		closest_distance = 100
		closest_item_place = None
		for element in self.elements:
			if isinstance(element, Table):
				for idx, item_position in enumerate(element.get_item_positions()):
					distance = (item_position + element.get_position()).distance_to(position)
					if distance < closest_distance and not element.item_position_taken(idx):
						closest_distance = distance
						closest_item_place = { 'table': element, 'index_position': idx }
		return closest_item_place

	def update(self):
		if not GameLoop().is_game_paused():
			for element in self.elements:
				element.update()
			self.sort_elements()
