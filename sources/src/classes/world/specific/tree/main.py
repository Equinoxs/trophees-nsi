from src.classes import PillarObject, Vector2, Camera, Player


class Tree(PillarObject):
	def __init__(self, data):
		self.image_type = 'tree'

		def get_hit(self):
			vector = Player().get_focus().get_position() - self.position
			Player().get_focus().get_position().add(vector.set_norm(30 * Camera().get_zoom()))

		data['interaction'] = get_hit
		self.hitbox = [Vector2(0, 0)]
		self.hitbox_action_radius = 30  # hitbox plus grosse
		super().__init__(data)

	def render(self):
		width, height = self.image.get_size()
		x, y = self.position.convert_to_tuple()
		self.position.set_all(x - width / 2 / Camera().get_zoom(), y - height / Camera().get_zoom())
		super().render()
		self.position.set_all(x, y)

	def get_data(self):
		data = super().get_data()
		if 'interaction' in data:
			del data['interaction'] # pas besoin dans la sauvegarde
		return data
