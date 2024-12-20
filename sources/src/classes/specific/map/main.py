from src.classes import DataHandler, GameLoop, SoundMixer, MapElement, MapObject, NPC, GroundSurface, Wall

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

	def add(self, element):
		self.elements.append(element)

	def remove(self, element_to_remove):
		for index, element in enumerate(self.elements):
			if element == element_to_remove:
				return self.elements.pop(index)

	def get_elements(self):
		return self.elements

	def throw_event(self, event):
		for element in self.elements:
			element.catch_event(event)

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

				case 'GroundSurface':
					self.elements.append(GroundSurface(element))

				case 'Wall':
					self.elements.append(Wall(element))

				case _:
					raise NotImplementedError

	def update(self):
		if not GameLoop().is_game_paused():
			for element in self.elements:
				element.update()
			self.sort_elements()

	def which_surface(self, position):
		for i in range(len(self.elements) - 1, 0, -1):
			if isinstance(self.elements[i], GroundSurface) and self.elements[i].point_in_boundaries(position):
				return self.elements[i].get_ground_type()
		return None
