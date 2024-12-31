from src.classes import Menu, DataHandler, ButtonActions, SCREEN_WIDTH


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
			self.current_menu = None
			self.current_menu_name = None
			self.load_menus()
			self.set_current_menu(self.current_menu_name)
			self.button_actions = ButtonActions()
			self.message_displayed = None

	def get_button_actions(self):
		return self.button_actions

	def get_menu(self, menu_name):
		return self.menus[menu_name]

	def load_menus(self):
		data = DataHandler().load_menus()
		menus = data['menus']
		if self.current_menu_name is None:
			self.current_menu_name = data['initial_menu']

		for name, data in menus.items():
			self.menus[name] = Menu(data)

	def get_current_menu_name(self):
		return self.current_menu_name

	def get_current_menu(self):
		return self.current_menu

	def set_current_menu(self, menu_name: str):
		if menu_name in self.menus:
			self.current_menu = self.menus[menu_name]
			self.current_menu_name = menu_name

	def update(self):
		if self.current_menu is not None:
			self.current_menu.update()

	def render(self):
		if self.current_menu is not None:
			self.current_menu.render()
