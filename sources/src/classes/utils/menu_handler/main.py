import pygame
from src.classes import Menu, DataHandler, GameLoop, SCREEN_WIDTH, SCREEN_HEIGHT


class MenuHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.menus = {}
			self.load_menus()
			self.current_menu = None
			self.set_current_menu('in_game')
			self.actions = {}

	def load_menus(self):
		menus = DataHandler().load_menus()

		for name, data in menus.items():
			self.menus[name] = Menu(data)

	def set_current_menu(self, menu_name: str):
		if menu_name in self.menus:
			self.current_menu = self.menus[menu_name]

	def update(self):
		if self.current_menu is not None:
			self.current_menu.update()

	def render(self):
		if GameLoop().is_game_paused():
			pause_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
			pause_overlay.fill((0, 0, 0, 200))
			GameLoop().get_camera().draw(pause_overlay, (0, 0), 'menu')

		if self.current_menu is not None:
			self.current_menu.render()
