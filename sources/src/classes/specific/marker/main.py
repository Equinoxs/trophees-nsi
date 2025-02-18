from src.classes import UIElement, GameLoop, SCREEN_HEIGHT, SCREEN_WIDTH


class Marker(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.position = data['position']
		self.x_offset = data.get('x_offset', 0)
		self.y_offset = data.get('y_offset', 0)
		self.special = data.get('special', False)

	def get_special(self):
		return self.special

	def render(self):
		x, y = self.position.convert_to_tuple()

		if self.special:
			camera_x = GameLoop().get_camera().get_camera().x
			camera_y = GameLoop().get_camera().get_camera().y
			zoom = GameLoop().get_camera().get_zoom()

			new_x = max(0, min((SCREEN_WIDTH - self.rect.width) / zoom, x - camera_x / zoom + self.x_offset))
			new_y = max(0, min((SCREEN_HEIGHT - self.rect.height) / zoom, y - camera_y / zoom + self.y_offset))

			self.position.set_all(zoom * new_x, zoom * new_y)

		else:
			self.position.set_all(
				(x - (GameLoop().get_camera().get_camera().x - self.rect.width / 2 ) / GameLoop().get_camera().get_zoom() + self.x_offset) * GameLoop().get_camera().get_zoom(),
				(y - (GameLoop().get_camera().get_camera().y - self.rect.height / 2) / GameLoop().get_camera().get_zoom() + self.y_offset) * GameLoop().get_camera().get_zoom()
			)

		self.update_rect()
		super().render()

		self.position.set_all(x, y)

		self.update_rect()
