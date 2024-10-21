from .. import Sprite, SoundMaker, Animatable, Vector2


class MapElement(Sprite, SoundMaker, Animatable):
	def __init__(self, position: Vector2, image_path: str, frame: tuple[int, int] = (0, 10_000), z_index: int = 0):
		Sprite.__init__(self, position, image_path, frame)
		SoundMaker.__init__(self)
		Animatable.__init__(self)
		self.z_index = z_index  # Un z_index de 1 s'affichera au-dessus d'un z_index de 0

	def get_z_index(self):
		return self.z_index

	def set_z_index(self, z_index: int):
		self.z_index = z_index

	def update(self):
		if self.animation_must_update():
			self.move_frame(500)  # valeur normée partout, à gérer lors de la création des images

	def render(self, screen):
		screen.blit(self.image, self.position.convert_to_tuple())
