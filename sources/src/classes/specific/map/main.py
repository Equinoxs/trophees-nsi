from src.classes import MapElement, MapObject, Vector2, NPC

def list_transform(list):
	new_list = []
	for el in list:
		new_list.append(Vector2(el[0], el[1]))
	return new_list

class Map:

	def __init__(self, elements: list):
		self.elements = []
		for el in elements:
			match el["type"]:
	   
				case "MapElement":
					self.elements.append(MapElement(
						Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"]
					)),
	   
				case "MapObject":
					self.elements.append(MapObject(
						Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"]
					)),

				case "NPC":
					self.elements.append(NPC(
						list_transform(el["pattern"]),
						Vector2(
							el["position"][0], el["position"][1]
						),
						el["image_path"],
						el["z_index"]
					))

				case _:
					raise NotImplementedError
 
	def search_by_name(self, npc_name: str):
		for el in self.elements:
			if isinstance(el, NPC) and el.image_path.split('/')[0] == npc_name:
				return el

	def update(self):
		for element in self.elements:
			element.update()

	def add(self, element):
		self.elements.append(element)

	def remove(self, element_to_remove):
		for element in self.elements:
			if element == element_to_remove:
				self.elements.pop(element_to_remove)

	def get_elements(self):
		return self.elements