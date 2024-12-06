from src.classes import MapElement, MapObject, NPC, DataHandler, GameLoop, SoundMixer

class Map:

	def __init__(self, map_name: str):
		self.elements = []
		self.load_elements_from(map_name)
		SoundMixer().play_music('wstheme')

	def sort_elements(self):
		self.elements.sort(key=lambda x: (x.get_z_index(), x.get_position().get_y()))

	def search_by_name(self, npc_name: str):
		for el in self.elements:
			if isinstance(el, NPC) and el.name == npc_name:
				return el
		return None

	def update(self):
		paused = GameLoop().is_game_paused()
		self.sort_elements()
		if not paused:
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
		for element in elements:
			match element['type']:

				case 'MapElement':
					self.elements.append(MapElement(element)),
	   
				case 'MapObject':
					self.elements.append(MapObject(element)),

				case 'NPC':
					self.elements.append(NPC(element))

				case _:
					raise NotImplementedError