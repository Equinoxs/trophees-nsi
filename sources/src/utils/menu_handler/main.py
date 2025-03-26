#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame

from src import Menu, DataHandler, GameLoop, ButtonActions


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
			self.markers = []
			self.dialogs = {}
			self.current_menu = None
			self.current_menu_name = None
			self.load_menus()
			self.set_current_menu(self.current_menu_name, update=False)
			self.button_actions = ButtonActions()
			self.fps_toggled = True

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
		self.markers.append(element)
		return element

	def remove_marker(self, marker_ref):
		self.menus['in_game'].delete_element(marker_ref)
		del self.markers[self.markers.index(marker_ref)]

	def add_dialog(self, dialog_name: str, dialog_data: dict):
		dialog_data['type'] = 'Dialog'
		dialog_data['title'] = dialog_name
		dialog_data['class'] = 'default_dialog'
		self.dialogs[dialog_name] = self.menus['in_game'].add_element(dialog_data)

	def remove_dialog(self, dialog_name: str):
		self.menus['in_game'].delete_element(self.dialogs[dialog_name])
		del self.dialogs[dialog_name]

	def is_dialog(self, dialog_name: str):
		return dialog_name in self.dialogs

	def get_current_menu_name(self):
		return self.current_menu_name

	def get_current_menu(self):
		return self.current_menu

	def get_fps_toggled(self):
		return self.fps_toggled
	
	def toggle_fps(self):
		if self.fps_toggled:
			self.fps_toggled = False
		else:
			self.fps_toggled = True

	def set_current_menu(self, menu_name: str, force_render: bool = False, update: bool = True):
		if menu_name == 'map_opened':
			GameLoop().get_camera().set_is_full_map_rendered(True)
		elif self.current_menu_name == 'map_opened' and menu_name != 'map_opened':
			GameLoop().get_camera().set_is_full_map_rendered(False)

		if menu_name in self.menus:
			if self.current_menu_name:
				self.menus_historics.append(self.current_menu_name)
			self.current_menu = self.menus[menu_name]
			self.current_menu_name = menu_name

		if update:
			self.update()
		if force_render:
			self.render()
			GameLoop().get_camera().get_screen().blit(GameLoop().get_camera().get_surface('menu'), (0, 0))
			pygame.display.flip()
	
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

		# Gérer l'affichage des markers spéciaux sur la grande map
		if self.current_menu_name == 'map_opened':
			for marker in self.markers:
				if marker.get_special() and marker.get_image() is not None:
					x, y =  marker.get_position().convert_to_tuple()
					marker.get_position().set_all(x + marker.x_offset, y + marker.y_offset)
					GameLoop().get_camera().draw(marker.get_image(), marker.get_position(), 'map')
					marker.get_position().set_all(x, y)
