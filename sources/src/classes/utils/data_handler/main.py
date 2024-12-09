import json
import os

from src.classes import Vector2, MissionHandler, TimeHandler, Player, LogHandler, SAVE
from src.classes import interactions, pattern_events, side_effects, missions


class DataHandler:
	_instance = None
	current_save = None

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
			self.missions_data = None
			self.menus_data = None
			self.current_save_chrono_tag = None
			self.last_save_player_position = None


	def get_data_from_last_save(self):
		# Il faut utiliser os.path.dirname pour éviter des chemins incorrects
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'..', '..', '..', '..', 'backups', 'automatic', 'main-save.json'
		)

		# Ouverture du fichier de sauvegarde principale
		try:
			with open(path, 'r') as save:
				data = json.load(save)
				LogHandler().add('/'.join(path.split('/')[-2:]), 'loaded')
		except FileNotFoundError:
			# Si le fichier de sauvegarde principale est vide ou inexistant, on utilise le backup par défaut
			with open(self.default_save_path, 'r') as save:
				data = json.load(save)
				LogHandler().add(self.default_save_path.split('/')[-1:][0], 'loaded')

		for map in data['maps']:
			for element_index in range(len(data['maps'][map]['elements'])):
				data['maps'][map]['elements'][element_index]['position'] = self.list_to_vector2(data['maps'][map]['elements'][element_index]['position'])

				if 'pattern_timeline' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['pattern_timeline'] = self.list_transform(data['maps'][map]['elements'][element_index]['pattern_timeline'], self.get_pattern_event)
				else:
					data['maps'][map]['elements'][element_index]['pattern_timeline'] = []

				if 'interaction' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['interaction'] = self.get_interaction(data['maps'][map]['elements'][element_index]['interaction'])

				if 'side_effects' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['side_effects'] = self.list_transform(data['maps'][map]['elements'][element_index]['side_effects'], self.get_side_effect)
				else:
					data['maps'][map]['elements'][element_index]['side_effects'] = []

				if 'authorized_sound_tracks' not in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['authorized_sound_tracks'] = []
		return data

	def load_save(self, force = False):
		if self.current_save is None or force:
			self.current_save = self.get_data_from_last_save()
		return self.current_save


	def save_data(self, data, backup_path):
		# Correction de la redondance du mot-clé 'path'
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'..', '..', '..', '..', 'backups', backup_path, 'main-save.json'
		)

		TimeHandler().add_chrono_tag('last_save', reset=True)
		self.last_save_player_position = Vector2(0, 0).copy(Player().get_focus().get_position())

		# Enregistrement des données dans le fichier JSON
		with open(path, 'w') as file:
			json.dump(data, file, indent=4, cls=JSONEncoder)

	def save(self, automatic = False):
		if not SAVE: return  # ne pas faire de sauvegardes (debug)
		LogHandler().add("Automatic save done")
		self.save_data(self.current_save, 'manual' if not automatic else 'automatic')


	def must_save(self):
		if self.last_save_player_position is None:
			self.last_save_player_position = Vector2(0, 0).copy(Player().get_focus().get_position())  # faire une copie de l'objet pour éviter d'accéder à la même instance
		return Player().get_focus().get_position().distance_to(self.last_save_player_position) > 100 or TimeHandler().add_chrono_tag('last_save') > 300  # 5 minutes


	def get_image_data(self, dir_name: str):
		png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'assets', 'images', dir_name, 'image.png')
		json_path = os.path.join(os.path.dirname(png_path), 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)
		
		return data, png_path
	
	def load_image(self, dir_name: str, force = False):
		if dir_name not in self.images_data or force:
			self.images_data[dir_name] = self.get_image_data(dir_name)
		return self.images_data[dir_name]


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
				data[dir_name] = self.get_sound_track_data(dir_name)[1]
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
		for mission in data['missions']:
			data['missions'][mission]['objectives'] = missions[mission]
		return data['missions']

	def load_missions(self, force: bool = False):
		if self.missions_data is None or force:
			self.missions_data = self.get_missions_data()
		return self.missions_data


	def get_menus_data(self):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'menu_handler', 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)

		return data['menus']

	def load_menus(self, force: bool = False):
		if self.menus_data is None or force:
			self.menus_data = self.get_menus_data()
		return self.menus_data



	def get_interaction(self, interaction_name: str = None):
		if len(interaction_name) > 6 and interaction_name[:6] == 'start_' and interaction_name[6:] in missions:
			def start_new_mission(self):
				MissionHandler().start_mission(interaction_name[6:])
			return start_new_mission
		if interaction_name == '' or interaction_name is None or interaction_name not in interactions:
			def default(self):
				return
			return default
		return interactions.get(interaction_name)

	def get_side_effect(self, side_effect_name: str = None):
		if side_effect_name == '' or side_effect_name is None or side_effect_name not in side_effects:
			def default(self):
				return
			return default
		return side_effects.get(side_effect_name)

	def get_pattern_event(self, pattern_event_name: str = None):
		if pattern_event_name == '' or pattern_event_name is None or pattern_event_name not in pattern_events:
			def default(self, delta_time):
				return
			return default
		return pattern_events.get(pattern_event_name)

	def list_to_vector2(self, list2: list):
		if type(list2) == list and len(list2) == 2:
			return Vector2(list2[0], list2[1])
		else:
			raise AttributeError

	def list_transform(self, list2: list, function_collecting_method):
		new_list = []
		for el in list2:
			if type(el) == list:
				new_list.append(Vector2(el[0], el[1]))
			elif type(el) == str:
				new_list.append(function_collecting_method(el))
			else:
				raise ValueError
		return new_list


class JSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Vector2): return obj.convert_to_tuple()
		if callable(obj): return obj.__name__  # fonctions d'interaction
		return super().default(obj)
