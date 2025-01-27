import pygame

from src.classes import Player, MenuHandler, LogHandler, DataHandler, Vector2, SCREEN_WIDTH, SCREEN_HEIGHT


class Camera:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, screen = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True

			self.screen = screen
			self.frame = self.screen.get_rect()
			self.camera = self.frame.copy()

			self.zoom = 1.2
			self.map_overflow_factor = 1.5

			self.is_map_rendered = False
			self.is_full_map_rendered = False

			self.initialize()

	def initialize(self):
		self.player_pos = Player().get_focus().get_position()
		self.surfaces = {}
		self.initialize_surfaces()

		elements = Player().get_map().get_elements()
		for element in elements:
			element.set_magnification(self.zoom)

	def initialize_surfaces(self):
			backup = DataHandler().load_save()
			current_map_name = Player().get_map_name()
			top_left_corner = backup['maps'][current_map_name]['top_left_corner']
			bottom_right_corner = backup['maps'][current_map_name]['bottom_right_corner']
			self.surfaces['full_map'] = pygame.Surface((self.zoom * (bottom_right_corner[0] - top_left_corner[0]), self.zoom * (bottom_right_corner[1] - top_left_corner[1])), pygame.SRCALPHA)
   
			self.surfaces['map'] = pygame.Surface((int(SCREEN_WIDTH * self.map_overflow_factor), int(SCREEN_HEIGHT * self.map_overflow_factor)), pygame.SCALED | pygame.SRCALPHA)
			self.surfaces['menu'] = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.SRCALPHA)

	def get_zoom(self):
		return self.zoom

	def get_is_map_rendered(self):
		return self.is_map_rendered

	def map_rendered(self):
		self.is_map_rendered = True

	def map_not_rendered(self):
		self.is_map_rendered = False

	def full_map_rendered(self):
		self.is_full_map_rendered = True

	def full_map_not_rendered(self):
		self.is_full_map_rendered = False

	def get_screen(self):
		return self.screen

	def get_surface(self, surface_name: str) -> pygame.Surface:
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
		for surface_name in self.surfaces.keys():
			if self.is_map_rendered:
				self.screen.blit(self.surfaces['map'], (-SCREEN_WIDTH * (self.map_overflow_factor - 1) / 2, -SCREEN_HEIGHT * (self.map_overflow_factor - 1) / 2))
			self.screen.blit(self.surfaces['menu'], (0, 0))

	def draw(self, surface_to_draw: pygame.Surface, position = (0, 0), surface_target_name: str = 'map', is_player_rendered: bool = False):
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
						self.surfaces['map'].blit(surface_to_draw, ((self.surfaces['map'].get_width() - width) // 2, (self.surfaces['map'].get_height() - height) // 2))
					else:
						self.surfaces['map'].blit(surface_to_draw, (
							int(x * self.zoom - self.camera.x + SCREEN_WIDTH * (self.map_overflow_factor - 1) / 2),
							int(y * self.zoom - self.camera.y + SCREEN_HEIGHT * (self.map_overflow_factor - 1) / 2)
						))
				if self.is_full_map_rendered:
					top_left_corner = DataHandler().load_save()['maps'][Player().get_map_name()]['top_left_corner']
					self.surfaces['full_map'].blit(surface_to_draw, (int(self.zoom * (x - top_left_corner[0])), int(self.zoom * (y - top_left_corner[1]))))
			case _:
				self.surfaces[surface_target_name].blit(surface_to_draw, (x, y))
