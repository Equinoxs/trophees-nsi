from src.classes import MapElement, Vector2

class Map:
	def __init__(self, image_path: str, width: int, height: int, elements: list):
		self.image_path = image_path
		self.width = width
		self.height = height
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
					))
				case _:
					raise NotImplementedError

		# self.elements = elements  # Une liste de tous les MapElements de la map

	def update(self, player):
		for element in self.elements:
			element.update(player)

	def add(self, element):
		self.elements.append(element)

	def remove(self, element_to_remove):
		for element in self.elements:
			if element == element_to_remove:
				self.elements.pop(element_to_remove)
