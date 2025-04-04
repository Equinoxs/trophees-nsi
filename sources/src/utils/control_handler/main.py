#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame
from inspect import getmembers

from src import DataHandler, GameLoop


class ControlHandler:
	_instance = None

	# Singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, saved_data = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.events = {'quit': False, 'clicked': False}
			self.keybinds = {}
			self.load_keybinds(saved_data['keybinds'])
			self.mouse_position = None
			self.pygame_events = []
			self.consumed_events = set()
			self.disabled_actions = set()
			self.settings_initialized = False

	def load_keybinds(self, keybinds_data):
		'''
		Convertit les valeurs stockées en constantes Pygame si nécessaire.
		'''
		self.keybinds = {action: getattr(pygame, key) if isinstance(key, str) else key for action, key in keybinds_data.items()}

	def get_pygame_key_name(self, key):
		pygame_vars = getmembers(pygame)
		return [var_name for var_name, var_val in pygame_vars if var_val is key if var_name.startswith('K_')]

	def get_keybinds(self):
		return self.keybinds

	def disable_actions(self, actions: list[str]):
		for key in actions:
			self.disabled_actions.add(key)

	def disable_all_actions(self):
		self.disable_actions(self.keybinds.keys())

	def enable_actions(self, actions: list[str]):
		for key in actions:
			self.disabled_actions.discard(key)

	def enable_all_actions(self):
		self.enable_actions(self.keybinds.keys())

	def handle_events(self):
		if not self.settings_initialized:
			self.initialize_settings_inputs()

		self.mouse_position = pygame.mouse.get_pos()
		self.finish_event('clicked')  # Réinitialiser l'état de clic à chaque frame
		self.pygame_events = pygame.event.get()

		for event in self.pygame_events:
			match event.type:
				case pygame.QUIT:
					self.events['quit'] = True
				case pygame.KEYDOWN:
					for action, key in self.keybinds.items():
						if key == event.key and action not in self.consumed_events and action not in self.disabled_actions:
							self.activate_event(action)
				case pygame.KEYUP:
					for action, key in self.keybinds.items():
						if key == event.key:
							self.finish_event(action)
							self.consumed_events.discard(action)
				case pygame.MOUSEBUTTONDOWN:
					self.activate_event('clicked')

	def is_activated(self, event_name: str):
		return self.events.get(event_name, False)

	def is_clicked(self, button):
		return self.is_activated('clicked') and button.get_rect().collidepoint(self.mouse_position)

	def activate_event(self, event_name: str):
		self.events[event_name] = True

	def finish_event(self, event_name: str):
		self.events[event_name] = False

	def reset_keybinds(self):
		menu = GameLoop().get_menu_handler().get_menu('settings')
		self.load_keybinds(DataHandler().load_save(new_game=True, reload=False)['keybinds'])

		for element in menu.get_elements():
			if getattr(element, 'event_name', None) is not None:
				menu.delete_element(element)

		self.initialize_settings_inputs()


	def consume_event(self, event_name: str):
		self.consumed_events.add(event_name)
		self.finish_event(event_name)

	def get_key_letter(self, event_name: str):
		'''
		Retourne le nom de la touche associée à un événement.
		'''
		key = self.keybinds.get(event_name)
		if key:
			return pygame.key.name(key)
		else:
			return None

	def get_pygame_events(self):
		return self.pygame_events

	def set_keybind(self, event_name: str, key: str):
		self.keybinds[event_name] = key

	def initialize_settings_inputs(self):
		aliases = {
			'pause': 'Pause',
			'interacted': 'Interact',
			'pick_drop': 'Pick/drop items',
			'go_forward': 'Move Forward',
			'go_backward': 'Move Backward',
			'go_right': 'Move Right',
			'go_left': 'Move Left',
			'sprint': 'Sprint',
			'toggle_map': 'Toggle Map',
			'pass_message_dialog': 'Pass Dialogs'
		}

		i = 0
		menu = GameLoop().get_menu_handler().get_menu('settings')

		for event, alias in aliases.items():
			y = 220 + i * 55
			label_data = {
				'type': 'UIElement',
				'class': 'key_settings_label',
				'label': alias,
				'y': y+7
			}

			input_data = {
				'type': 'KeybindInput',
				'class': 'key_settings_input',
				'event_name': event,
				'default_text': pygame.key.name(self.keybinds[event]),
				'y': y
			}

			i += 1

			if not menu.get_elements(event):
				GameLoop().get_menu_handler().get_menu('settings').add_element(label_data)
				GameLoop().get_menu_handler().get_menu('settings').add_element(input_data)

			self.settings_initialized = True
