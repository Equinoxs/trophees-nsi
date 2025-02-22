from src.classes import Sprite, Animatable, SoundMaker


class MapElement(Sprite, SoundMaker, Animatable):
	def __init__(self, data: dict):
		Sprite.__init__(self, data['position'], data.get('image_path', None))
		SoundMaker.__init__(self, self.position, data.get('authorized_sound_tracks', []))
		Animatable.__init__(self, data.get('image_path', None))
		self.z_index = data.get('z_index', 1)  # Un z_index de 1 s'affichera au-dessus d'un z_index de 0
		self.z_indexes_history = [self.z_index]
		self.name = data['name']

	def get_name(self):
		return self.name

	def get_z_index(self):
		return self.z_index
		
	def set_z_index(self, z_index: int):
		self.z_indexes_history.append(self.z_index)
		self.z_index = z_index

	def set_z_index_prev(self):
		if len(self.z_indexes_history) >= 2:
			self.set_z_index(self.z_indexes_history[-2])

	def catch_event(self, event):
		pass

	def update(self):
		SoundMaker.update(self)
		Animatable.update(self)
		Sprite.update(self)
