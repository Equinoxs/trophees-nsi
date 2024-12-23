from src.classes import Sprite, Animatable, SoundMaker, Camera


class MapElement(Sprite, SoundMaker, Animatable):
	def __init__(self, data):
		SoundMaker.__init__(self, data['position'], data['authorized_sound_tracks'])
		Sprite.__init__(self, data['position'], data['image_path'])
		Animatable.__init__(self, data['image_path'])
		self.z_index = data['z_index']  # Un z_index de 1 s'affichera au-dessus d'un z_index de 0
		self.z_indexes_historic = [self.z_index]
		self.name = data['name']

	def get_name(self):
		return self.name

	def get_z_index(self):
		return self.z_index
		
	def set_z_index(self, z_index: int):
		self.z_indexes_historic.append(self.z_index)
		self.z_index = z_index

	def set_z_index_prev(self):
		if len(self.z_indexes_historic) >= 2:
			self.set_z_index(self.z_indexes_historic[-2])

	def catch_event(self, event):
		pass

	def update(self):
		self.update_index_animation()
		self.go_to_frame(self.frame_index, self.animation_name)

	def render(self):
		screen_width = Camera().get_frame().x
		screen_height = Camera().get_frame().y
		camera_x = Camera().get_camera().x
		camera_y = Camera().get_camera().y
		width, height = self.image.get_size()

		if self.position.x + width < camera_x and self.position.x > camera_x + screen_width:
			if self.position.y + height < camera_y and self.position.y > camera_y + screen_height:
				return

		Camera().get_screen().blit(
			self.image,
			(
				Camera().get_zoom() * (self.position.x - camera_x),
				Camera().get_zoom() * (self.position.y - camera_y)
			)
		)
