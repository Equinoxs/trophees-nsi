from src.classes import Player

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
			self.zoom = 1
			elements = Player().get_map().get_elements()
			for element in elements:
				element.set_magnification(element.get_magnification() * self.zoom)

	def get_zoom(self):
		return self.zoom

	def update(self):
		elements = Player().get_map().get_elements()
		width, height = Player().get_focus().get_image().get_size()
		self.camera.center = (self.zoom * (self.player_pos.get_x() + width / 2), self.zoom * (self.player_pos.get_y() + height / 2))
		# Remplir l'écran de noir
		self.screen.fill((0,) * 3)
		for element in elements:
			self.screen.blit(
	   			element.get_image(),
				(
					self.zoom * (element.get_position().get_x() - self.camera.x),
			 		self.zoom * (element.get_position().get_y() - self.camera.y)
				)
			)