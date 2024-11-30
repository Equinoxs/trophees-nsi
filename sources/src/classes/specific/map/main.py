from src.classes import MapElement, MapObject, Vector2, NPC, SaveHandler
from src.utils import interactions

def get_interaction(interaction_name):
    if interaction_name == '':
        interaction_name = 'default'
    return interactions.get(interaction_name)

def list_transform(list2: list):
	new_list = []
	for el in list2:
		if type(el) == list:
			new_list.append(Vector2(el[0], el[1]))
		elif type(el) == str:
			new_list.append(get_interaction(el))
		else:
			raise ValueError
	return new_list

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
		elements = SaveHandler().load_save()['maps'][map_name]['elements']
		for el in elements:
			match el["type"]:

				case "MapElement":
					self.elements.append(MapElement(
						el["name"],
    					Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"]
					)),
	   
				case "MapObject":
					self.elements.append(MapObject(
						el["name"],
						Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"],
						get_interaction(el["interaction"])
					)),

				case "NPC":
					self.elements.append(NPC(
						el["name"],
						list_transform(el["pattern_timeline"]),
						Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"],
						get_interaction(el["interaction"])
					))

				case _:
					raise NotImplementedError
