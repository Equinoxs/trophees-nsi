from src.classes import PillarObject, Vector2, Camera


class Tree(PillarObject):
	def __init__(self, data):
		self.image_type = 'tree'
		self.hitbox = [Vector2(0, 0)]
		self.hitbox_action_radius = 30  # hitbox plus grosse
		super().__init__(data)

	def render(self):
		width, height = self.image.get_size()
		x, y = self.position.convert_to_tuple()
		self.position.set_all(x - width / 2 / Camera().get_zoom(), y - height / Camera().get_zoom())
		super().render()
		self.position.set_all(x, y)