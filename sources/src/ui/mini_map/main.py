import pygame

from src import Button, GameLoop, SCREEN_WIDTH


class MiniMap(Button):
	def __init__(self, data):
		data['action'] = 'open_map'
		data['color'] = 'transparent'
		self.height = data['height']
		self.surface_to_watch = data.get('surface_to_watch', 'map')
		Button.__init__(self, data)

	def update(self):
		original_surface = GameLoop().get_camera().get_surface(self.surface_to_watch)

		new_width = self.height / original_surface.get_height() * original_surface.get_width()
		new_height = self.height
		if new_width > SCREEN_WIDTH:
			new_width = SCREEN_WIDTH
			new_height = new_width / original_surface.get_width() * original_surface.get_height()

		self.surface = pygame.transform.scale(original_surface, (new_width, new_height))

		if GameLoop().get_menu_handler().get_current_menu_name() == 'in_game':
			return super().update()
		else:
			super().update()
			return False

	def render(self):
		super().render('menu', True)