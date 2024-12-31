from src.classes import UIElement, GameLoop


class Marker(UIElement):
	def __init__(self, data, position):
		super().__init__(data)
		self.position = position

	def render(self):
		x, y = self.position.convert_to_tuple()
		self.position.set_all(
    		x - GameLoop().get_camera().get_camera().get_x() - self.rect.width / 2,
    		y - GameLoop().get_camera().get_camera().get_y() - self.rect.height - 10
    	)
		self.update_rect()
		super().render()
		self.position.set_all(x, y)
		self.update_rect()
