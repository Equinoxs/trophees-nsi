class Map:
	def __init__(self):
		self.elements = []  # Une liste de tous les MapElements de la map

	def update(self, player):
		for element in self.elements:
			element.update(player)

	def add(self, element):
		self.elements.append(element)

	def remove(self, element_to_remove):
		for element in self.elements:
			if element == element_to_remove:
				self.elements.pop(element_to_remove)
