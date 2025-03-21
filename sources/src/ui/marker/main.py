from src import UIElement, GameLoop, SCREEN_HEIGHT, SCREEN_WIDTH


class Marker(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.position = data['position']
		self.real_image = data.get('real_image', None)
		self.x_offset = data.get('x_offset', 0)
		self.y_offset = data.get('y_offset', 0)
		self.special = data.get('special', False)

	def get_special(self):
		return self.special

	def render(self):
		x, y = self.position.convert_to_tuple()

		if self.special:
			zoom = GameLoop().get_camera().get_zoom()

			camera_x = GameLoop().get_camera().get_camera().x / zoom
			camera_y = GameLoop().get_camera().get_camera().y / zoom
			max_x = (SCREEN_WIDTH - self.rect.width) / zoom
			max_y = (SCREEN_HEIGHT - self.rect.height) / zoom
			rel_x = x - camera_x + self.x_offset
			rel_y = y - camera_y + self.y_offset

			new_x = max(0, min(max_x, rel_x))
			new_y = max(0, min(max_y, rel_y))

			if rel_x - SCREEN_WIDTH / 2 == 0:
				rel_x += 1

			a = (rel_y - SCREEN_HEIGHT / 2) / (rel_x - SCREEN_WIDTH / 2)
			b = rel_y - a * rel_x

			possible_new_y = a * rel_x + b
			if possible_new_y >= max_y or possible_new_y < 0:
				new_x = (new_y - b) / a
			else:
				new_y = possible_new_y

			new_x = max(0, min(max_x, new_x))
			new_y = max(0, min(max_y, new_y))

			self.position.set_all(zoom * new_x, zoom * new_y)

		else:
			self.position.set_all(
				(x - (GameLoop().get_camera().get_camera().x - self.rect.width / 2 ) / GameLoop().get_camera().get_zoom() + self.x_offset) * GameLoop().get_camera().get_zoom(),
				(y - (GameLoop().get_camera().get_camera().y - self.rect.height / 2) / GameLoop().get_camera().get_zoom() + self.y_offset) * GameLoop().get_camera().get_zoom()
			)

		self.update_rect()
		super().render()

		if self.real_image is not None:
			GameLoop().get_camera().draw(self.real_image, self.position, 'menu')

		self.position.set_all(x, y)

		self.update_rect()
