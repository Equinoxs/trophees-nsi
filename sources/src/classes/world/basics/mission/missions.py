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

				'introduction_denniston_1': 'Follow Alastair Denniston',
				'introduction_denniston_3': 'Follow Alastair Denniston',
				'introduction_denniston_4': 'Follow Alastair Denniston',
				'introduction_denniston_6': 'Follow Alastair Denniston',

				'first_job_1': 'Get the letter in Building 2',
				'first_job_2': 'Deliver the letter in Hut 6',

				'act2_upgrade_0': 'Listen to Denniston'

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

	def use_create_dialog(self, dialog_name: str, dialog_data: dict, immobilize_player: bool = False):
		self.dialog_name = dialog_name
		menu_handler = GameLoop().get_menu_handler()
		self.dialog_box = self.objectives_store.get(dialog_name + '_created', False)

		if immobilize_player:
			GameLoop().get_control_handler().disable_actions(['go_forward', 'go_backward', 'go_left', 'go_right'])

		if not menu_handler.is_dialog(dialog_name):
			if not self.dialog_box:
				menu_handler.add_dialog(dialog_name, dialog_data)
				self.objectives_store[dialog_name + '_created'] = True
			else:
				del self.objectives_store[dialog_name + '_created']
				self.dialog_name = None
				if immobilize_player:
					GameLoop().get_control_handler().enable_all_actions()
				return 1
		return 0

	def use_move_npc(self, npc_name: str, destination: Vector2):
		npc = Player().get_map().search_by_name(npc_name)
		npc.set_objective(destination)
		if npc.move_npc_to_objective():
			return 0
		else:
			return 1



	# --- MISSION TEST ---

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
			index = -1  # mission échouée
		else:
			if Player().get_focus().get_position().get_y() <= 0:
				index = 1  # objectif réussi
			else:
				index = 0  # objectif en cours
		if index != 0:
			GameLoop().get_sound_mixer().play_music_prev()
			TimeHandler().remove_chrono_tag('mission_test_0')
		return index



	# --- MISSION DÉCOUVERTE DE LA MAP AVEC DENNISTON ---

	def introduction_denniston_0(self):
		Player().get_map().set_allow_map_change(False)
		Player().get_map().remove_wall('beginning_wall')
		dialog_data = {
			'messages': [
				'Hello. Welcome to Bletchely Park',
				"I am Alastair Denniston, your commandant. By now, you're gonna do what I say.",
				'At Bletchley Park, we fight for peace, against the german people. Before I tell you more, would you please sign a contract. In a few words, you will remain under the silence about what is going on here. Otherwise you would be considered as a traitor that MIB must deal with.',
				'If you do consent, please continue. However, if you do not, please close that window, delete this game and never come back!',
				'Congratulations, let me present you the Park.'
			]
		}
		return self.use_create_dialog('introduction_denniston_0_dialog', dialog_data, immobilize_player=True)

	def introduction_denniston_1(self):
		return self.use_move_npc('alastair_denniston', Vector2(1250, 2530))

	def introduction_denniston_2(self):
		dialog_data = {
			'messages': [
				'Do you see the house in front of us?',
				"It is called the Little House, here you're gonna find some stuff that may be useful to you."
			]
		}
		return self.use_create_dialog('introduction_denniston_2_dialog', dialog_data)

	def introduction_denniston_3(self):
		return self.use_move_npc('alastair_denniston', Vector2(800, 2580))

	def introduction_denniston_4(self):
		return self.use_move_npc('alastair_denniston', Vector2(750, 2150))

	def introduction_denniston_5(self):
		dialog_data = {
			'messages': [
				'This big building to your left is the Mansion. One of the most important edifice here.',
				'I hope you remembered the names of the places I introduced, you will need them in a few moments.'
			]
		}
		return self.use_create_dialog('introduction_denniston_5_dialog', dialog_data)

	def introduction_denniston_6(self):
		return self.use_move_npc('alastair_denniston', Vector2(950, 1360))

	def introduction_denniston_7(self):
		dialog_data = {
			'messages': [
				'There are the Huts, you can see the number 6 and the number 8 on these.',
				'They will provide you some very important stuff you will need.',
				'If you follow this way, you will find Building 1 and Building 2. I am sure you will enjoy this place!',
				"Go! My men are waiting for you, and maybe I'll see you around."
			]
		}
		return self.use_create_dialog('introduction_denniston_7_dialog', dialog_data)



	# --- PREMIÈRE MISSION ---

	def first_job_0(self):
		dialog_data = {
			'messages': [
				'So you\'re the new one, huh?',
				'I saw you coming, you seem like a hard worker. And that\'s good, because I got a mission for you!',
				'You need to get into Building 2, you will see a wide table with a letter in it, I need you to get it and bring it to Hut 6.',
				'In Hut 6, you\'ll see a table at the far end with letters like the one you will pick on it, put the mail on this table and we\'ll get the rest.',
				'Thank you very much!'
			]
		}
		return self.use_create_dialog('first_job_0_dialog', dialog_data)

	def first_job_1(self):
		inventory = Player().get_focus().get_inventory()
		if inventory is not None and inventory.get_name() == 'building_2_table_2_mail':
			return 1
		return 0

	def first_job_2(self):
		if Player().get_map().get_name() == 'hut_6':
			item = Player().get_map().search_by_name('hut_6_table_1').get_item('building_2_table_2_mail')
			if item is not None:
				return 1
		return 0



	# --- DENNISTON MONTE EN GRADE LE JOUEUR ---

	def act2_upgrade_0(self):
		dialog_data = {
			'messages': [
				'You have been doing really well after hearing from my men.',
				"That's why I give you the access to Hut 8.",
				'You may take a tour in it, some people expect to see you there.'
			]
		}
		return self.use_create_dialog('introduction_denniston_0_dialog', dialog_data)



	def do(self, mission_name: str, index: int):
		objective_method = getattr(self, mission_name + '_' + str(index), None)
		return objective_method()
