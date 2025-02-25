from src.classes import GameLoop, TimeHandler, Player


class Missions:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.missions_set = set()
			self.objectives_store = {}

			# Les clés ci-dessous doivent être de la forme <nom_de_la_mission>_<index_de_l'objectif>
			self.objective_descriptions = {
				'mission_test_1': 'get your y coordinate below 0 under 10 seconds!'
			}

			self.update_missions_set()

	def get_missions_set(self):
		return self.missions_set

	def update_missions_set(self):
		self.missions_set = set()
		for objectives in self.objective_descriptions:
			mission_name = '_'.join(objectives.split('_')[:-1])
			if mission_name not in self.missions_set:
				self.missions_set.add(mission_name)

	def is_mission(self, mission_name):
		return mission_name in self.missions_set

	def get_description(self, mission_name: str, index: int):
		return self.objective_descriptions.get(f'{mission_name}_{index}', None)

	def get_objectives_len(self, mission_name: str):
		method = True
		index = -1
		while method is not None:
			index += 1
			method = getattr(self, mission_name + '_' + str(index), None)
		print(index)
		return index



	def mission_test_0(self):
		menu_handler = GameLoop().get_menu_handler()
		dialog_name = 'mission_test_0_dialog'
		dialog_created = self.objectives_store.get(dialog_name + '_name', False)
		if not menu_handler.is_dialog(dialog_name):
			if not dialog_created:
				dialog_data = {
					'messages': ['Hello my friend!', 'I need you to do something a bit strange...', 'Could you get your y coordinate below 0?', 'Thank you very much!']
				}
				menu_handler.add_dialog(dialog_name, dialog_data)
				self.objectives_store[dialog_name + '_name'] = True
			else:
				del self.objectives_store[dialog_name + '_name']
				return 1
		return 0

	def mission_test_1(self):
		time = TimeHandler().add_chrono_tag('mission_test_0')
		index = 0
		if time == 0:
			GameLoop().get_sound_mixer().play_music('tryhard')  # l'objectif commence
		if time > 10:
			Player().get_focus().play_sound('game_over')
			index = -1  # mission échouée
		else:
			if Player().get_focus().get_position().get_y() <= 0:
				Player().get_focus().play_sound('magical_hit')
				index = 1  # objectif réussi
			else:
				index = 0  # objectif en cours
		if index != 0:
			GameLoop().get_sound_mixer().play_music_prev()
			TimeHandler().remove_chrono_tag('mission_test_0')
		return index



	def do(self, mission_name: str, index: int):
		objective_method = getattr(self, mission_name + '_' + str(index), None)
		return objective_method()
