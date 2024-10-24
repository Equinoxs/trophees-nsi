import json
import os


class SaveHandler:
	_instance = None

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

	def save(self, data, backup_path):
		# Correction de la redondance du mot-clé 'path'
		path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			'../../../../backups',
			backup_path
		)

		# Enregistrement des données dans le fichier JSON
		with open(path, 'w') as file:
			json.dump(data, file, indent=4)
   