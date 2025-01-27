from src.classes import GroundSurface, DataHandler


class Interior(GroundSurface):
	def __init__(self, data: dict):
		self.image_type = 'interior'
		data['boundaries'] = []
		super().__init__(data)
		self.boundaries = DataHandler().list_transform(self.image_data.get('boundaries', []))
