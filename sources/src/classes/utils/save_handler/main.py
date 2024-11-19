import json
import os


class SaveHandler:
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
		self.images_data = []

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
		return data
	
	def load_save(self, force = False):
		if self.current_save is None or force:
			self.current_save = self.get_data_from_last_save()
		return self.current_save
	
	def save(self, automatic = False):
		self.save_data(self.current_save, "manual" if not automatic else "automatic")

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