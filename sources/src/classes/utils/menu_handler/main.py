from src.classes import Menu, DataHandler, ButtonActions


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
			self.menus_historics = []
			self.classes = {}
			self.markers = {}
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

	def get_class(self, class_name):
		if class_name in set(self.classes.keys()):
			return self.classes[class_name]
		else:
			return {}

	def load_menus(self):
		data = DataHandler().load_menus()
		menus = data['menus']
		self.classes = data['classes']
		if self.current_menu_name is None:
			self.current_menu_name = data['initial_menu']
		self.menus_historics.append(self.current_menu_name)
		for name, data in menus.items():
			self.menus[name] = Menu(data)

	def add_marker(self, marker_data: dict):
		marker_data['type'] = 'Marker'
		element = self.menus['in_game'].add_element(marker_data)
		return element

	def remove_marker(self, marker_ref):
		self.menus['in_game'].delete_element(marker_ref)

	def get_current_menu_name(self):
		return self.current_menu_name

	def get_current_menu(self):
		return self.current_menu

	def set_current_menu(self, menu_name: str):
		if menu_name in self.menus:
			if self.current_menu_name:
				self.menus_historics.append(self.current_menu_name)
			self.current_menu = self.menus[menu_name]
			self.current_menu_name = menu_name
	
	def get_last_menu(self):
		if self.menus_historics:
			return self.menus_historics[-1]
		return None
	
	def set_last_menu(self):
		last_menu = self.get_last_menu()
		if last_menu and last_menu in self.menus:
			self.current_menu = self.menus[last_menu]
			self.current_menu_name = last_menu

	def update(self):
		if self.current_menu is not None:
			self.current_menu.update()

	def render(self):
		if self.current_menu is not None:
			self.current_menu.render()
