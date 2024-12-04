import json
import os

from src.classes import Vector2
from src.utils import interactions


class DataHandler:
	_instance = None
	current_save = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		# Il faut utiliser os.path.dirname pour remonter le chemin correctement
		self.default_save_path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'../../../../backups/new_game_backup.json'
		)
		self.images_data = {}
		self.sounds_data = {}

	def get_data_from_last_save(self):
		# Il faut utiliser os.path.dirname pour éviter des chemins incorrects
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'../../../../backups/automatic/main-save.json'
		)

		# Ouverture du fichier de sauvegarde principale
		try:
			with open(path, 'r') as save:
				data = json.load(save)
		except FileNotFoundError:
			# Si le fichier de sauvegarde principale est vide ou inexistant, on utilise le backup par défaut
			with open(self.default_save_path, 'r') as save:
				data = json.load(save)

		for map in data['maps']:
			for element_index in range(len(data['maps'][map]['elements'])):
				data['maps'][map]['elements'][element_index]['position'] = self.list_to_vector2(data['maps'][map]['elements'][element_index]['position'])

				if 'pattern_timeline' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['pattern_timeline'] = self.list_transform(data['maps'][map]['elements'][element_index]['pattern_timeline'])
				else:
					data['maps'][map]['elements'][element_index]['pattern_timeline'] = []

				if 'interaction' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['interaction'] = self.get_interaction(data['maps'][map]['elements'][element_index]['interaction'])
				else:
					data['maps'][map]['elements'][element_index]['interaction'] = self.get_interaction('default')

				if 'side_effects' in data['maps'][map]['elements'][element_index]:
					data['maps'][map]['elements'][element_index]['side_effects'] = self.list_transform(data['maps'][map]['elements'][element_index]['side_effects'])
				else:
					data['maps'][map]['elements'][element_index]['side_effects'] = []


		return data
	
	def load_save(self, force = False):
		if self.current_save is None or force:
			self.current_save = self.get_data_from_last_save()
		return self.current_save
	
	def save(self, automatic = False):
		self.save_data(self.current_save, 'manual' if not automatic else 'automatic')

	def save_data(self, data, backup_path):
		# Correction de la redondance du mot-clé 'path'
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'../../../../backups',
			backup_path
		)

		# Enregistrement des données dans le fichier JSON
		with open(path, 'w') as file:
			json.dump(data, file, indent=4)

	def get_image_data(self, dir_name: str):
		png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../assets/images', dir_name, 'image.png')
		json_path = os.path.join('/'.join(png_path.split('/')[0:-1]), 'info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)
		
		return data, png_path
	
	def load_image(self, dir_name: str, force = False):
		if dir_name not in self.images_data or force:
			self.images_data[dir_name] = self.get_image_data(dir_name)
		return self.images_data[dir_name]

	def get_sound_track_data(self, dir_name: str):
		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../assets/sounds/effects', dir_name, 'info.json')
		with open(json_path, 'r') as file:
			data = json.load(file)

		sound_paths = {}
		for sound_name in data['sounds']:
			sound_paths[sound_name] = os.path.join('/'.join(json_path.split('/')[0:-1]), sound_name + '.' + data['sounds'][sound_name]['extension'])

		return data, sound_paths

	def load_sound(self, dir_name: str, sound_name: str, force = False):
		if dir_name == 'music': return self.load_music(sound_name)
		if dir_name not in self.sounds_data or force:
			self.sounds_data[dir_name] = {}
			self.sounds_data[dir_name][sound_name] = self.get_sound_data(dir_name, sound_name)
		elif sound_name not in self.sounds_data[dir_name] or force:
			self.sounds_data[dir_name][sound_name] = self.get_sound_data(dir_name, sound_name)

		return self.sounds_data[dir_name][sound_name]

	def load_music(self, map_name: str):
		music_name = self.load_save()['maps'][map_name]['music']

		json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../assets/sounds/music/info.json')

		with open(json_path, 'r') as file:
			data = json.load(file)
		if not music_name in data['sounds']: return None

		return data, os.path.join('/'.join(json_path.split('/')[0:-1]), music_name + '.' + data['sounds'][music_name]['extension'])

	def get_interaction(self, interaction_name: str = 'default'):
		if interaction_name == '':
			interaction_name = 'default'
		return interactions.get(interaction_name)

	def list_to_vector2(self, list2: list):
		if type(list2) == list and len(list2) == 2:
			return Vector2(list2[0], list2[1])
		else:
			raise AttributeError

	def list_transform(self, list2: list):
		new_list = []
		for el in list2:
			if type(el) == list:
				new_list.append(Vector2(el[0], el[1]))
			elif type(el) == str:
				new_list.append(self.get_interaction(el))
			else:
				raise ValueError
		return new_list

