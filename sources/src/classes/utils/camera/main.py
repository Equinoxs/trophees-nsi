import pygame

from src.classes import Player, MenuHandler, LogHandler, GameLoop, Vector2, SCREEN_WIDTH, SCREEN_HEIGHT


class Camera:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, screen = None):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.screen = screen
			self.frame = self.screen.get_rect()
			self.camera = self.frame.copy()
			self.player_pos = Player().get_focus().get_position()
			self.zoom = 1.4
			elements = Player().get_map().get_elements()
			self.is_map_rendered = False
			self.surfaces = { 'mini_map': pygame.Surface((self.zoom * 1200, self.zoom * 1200), pygame.SRCALPHA) }
			for element in elements:
				element.set_magnification(element.get_magnification() * self.zoom)

	def _create_surface(self, surface_name):
		if surface_name not in set(self.surfaces.keys()):
			self.surfaces[surface_name] = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.SRCALPHA)

	def get_zoom(self):
		return self.zoom

	def get_is_map_rendered(self):
		return self.is_map_rendered

	def map_rendered(self):
		self.is_map_rendered = True

	def map_not_rendered(self):
		self.is_map_rendered = False

	def get_screen(self):
		return self.screen

	def get_surface(self, surface_name: str)->pygame.Surface:
		self._create_surface(surface_name)
		return self.surfaces[surface_name]

	def get_frame(self):
		return self.frame

	def get_camera(self):
		return self.camera

	def update(self):
		_, height = Player().get_focus().get_image().get_size()
		self.camera.center = (int(self.zoom * self.player_pos.get_x()), int(self.zoom * self.player_pos.get_y() - height / 2))
		self.screen.fill((0,) * 3)  # Couleur de fond = noir

		for surface_name in self.surfaces.keys():
			self.surfaces[surface_name].fill((0,) * 4)

		for element in Player().get_map().get_elements():
			element.render()
		LogHandler().render()
		MenuHandler().render()
		assert False
		for surface_name in self.surfaces.keys():
			if self.is_map_rendered:
				self.screen.blit(self.surfaces['map'], (0, 0))
			self.screen.blit(self.surfaces['menu'], (0, 0))

	def draw(self, surface_to_draw: pygame.Surface, position = (0, 0), surface_target_name: str = 'map', is_player_rendered: bool = False):
		self._create_surface(surface_target_name)

		if isinstance(position, Vector2):
			x, y = position.convert_to_tuple()
		elif type(position) == tuple:
			x, y = position
		else:
			raise ValueError

		match surface_target_name:
			case 'map':
				if self.is_map_rendered:
					if is_player_rendered:
						width, height = surface_to_draw.get_size()
						self.surfaces['map'].blit(surface_to_draw, ((SCREEN_WIDTH - width) // 2, (SCREEN_HEIGHT - height) // 2))
					else:
						self.surfaces['map'].blit(surface_to_draw, (x * self.zoom - self.camera.x, y * self.zoom - self.camera.y))
					self.surfaces['mini_map'].blit(surface_to_draw, (int(self.zoom * (x + 600)), int(self.zoom * (y + 600))))
			case _:
				self.surfaces[surface_target_name].blit(surface_to_draw, (x, y))
