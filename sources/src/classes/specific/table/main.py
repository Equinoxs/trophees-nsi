from src.classes import Furniture


class Table(Furniture):
	def __init__(self, data: dict):
		self.image_type = 'table'
		super().__init__(data)
