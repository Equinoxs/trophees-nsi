from src.classes import Sprite, Animatable, Vector2, SoundMaker


class MapElement(Sprite, SoundMaker, Animatable):
	def __init__(self, position: Vector2, image_path: str, z_index: int = 0):
		SoundMaker.__init__(self, position)
		Sprite.__init__(self, position, image_path)
		Animatable.__init__(self, image_path)
		self.z_index = z_index  # Un z_index de 1 s'affichera au-dessus d'un z_index de 0

	def get_z_index(self):
		return self.z_index

	def set_z_index(self, z_index: int):
		self.z_index = z_index

	def update(self):
		self.update_index_animation()
		self.go_to_frame(self.frame_index, self.animation_name)

