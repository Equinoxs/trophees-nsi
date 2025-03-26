#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import BaseObject, DataHandler, Door, Vector2


class Building(BaseObject):
	def __init__(self, data: dict, add_element):
		self.image_type = 'building'
		super().__init__(data)

		self.hitbox = DataHandler().list_transform(self.image_data['hitbox'])
		self.hitbox_action_radius = self.image_data.get('hitbox_action_radius', self.hitbox_action_radius)
		self.required_level = data['required_level']

		width, height = self.image.get_size()
		for i in range(len(self.hitbox)):
			self.hitbox[i].set_x(self.hitbox[i].get_x() * (width / 100))
			self.hitbox[i].set_y(self.hitbox[i].get_y() * (height / 100))

		if 'door' in self.image_data:
			door_data = self.image_data['door'].copy()
			door_data['type'] = 'Door'
			door_data['required_level'] = self.required_level

			if 'door' not in door_data:
				door_data['name'] = self.name + '_door'
			if not isinstance(door_data['position'], Vector2):
				door_data['position'] = Vector2(door_data['position'][0], door_data['position'][1])
			door_data['position'].set_x(door_data['position'].get_x() * (width / 100))
			door_data['position'].set_y(door_data['position'].get_y() * (height / 100))

			door_data['position'] += self.position
			door = Door(door_data)
			door.you_belong_to_building()
			add_element(Door(door_data))

	def get_data(self):
		data = super().get_data()
		data['required_level'] = self.required_level
		return data
