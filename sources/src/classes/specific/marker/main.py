from src.classes import UIElement, GameLoop


class Marker(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.position = data['position']
		self.x_offset = data.get('x_offset', 0)
		self.y_offset = data.get('y_offset', 0)

	def render(self):
		x, y = self.position.convert_to_tuple()
		self.position.set_all(
			(x - (GameLoop().get_camera().get_camera().x - self.rect.width / 2 ) / GameLoop().get_camera().get_zoom() + self.x_offset) * GameLoop().get_camera().get_zoom(),
			(y - (GameLoop().get_camera().get_camera().y - self.rect.height / 2) / GameLoop().get_camera().get_zoom() + self.y_offset) * GameLoop().get_camera().get_zoom()
		)
		self.update_rect()
		super().render()
		self.position.set_all(x, y)
		self.update_rect()
