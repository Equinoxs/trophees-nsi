from src.classes import MapElement, MapObject, Vector2, NPC, DataHandler

class Map:

	def __init__(self, map_name: str):
		self.elements = []
		self.load_elements_from(map_name)

	def sort_elements(self):
		self.elements.sort(key=lambda x: (x.get_z_index(), x.get_position().get_y()))
 
	def search_by_name(self, npc_name: str):
		for el in self.elements:
			if isinstance(el, NPC) and el.name == npc_name:
				return el
		return None

	def update(self):
		self.sort_elements()
		for element in self.elements:
			element.update()

	def add(self, element):
		self.elements.append(element)

	def remove(self, element_to_remove):
		for index, element in enumerate(self.elements):
			if element == element_to_remove:
				return self.elements.pop(index)

	def get_elements(self):
		return self.elements

	def load_elements_from(self, map_name):
		self.elements = []
		elements = DataHandler().load_save()['maps'][map_name]['elements']
		for el in elements:
			match el['type']:

				case 'MapElement':
					self.elements.append(MapElement(
						el['name'],
						el['position'],
						el['image_path'],
						el['z_index']
					)),
	   
				case 'MapObject':
					self.elements.append(MapObject(
						el['name'],
						el['position'],
						el['image_path'],
						el['z_index'],
						el['interaction'],
						el['side_effects']
					)),

				case 'NPC':
					self.elements.append(NPC(
						el['name'],
						el['pattern_timeline'],
						el['position'],
						el['image_path'],
						el['z_index'],
						el['interaction'],
						el['side_effects']
					))

				case _:
					raise NotImplementedError
