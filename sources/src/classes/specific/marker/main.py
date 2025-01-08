from src.classes import UIElement, GameLoop


class Marker(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.position = data['position']
		self.x_offset = data['x_offset']
		self.y_offset = data['y_offset']

	def render(self):
		x, y = self.position.convert_to_tuple()
		self.position.set_all(
    		x - GameLoop().get_camera().get_camera().get_x() - self.rect.width / 2 + self.x_offset,
    		y - GameLoop().get_camera().get_camera().get_y() - self.rect.height / 2 + self.y_offset
    	)
		self.update_rect()
		super().render()
		self.position.set_all(x, y)
		self.update_rect()
