from src.classes import GameLoop, TimeHandler, Player, Vector2


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
			self.dialog_name = None

			# Les clés ci-dessous doivent être de la forme <nom_de_la_mission>_<index_de_l'objectif>
			self.objective_descriptions = {
				'mission_test_1': 'get your y coordinate below 0 under 10 seconds!',
				'introduction_denniston_1': 'Follow Alastair Denniston'
			}

			self.update_missions_set()

	def del_ui_elements(self):
		if self.dialog_name is not None:
			GameLoop().get_menu_handler().remove_dialog(self.dialog_name)
		for possible_element in self.objectives_store.values():
			GameLoop().get_menu_handler().get_menu('in_game').delete_element(possible_element)

	def reset_store(self):
		self.objectives_store = {}

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

	def use_create_dialog(self, dialog_name: str, dialog_data: dict):
		self.dialog_name = dialog_name
		menu_handler = GameLoop().get_menu_handler()
		self.dialog_box = self.objectives_store.get(dialog_name + '_created', False)

		if not menu_handler.is_dialog(dialog_name):
			if not self.dialog_box:
				menu_handler.add_dialog(dialog_name, dialog_data)
				self.objectives_store[dialog_name + '_created'] = True
			else:
				del self.objectives_store[dialog_name + '_created']
				self.dialog_name = None
				return 1
		return 0



	def mission_test_0(self):
		dialog_data = {
			'messages': ['Hello my friend!', 'I need you to do something a bit strange...', 'Could you get your y coordinate below 0?', 'Thank you very much!']
		}
		return self.use_create_dialog('mission_test_0_dialog', dialog_data)

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



	def introduction_denniston_0(self):
		Player().get_map().set_allow_map_change(False)
		GameLoop().get_control_handler().disable_actions(['go_forward', 'go_backward', 'go_left', 'go_right'])
		dialog_data = {
			'messages': [
				'Hello. Welcome to Bletchely Park',
				"I am Alastair Denniston, your commandant. By now, you're gonna do what I say.",
				'At Bletchley Park, we fight for peace, against the german people. Before I tell you more, would you please sign a contract. In a few words, you will remain under the silence about what is going on here. Otherwise you would be considered as a traitor that MIB must deal with.',
				'If you do consent, please continue. However, if you do not, please close that window, delete this game and never come back!',
				'Congratulations, let me present you the Park.'
			]
		}
		done = self.use_create_dialog('introduction_denniston_0_dialog', dialog_data)
		if done == 1:
			GameLoop().get_control_handler().enable_all_actions()
			return 1
		else:
			return 0
			

	def introduction_denniston_1(self):
		alastair_denniston = Player().get_map().search_by_name('alastair_denniston')
		alastair_denniston.set_objective(Vector2(1250, 2530))
		if alastair_denniston.move_npc_to_objective():
			return 0
		else:
			GameLoop().get_control_handler().enable_all_actions()
			return 1

	def introduction_denniston_2(self):
		dialog_data = {
			'messages': [
				'Do you see the house in front of us?',
				"It is called the Little House, here you're gonna find some stuff that may be useful to you."
			]
		}
		return self.use_create_dialog('introduction_denniston_0_dialog', dialog_data)



	def do(self, mission_name: str, index: int):
		objective_method = getattr(self, mission_name + '_' + str(index), None)
		return objective_method()
