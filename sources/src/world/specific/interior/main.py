#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import GroundSurface, DataHandler


class Interior(GroundSurface):
	def __init__(self, data: dict):
		self.image_type = 'interior'
		data['boundaries'] = []
		super().__init__(data)
		self.boundaries = DataHandler().list_transform(self.image_data.get('boundaries', []))
