from src.classes import Sprite, Animatable, Vector2, SoundMaker, Camera


class MapElement(Sprite, SoundMaker, Animatable):
	def __init__(self, data):
		SoundMaker.__init__(self, data['position'], data['authorized_sound_tracks'])
		Sprite.__init__(self, data['position'], data['image_path'])
		Animatable.__init__(self, data['image_path'])
		self.z_index = data['z_index']  # Un z_index de 1 s'affichera au-dessus d'un z_index de 0
		self.name = data['name']

	def get_z_index(self):
		return self.z_index
		
	def set_z_index(self, z_index: int):
		self.z_index = z_index
		
	def update(self):
		self.update_index_animation()
		self.go_to_frame(self.frame_index, self.animation_name)
		
	def render(self):
		Camera().get_screen().blit(
			self.image,
			(
				Camera().get_zoom() * (self.position.x - Camera().get_camera().x),
				Camera().get_zoom() * (self.position.y - Camera().get_camera().y)
			)
		)