import json
import os
import pygame
from time import time
from copy import deepcopy

from src.classes import Vector2, TimeHandler, Player, LogHandler, SAVE, GameLoop


class DataHandler:
	_instance = None
	current_save = None
	model = {
		'type': 'required',
		'image_path': None,
		'name': 'anonymous',
		'position': [0, 0],
		'authorized_sound_tracks': [],
		'z_index': 0,
		'interaction': None,
		'pattern_timeline': [],
		'pattern_type': 'loop',
		'level': 1,
		'side_effects': [],
		'boundaries': [],
		'required_level': 0,
		'wall_type': 'gray_brick',
		'wall_height': None,
		'wall_width': None,
		'mission': None
	}

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True  # Empêche une nouvelle initialisation
			# Il faut utiliser os.path.dirname pour remonter le chemin correctement
			self.default_save_path = os.path.join(
				os.path.dirname(os.path.abspath(__file__)),
				'..', '..', '..', '..', 'backups', 'new_game_backup.json'
			)
			self.images_data = {}
			self.sounds_data = {}
			self.stickers_data = {}
			self.fonts = {}
			self.missions_data = None
			self.menus_data = None
			self.current_save_chrono_tag = None
			self.last_save_player_position = None


	def get_data_from_last_save(self, name: str):
		if name is not None:

			path = os.path.join(
				os.path.dirname(os.path.abspath(__file__)),
				'..', '..', '..', '..', 'backups', name + '.json'
			)

			try:
				with open(path, 'r') as save:
					data = json.load(save)
					LogHandler().add('/'.join(path.split('/')[-2:]), 'loaded')
			except FileNotFoundError:
				with open(self.default_save_path, 'r') as save:
					data = json.load(save)
					LogHandler().add(self.default_save_path.split('/')[-1:][0], 'loaded')
		else:
			with open(self.default_save_path, 'r') as save:
				data = json.load(save)
				LogHandler().add(self.default_save_path.split('/')[-1:][0], 'loaded')
		for map in data['maps']:
			for element_index in range(len(data['maps'][map]['elements'])):
				# Pour s'assurer que tous les objets aient leurs propriétés définies
				for required_key, default_value in self.model.items():
					if required_key not in data['maps'][map]['elements'][element_index]:
						data['maps'][map]['elements'][element_index][required_key] = data['maps'][map]['elements'][element_index].get(required_key, default_value)

				# Post-processing
				data['maps'][map]['elements'][element_index]['position'] = self.list_to_vector2(data['maps'][map]['elements'][element_index]['position'])
				data['maps'][map]['elements'][element_index]['pattern_timeline'] = self.list_transform(data['maps'][map]['elements'][element_index]['pattern_timeline'])
				data['maps'][map]['elements'][element_index]['side_effects'] = self.list_transform(data['maps'][map]['elements'][element_index]['side_effects'])
				data['maps'][map]['elements'][element_index]['boundaries'] = self.list_transform(data['maps'][map]['elements'][element_index]['boundaries'])
		return data

	def load_save(self, name = 'default', force = False):
		if self.current_save is None or force:
			self.current_save = self.get_data_from_last_save(name)
		return self.current_save


	def save_data(self, original_data: dict, name):
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'..', '..', '..', '..', 'backups', name + '.json'
		)

		data = deepcopy(original_data) # copie

		for map in data['maps']:
			for element_index in range(len(data['maps'][map]['elements'])):
				# Pour ne pas sauvegarder de données inutiles
				for required_key, default_value in self.model.items():
					if required_key in data['maps'][map]['elements'][element_index] and data['maps'][map]['elements'][element_index][required_key] == default_value:
						data['maps'][map]['elements'][element_index].pop(required_key)
			if map == Player().get_map_name():
				for element_index in range(len(data['maps'][map]['elements'])):
					if data['maps'][map]['elements'][element_index]['type'] == 'NPC' and data['maps'][map]['elements'][element_index]['name'] == Player().get_focus().get_name():
						data['maps'][map]['elements'][element_index]['position'] = [int(p) for p in Player().get_focus().get_position().convert_to_tuple()]

		TimeHandler().add_chrono_tag('last_save', reset=True)
		self.last_save_player_position = Vector2(0, 0).copy(Player().get_focus().get_position())

		data['last_save_time'] = time()
		data['keybinds'] = GameLoop().get_control_handler().get_keybinds()
		print(data)
		print(original_data)
		with open(path, 'w') as file:
			json.dump(data, file, indent=4, cls=JSONEncoder)

	def save(self, name = 'default'):
		if not SAVE:
			return  # ne pas faire de sauvegardes (debug)
		LogHandler().add("Automatic save done")
		assert name != 'new_game_backup' # TODO: mettre un vrai système
		self.save_data(self.current_save, name)

	def get_save_files(self):
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'..', '..', '..', '..', 'backups'
		)
		save_files = []
		for f in os.listdir(path):
			if f.endswith('.json') and os.path.isfile(os.path.join(path, f)) and f != 'new_game_backup.json':
				save_files.append(f)
		return save_files

	def save_name_valid(self, name):
		forbidden_chars = '*|!:/\\?<>"'
		forbidden_names = ['.', '..', 'CON', 'PRN', 'AUX', 'NUL'] + [f'LPT{x}' for x in range(1, 10)] + [f'COM{x}' for x in range(1, 10)]
		return not any(c in name for c in forbidden_chars) and not any(n == name.upper() for n in forbidden_names)

	def must_save(self):
		if self.last_save_player_position is None:
			self.last_save_player_position = Player().get_focus().get_position().copy()  # faire une copie de l'objet pour éviter d'accéder à la même instance
		return Player().get_focus().get_position().distance_to(self.last_save_player_position) > 100 or TimeHandler().add_chrono_tag('last_save') > 300  # 5 minutes


	def get_image_data(self, dir_name: str):
		png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'images', dir_name, 'image.png')
		json_path = os.path.join(os.path.dirname(png_path), 'info.json')

		model = {
			'animations': {},
			'hitbox': []
		}

		with open(json_path, 'r') as file:
			data = json.load(file)

		for required_key, default_value in model.items():
			data[required_key] = data.get(required_key, default_value)
		
		return data, png_path
	
	def load_image(self, dir_name: str, image_type: str = '', force = False):
		dir_name = os.path.join(image_type, dir_name)
		if dir_name not in self.images_data or force:
			self.images_data[dir_name] = self.get_image_data(dir_name)
		return self.images_data[dir_name]

	def load_wall_images(self, dir_name: str):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'images', 'wall', dir_name, 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)

		if type(data['images']['front']) == str:
			front_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['front'] + '.png'), 'height': None }
		else:
			front_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['front']['path'] + '.png'), 'height': data['images']['front']['height'] }

		if 'side' not in data['images']:
			side_data = {}
		elif type(data['images']['side']) == str:
			side_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['side'] + '.png'), 'height': None }
		else:
			side_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['side']['path'] + '.png'), 'height': data['images']['side']['height'] }

		if 'top' not in data['images']:
			top_data = {}
		elif type(data['images']['top']) == str:
			top_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['top'] + '.png'), 'height': None }
		else:
			top_data = { 'path': os.path.join(os.path.dirname(json_path), data['images']['top']['path'] + '.png'), 'height': data['images']['top']['height'] }

		return data, front_data, side_data, top_data

	def load_ui_elements_image(self, image_name: str):
		png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'images', 'ui_element', image_name + '.png')
		return png_path

	def get_sticker_data(self, sticker_name: str):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'images','wall_sticker', sticker_name, 'info.json')
		with open(json_path, 'r') as file:
			data = json.load(file)

		png_path = os.path.join(os.path.dirname(json_path), 'image.png')
		return data, png_path

	def load_sticker_data(self, sticker_name: str, height: int = None, force: bool = False):
		if sticker_name not in self.stickers_data or force:
			self.stickers_data[sticker_name] = self.get_sticker_data(sticker_name)
		data, png_path = self.stickers_data[sticker_name]
		return data, self.get_image_surface(png_path, height if height is not None else data.get('height', None))

	def get_image_surface(self, image_path: str, target_height: int = None):
		image = pygame.image.load(image_path).convert_alpha()
		if target_height is not None:
			width, height = image.get_size()
			image = pygame.transform.scale(image, (width * target_height / height, target_height))
		return image





	def get_sound_track_data(self, dir_name: str):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'sounds', 'effects', dir_name, 'info.json')
		with open(json_path, 'r') as file:
			data = json.load(file)

		sound_paths = {}
		for sound_name in data['sounds']:
			sound_paths[sound_name] = os.path.join(os.path.dirname(json_path), sound_name + '.' + data['sounds'][sound_name]['extension'])

		return data, sound_paths

	def get_all_sound_tracks_data(self):
		data = {}
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'sounds', 'effects')
		for dir_name in os.listdir(path):
			full_path = os.path.join(path, dir_name)
			if os.path.isdir(full_path):
				data[dir_name] = self.get_sound_track_data(dir_name)
		return data


	def load_sound(self, dir_name: str, sound_name: str, force = False):
		if dir_name not in self.sounds_data or force:
			self.sounds_data[dir_name] = {}
			self.sounds_data[dir_name][sound_name] = self.get_sound_data(dir_name, sound_name)
		elif sound_name not in self.sounds_data[dir_name] or force:
			self.sounds_data[dir_name][sound_name] = self.get_sound_data(dir_name, sound_name)

		return self.sounds_data[dir_name][sound_name]

	def load_music(self, music_name: str):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'sounds', 'music', 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)
		if not music_name in data['sounds']: return None

		return data, os.path.join(os.path.dirname(json_path), music_name + '.' + data['sounds'][music_name]['extension'])


	def get_missions_data(self):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mission_handler', 'missions.json')
		with open(json_path, 'r') as file:
			data = json.load(file) 
		return data['missions']

	def load_missions(self, force: bool = False):
		if self.missions_data is None or force:
			self.missions_data = self.get_missions_data()
		return self.missions_data


	def get_menus_data(self):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'menu_handler', 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)

		return data

	def load_menus(self, force: bool = False):
		if self.menus_data is None or force:
			self.menus_data = self.get_menus_data()
		return self.menus_data


	def get_font_data(self, font_name: str, font_size: int):
		font_path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'..', '..', '..', '..', 'assets', 'fonts', font_name + '.ttf'
		)
		return pygame.font.Font(font_path, font_size)

	def load_font(self, font_name: str, font_size: int, force: bool = False):
		key = font_name + str(font_size)
		if key not in self.fonts or force:
			self.fonts[key] = self.get_font_data(font_name, font_size)
		return self.fonts[key]


	def list_to_vector2(self, list2: list):
		if type(list2) == list and len(list2) == 2:
			return Vector2(list2[0], list2[1])
		elif isinstance(list2, Vector2):
			return list2
		else:
			raise AttributeError

	def list_transform(self, list2: list):
		new_list = []
		for el in list2:
			if type(el) == list:
				new_list.append(Vector2(el[0], el[1]))
			else:
				new_list.append(el)
		return new_list


class JSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Vector2):
			return obj.convert_to_tuple()
		if callable(obj):
			return obj.__name__  # fonctions d'interaction
		return super().default(obj)
