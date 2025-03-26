#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import BaseObject, DataHandler


class NaturalObject(BaseObject):
	def __init__(self, data: dict):
		if not hasattr(self, 'image_type'):
			self.image_type = 'natural_object'
		super().__init__(data)

		self.hitbox = DataHandler().list_transform(self.image_data.get('hitbox', self.hitbox))
		self.hitbox_action_radius = self.image_data.get('hitbox_action_radius', self.hitbox_action_radius)
  
		width, height = self.image.get_size()
		for i in range(len(self.hitbox)):
			self.hitbox[i].set_x(self.hitbox[i].get_x() * (width / 100))
			self.hitbox[i].set_y(self.hitbox[i].get_y() * (height / 100))

		if 'interaction' in self.image_data and self.interaction is None:
			self.interaction = self.image_data['interaction']
