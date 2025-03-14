import pygame

from src.classes import GameLoop, TimeHandler, Player, Vector2, SCREEN_WIDTH, SCREEN_HEIGHT


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
		
				'gordon_welchman_presentation_0': 'Listen to the stranger',

				'alan_turing_presentation_0': 'Listen to the stranger',
				'alan_turing_presentation_1': 'Follow Alan Turing',
				'alan_turing_presentation_2': 'Follow Alan Turing',
				
				'hugh_alexander_presentation_0': 'Listen to the stranger',

				'mansion_presentation_0': 'Listen to the stranger',
		
				'building_1_presentation_0': 'Listen to the stranger',

				'introduction_denniston_1': 'Follow Alastair Denniston',
				'introduction_denniston_3': 'Follow Alastair Denniston',
				'introduction_denniston_4': 'Follow Alastair Denniston',
				'introduction_denniston_6': 'Follow Alastair Denniston',

				'first_job_1': 'Get the letter in Building 2',
				'first_job_2': 'Decrypt the morse encrypted message',
				'first_job_3': 'Deliver the letter in Hut 6',

				'act2_upgrade_0': 'Listen to Denniston',

				'bombes_manipulation_1': 'Interact with the Bombe',

				'decrypt_enigma_1': 'Interact with Enigma',

				'insert_colossus_1': 'Collect the punch card',
				'insert_colossus_2': 'Interact with Colossus',
				'insert_colossus_3': 'Insert the punch card into Colossus'
			}

			self.update_missions_set()

	def del_ui_elements(self):
		if self.dialog_name is not None:
			GameLoop().get_menu_handler().remove_dialog(self.dialog_name)
		for possible_element in self.objectives_store.values():
			GameLoop().get_menu_handler().get_menu('in_game').delete_element(possible_element)

	def get_objectives_store(self):
		return self.objectives_store

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

	def use_interaction(self, object_name: str):
		object = Player().get_map().search_by_name(object_name)
		if object is None:
			return 0
		if object.get_interaction() is None:
			self.objectives_store[object_name + '_interacted'] = False
			object.set_interaction('mission_interaction', force=True)
		elif self.objectives_store[object_name + '_interacted']:
			self.objectives_store[object_name + '_interacted'] = False
			object.set_interaction(None)
			return 1
		return 0

	def use_wait_for_item(self, item_name: str):
		inventory = Player().get_focus().get_inventory()
		if inventory is not None and inventory.get_name() == item_name:
			return 1
		return 0



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
			GameLoop().get_sound_mixer().play_music('mission')
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



	# --- PRÉSENTATION DE GORDON WELCHMAN ---

	def gordon_welchman_presentation_0(self):
		dialog_data = {
			'messages': [
				'Hello new one! I\'m glad to meet you.',
				'My name is Gordon Welchman. I am the boss of this Hut.',
				'Let me explain you what do we do here. In Hut 6, we work on traffic analysis of encrypted German communications. You see, the Germans communicate via encrypted message, we have the but we don\'t know how to break them.',
				'They use the Enigma machine to encrypt and decrypt their messages, by using a common cipher which changes every day, so we have to find a clever way to guess this cipher fast.',
				'In conclusion, we try to manage to break the German Enigma machine cipher. If we do it, we would have very important pieces of information about the German organizations and plans.'
			]
		}
		return self.use_create_dialog('gordon_welchman_presentation_0_dialog', dialog_data)



	# --- PRÉSENTATION DU MANOIR ---

	def mansion_presentation_0(self):
		dialog_data = {
			'messages': [
				'Hey! I hope you enjoy this place.',
				'Well, here is the Mansion, if you want some peace moments, go there, you have to read and to work!',
				'You just need to know that this place is to get some rest, take a coffee or a cup of tea, and get unstressed, which is very important in jobs like the guys do.',
				'Finally, I hope I\'ll see you around soon, goodbye my friend!'
			]
		}
		return self.use_create_dialog('mansion_presentation_0_dialog', dialog_data)



	# --- PRÉSENTATION DU BUILDING 1 ---

	def building_1_presentation_0(self):
		dialog_data = {
			'messages': [
				'Thank you for coming in Building 1!',
				'A lot of work that we do here is focused on administrative stuff, it\'s not very important but let it be, somebody must do it huh!',
				'You know, what do we do here, they keep saying it\'s important but I don\'t know if we will manage to do it...'
			]
		}
		return self.use_create_dialog('building_1_presentation_0_dialog', dialog_data)



	# --- MISSION DÉCOUVERTE DE LA MAP AVEC DENNISTON ---

	def introduction_denniston_0(self):
		Player().get_map().set_allow_map_change(False)
		Player().get_map().remove_wall('beginning_wall')
		dialog_data = {
			'messages': [
				'Hello. Welcome to Bletchely Park',
				"I am Alastair Denniston, your commandant. By now, you're gonna do what I say.",
				'At Bletchley Park, we fight for peace, against the german people. Before I tell you more, would you please sign a contract. In a few words, you will remain under the silence about what is going on here. Otherwise you would be considered as a traitor that MI6 must deal with.',
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
		return self.use_wait_for_item('building_2_table_2_mail')

	def first_job_2(self):
		if GameLoop().get_menu_handler().get_current_menu_name() != 'mission':
			GameLoop().get_control_handler().disable_all_actions()
			GameLoop().get_mission_handler().get_current_mission().move_displayed_description('mission')
			GameLoop().get_menu_handler().set_current_menu('mission')

			paper_data = {
				'type': 'UIElement',
				'id': 'paper_bg',
				'class': 'first_job_2_paper_bg'
			}

			encrypted_message_data = {
				'type': 'UIElement',
				'id': 'encrypted_message',
				'class': 'first_job_2_encrypted_message',
				'label': 'Encrypted Message: ..-. .- .-.. -.-. --- -. / ...-- / .--. --- ... .. - .. --- -. / . .- --. .-.. . / .-- . ... - .-.-.- / ...- --- .-. -... . .-. . .. - ..- -. --. / ..-. ..- .-. / -- .. ... ... .. --- -. / -.-. --- -... .-.'
			}

			morse_input_data = {
				'type': 'TextInput',
				'id': 'morse_input',
				'class': 'first_job_2_morse_input'
			}

			GameLoop().get_menu_handler().get_current_menu().add_element(paper_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(encrypted_message_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(morse_input_data)
		else:
			input = GameLoop().get_menu_handler().get_current_menu().get_element_by_id('morse_input')
			if input.get_text().upper() == 'FALCON 3 POSITION EAGLE WEST. VORBEREITUNG FUR MISSION COBR':
				GameLoop().get_control_handler().enable_all_actions()
				GameLoop().get_mission_handler().get_current_mission().move_displayed_description('in_game')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('paper_bg')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('encrypted_message')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('morse_input')
				GameLoop().get_menu_handler().set_current_menu('in_game')
				return 1
		return 0

	def first_job_3(self):
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


	def alan_turing_presentation_0(self):
		dialog_data = {
			'messages': [
				'Ah, you must be the new recruit. Welcome to Hut 8.',
				'I’m Alan Turing. Our work here focuses on deciphering the German Navy\'s Enigma, which is even more complex than other versions.',
				'To tackle this challenge, we\'ve designed an electromechanical machine',
				'the BOMBE.',
				'It helps us quickly find the right settings to decode messages.',
				'Our goal is to break these codes as fast as possible. The sooner we succeed, the more valuable the information we uncover.',
				'Now, come, I\'ll introduce you to the team. I think some of them have a mission for you...'
			]
		}
		return self.use_create_dialog('alan_turing_presentation_0_dialog', dialog_data)

	def alan_turing_presentation_1(self):
		return self.use_move_npc('alan_turing', Vector2(303, 479))
	
	def alan_turing_presentation_2(self):
		return self.use_move_npc('alan_turing', Vector2(303, 130))

	def hugh_alexander_presentation_0(self):
		dialog_data = {
			'messages': [
				'Ah, so you’re the new recruit Alan mentioned. Welcome to the team!',
				'I’m Hugh Alexander, head of the Hut 8 cryptanalysis team. Here, we focus on breaking the Enigma messages from the German Navy.',
				'The machine helps, but cracking the code still requires sharp thinking and careful analysis.',
				'Let’s see what you’re capable of. We just intercepted a fresh batch of encrypted messages.',
				'Your task is to go to the mansion, find the encrypted message, examine it and decode it',
				'Once you found it, come back to me.'
			]
		}
		return self.use_create_dialog('hugh_alexander_presentation_0_dialog', dialog_data)
	
	def do(self, mission_name: str, index: int):
		objective_method = getattr(self, mission_name + '_' + str(index), None)
		return objective_method()



	# --- DÉCOUVERTE DES BOMBES DE TURING ET WELCHMAN ---

	def bombes_manipulation_0(self):
		Player().get_map().set_allow_map_change(False)
		dialog_data = {
			'messages': [
				'I have a mission for you, the bombe is broken, do you think you can repair it?',
				'Great! Come back to me when you\'re done.'
			]
		}
		return self.use_create_dialog('bombes_manipulation_0_dialog', dialog_data)

	def bombes_manipulation_1(self):
		if self.use_interaction('bombe'):

			# gérer l'affichage du menu
			GameLoop().get_menu_handler().set_current_menu('missions')
			menu = GameLoop().get_menu_handler().get_current_menu()
			if menu.get_element_by_id('bombe_background') is None:
				background_data = {
					'type': 'UIElement',
					'id': 'bombe_background',
					'image_path': 'bombe_background',
					'image_height': 600
				}
				menu.add_element(background_data)
		return 1 # à continuer



	# --- DÉCRYPTAGE AVEC ENIGMA ---

	def decrypt_enigma_0(self):
		dialog_data = {
			'messages': [
				'Now the time has come! You have you serious mission, let me tell you what you will have to accomplish.',
				'You\'re gonna decrypt a message with the Enigma machine that we collected from the nazis.',
				'To get a little more technical in my explainations, Enigma encrypt a letter in another one. However, if it tries to encrypt an "h" for example, the encrypted letter corresponding won\'t be an "h".',
				'We just have to find a probable word used by the nazis in the encrypted message, and find the corresponding word based on what I said. For example, the word "wheather" is traduced by "Wetter" in german.',
				'The encrypted word of "Wetter" won\'t see its first letter as a "W" or its second letter as a "e", et ceatera.',
				'We modified our Enigma machine, so in it, you will see the encrypted message that you have to slide and find the probable word. When you will be done, you should see a light turning on.'
			]
		}
		return self.use_create_dialog('decrypt_enigma_0_dialog', dialog_data)

	def decrypt_enigma_1(self):
		return self.use_interaction('enigma')

	def decrypt_enigma_2(self):
		if 'decrypt_enigma_2_initialized' not in self.objectives_store:
			self.objectives_store['decrypt_enigma_2_initialized'] = True
			GameLoop().get_control_handler().disable_all_actions()
			GameLoop().get_control_handler().enable_actions(['enter'])
			GameLoop().get_mission_handler().get_current_mission().move_displayed_description('mission')
			GameLoop().get_menu_handler().set_current_menu('mission')

			enigma_bg_data = {
				'type': 'UIElement',
				'id': 'enigma_bg',
				'width': 700,
				'height': 575,
				'x': 'center',
				'y': 'center',
				'color': (255, 255, 150)
			}

			light_data = {
				'type': 'UIElement',
				'id': 'light',
				'width': 50,
				'height': 50,
				'border_radius': 25,
				'color': (0, 0, 0),
				'x': 'center',
				'y': 'center',
				'border_length': 4,
				'border_color': (120,) * 3,
			}

			border_width = 250
			border_data = {
				'type': 'UIElement',
				'id': 'border',
				'width': border_width,
				'height': 50,
				'x': 'center',
				'y': 250,
				'border_length': 2,
				'border_color': (0, 0, 0),
				'color': 'transparent'
			}

			encrypted_message_data = {
				'type': 'UIElement',
				'id': 'encrypted_message',
				'width': 'auto',
				'height': 'auto',
				'x': (SCREEN_WIDTH - border_width) / 2 + 3,
				'y': 250,
				'font_size': 40,
				'font_family': 'monofonto',
				'label': 'DFSU MKLE BJAP BCAHJ DKFL FJKD SQOF KWXA MNRO',
				'color': 'transparent',
				'text_align': 'left'
			}

			GameLoop().get_menu_handler().get_current_menu().add_element(enigma_bg_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(light_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(border_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(encrypted_message_data)
		else:
			element = GameLoop().get_menu_handler().get_current_menu().get_element_by_id('encrypted_message')
			for event in GameLoop().get_control_handler().get_pygame_events():
				if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
					x = element.get_position().get_x()
    
					if event.key == pygame.K_LEFT:
						element.get_position().set_x(x + 20)
					else:
						element.get_position().set_x(x - 20)
    
			if 357 < element.get_position().get_x() < 359:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('light').set_color((255,) * 4)
				if GameLoop().get_control_handler().is_activated('enter'):
					GameLoop().get_control_handler().enable_all_actions()
					GameLoop().get_mission_handler().get_current_mission().move_displayed_description('in_game')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('enigma_bg')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('light')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('border')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('encrypted_message')
					GameLoop().get_menu_handler().set_current_menu('in_game')
					return 1
			else:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('light').set_color((0,) * 3)
				if GameLoop().get_control_handler().is_activated('enter'):
					return -1
		return 0



	# --- INSÉRER LA PUNCH CARD DANS COLOSSUS ---

	def insert_colossus_0(self):
		dialog_data = {
			'messages': [
				'Hey! we are preparing some tests and we need colossus.',
				'Could you insert the punch card that you see on this table in Colossus please? The team would be very thankful.'
			]
		}
		return self.use_create_dialog('insert_colossus_0_dialog', dialog_data)

	def insert_colossus_1(self):
		return self.use_wait_for_item('colossus_punch_card')
