from src.classes import BaseObject, DataHandler, Door, Vector2


class Building(BaseObject):
	def __init__(self, data, add_element):
		self.image_type = 'building'
		super().__init__(data)
		self.hitbox = DataHandler().list_transform(self.image_data['hitbox'])
		self.hitbox_action_radius = self.image_data.get('hitbox_action_radius', self.hitbox_action_radius)
		if 'door' in self.image_data:
			door_data = self.image_data['door']
			door_data['type'] = 'Door'
			if 'door' not in door_data:
				door_data['name'] = self.name + '_door'
			if not isinstance(door_data['position'], Vector2):
				door_data['position'] = Vector2(door_data['position'][0], door_data['position'][1])
			door_data['position'] += self.position
			add_element(Door(door_data))
