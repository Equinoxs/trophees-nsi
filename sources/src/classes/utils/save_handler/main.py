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
		self.default_save_path = os.path.join(
			os.path.abspath(__file__),
			'../../../../../backups/new_game_backup.json'
		)
		return

	def get_data_from_last_save(self):
		path = os.path.join(
			os.path.abspath(__file__),
			'../../../../../backups/automatic/main-save.json'
		)
		with open(path, 'r') as save:
			data = json.load(save)
		if data == {}:
			with open(self.default_save_path, 'r') as save:
				data = json.load(save)
		return data

	def save(self, data, backup_path):
		path = path = os.path.join(
			os.path.abspath(__file__),
			'../../../../backups',
   			backup_path
		)
		with open(path, 'w') as file:
			json.dump(data, file, indent=4)
