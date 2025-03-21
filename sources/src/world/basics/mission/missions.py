import pygame

from src import GameLoop, TimeHandler, Player, Vector2, SCREEN_WIDTH, SCREEN_HEIGHT, DEBUG


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

				'mission_test_1': 'Get at the top of the map under 10 seconds!',
		
				'gordon_welchman_presentation_0': 'Listen to the stranger',

				'alan_turing_presentation_0': 'Listen to the stranger',
				
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
				'bombes_manipulation_2': 'Connect the wires',
				'bombes_manipulation_3': 'Talk to Hugh Alexander',
				'bombes_manipulation_4': 'Listen to Hugh Alexander',

				'decrypt_enigma_1': 'Interact with Enigma',
				'decrypt_enigma_2': 'Decrypt the message',
				'decrypt_enigma_3': 'Come back to Alan Turing',
				'decrypt_enigma_4': 'Listen to Alan Turing',

				'act3_upgrade_0': 'Listen to Alastair Denniston',

				'insert_colossus_1': 'Collect the punched cards',
				'insert_colossus_2': 'Insert the punched cards into Colossus',
				'insert_colossus_3': 'Talk again to Tommy Flowers',
				'insert_colossus_4': 'Listen to Tommy Flowers',

				'final_0': 'Listen to Alastair Denniston',
				'final_1': 'Destroy Enigma',
				'final_3': 'Destroy the Bombe',
				'final_5': 'Destroy Colossus',
				'final_7': 'Talk to Denniston',
				'final_8': 'Listen to Denniston',

				'epilogue_joan_clarke_0': 'Listen to Joan Clarke',
		
				'epilogue_bill_tutte_0': 'Listen to William (Bill) Tutte',
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
		if object_name + '_interacted' not in self.objectives_store:
			self.objectives_store[object_name + '_interacted'] = False
			object.set_interaction('mission_interaction', force=True)
		elif self.objectives_store[object_name + '_interacted']:
			self.objectives_store[object_name + '_interacted'] = False
			object.set_interaction(None)
			del self.objectives_store[object_name + '_interacted']
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
			'messages': ['Hello my friend!', 'I need you to do something a bit strange...', 'Could you get at the top of the map please?', 'Thank you very much!']
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
				'My name is Gordon Welchman. I am the head of this Hut.',
				'Let me explain you what do we do here. In Hut 6, we work on traffic analysis of encrypted German communications. You see, the Germans communicate via encrypted message, we can intercept them but we don\'t know how to break those messages.',
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
				'the workload can be quite hard sometimes, good luck',
				'I hope I\'ll see you around soon, goodbye my friend!'
			]
		}
		return self.use_create_dialog('mansion_presentation_0_dialog', dialog_data)



	# --- PRÉSENTATION DU BUILDING 1 ---

	def building_1_presentation_0(self):
		dialog_data = {
			'messages': [
				'Thank you for coming in Building 1!',
				'A lot of work that we do here is focused on administrative stuff, it\'s not very important but that\'s the way it is, somebody must do it huh!',
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
				"I am Alexander Denniston, your commander. By now, you're gonna do what I say.",
				'At Bletchley Park, we fight for peace, against the Nazis. Before I tell you more, would you please sign this secrecy act. In a few words, you have to remain silent about what is going on here, even to your coworkers from other buildings, Otherwise you will be considered as a national threat',
				'If you do consent, please continue. However, if you do not, please close that window, delete this game and never come back!',
				'Congratulations, let me show you around.'
			]
		}
		return self.use_create_dialog('introduction_denniston_0_dialog', dialog_data, immobilize_player=True)

	def introduction_denniston_1(self):
		return self.use_move_npc('alastair_denniston', Vector2(1250, 2530))

	def introduction_denniston_2(self):
		dialog_data = {
			'messages': [
				'Do you see the building in front of us?',
				"you're going to find some stuff that may be useful in there."
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
				'This big building to your left is the mansion. One of the most important edifices here.',
				'I hope you remember the names of the places I introduced you, you will need them in a few moments.'
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
				'If you follow this way, you will find Building 1 and Building 2. Good luck with your work.',
				"Go! My men are waiting for you, and maybe I'll see you around."
			]
		}
		return self.use_create_dialog('introduction_denniston_7_dialog', dialog_data)



	# --- PREMIÈRE MISSION ---

	def first_job_0(self):
		dialog_data = {
			'messages': [
				'So you\'re the new one, huh?',
				'I saw you coming, you look like a hard worker. And that\'s good, because I got a mission for you!',
				'You need to get into Building 2, the orange building in front of us. There is a wide table with a letter on it, I need you to get it and bring it to Hut 6.',
				'In Hut 6, there is a table at the far end with letters like the one you have to get, put the mail on this table and we\'ll do the rest.',
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
				'label': 'Encrypted Message: ..-. .- .-.. -.-. --- -. / ...-- / .--. --- ... .. - .. --- -. / .-- . ... -'
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
			if input.get_text().upper() == 'FALCON 3 POSITION WEST' or (DEBUG and input.get_text().upper() == 'PASS'):
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
				'You have been doing really well from what I\'ve heard.',
				"That's why I give you the access to Hut 8.",
				'some people are expecting you there.'
			]
		}
		return self.use_create_dialog('introduction_denniston_0_dialog', dialog_data)


	def alan_turing_presentation_0(self):
		dialog_data = {
			'messages': [
				'Ah, you must be the new recruit. Welcome to Hut 8.',
				'I\'m Alan Turing head of the Hut 8 cryptanalysis teams. Our work here focuses on deciphering the naval Enigma, code-named \'shark\', which is even more complex than other versions.',
				'No one really wanted to try to tackle that one really, they all thought it was impossible',
				'To tackle this challenge, we\'ve designed an electromechanical machine',
				'the BOMBE.',
				'It helps us quickly find the right settings to decode messages.',
				'Our goal is to break these codes as fast as possible. The sooner we succeed, the more valuable the information we uncover.',
				'Now, I think Hugh Alexander over here has a mission for you, go see him!'
			]
		}
		return self.use_create_dialog('alan_turing_presentation_0_dialog', dialog_data)



	# --- PRÉSENTATION DE HUGH ALEXANDER ---

	def hugh_alexander_presentation_0(self):
		dialog_data = {
			'messages': [
				'Ah, so you\'re the new recruit Alan mentioned. Welcome to the team!',
				'I\'m Hugh Alexander, nice to meet you.',
				'The machine helps, but cracking the code still requires some sharp thinking and careful analysis.',
				'I do have a mission for you, come back and see me later'
			]
		}
		return self.use_create_dialog('hugh_alexander_presentation_0_dialog', dialog_data)



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
		return self.use_interaction('bombe')

	def bombes_manipulation_2(self):
		pos_green = Vector2(480, 170)
		pos_blue = Vector2(480, 400)
		pos_red = Vector2(480, 640)
		if 'bombes_manipulation_2_initialized' not in self.objectives_store:
			self.objectives_store['bombes_manipulation_2_initialized'] = True
			GameLoop().get_control_handler().disable_all_actions()
			GameLoop().get_mission_handler().get_current_mission().move_displayed_description('mission')
			GameLoop().get_menu_handler().set_current_menu('mission')

			background_data = {
				'type': 'UIElement',
				'id': 'background',
				'image': 'bombe_wires',
				'image_height': SCREEN_HEIGHT,
				'color': 'transparent',
				'x': 0,
				'y': 0
			}

			wires_width = 40

			green_wire_data = {
				'type': 'Line',
				'id': 'green_wire',
				'start_pos': pos_green.copy(),
				'end_pos': pos_green.copy(),
				'color': (14, 181, 17),
				'width': wires_width
			}

			blue_wire_data = {
				'type': 'Line',
				'id': 'blue_wire',
				'start_pos': pos_blue.copy(),
				'end_pos': pos_blue.copy(),
				'color': (12,77,214),
				'width': wires_width
			}

			red_wire_data = {
				'type': 'Line',
				'id': 'red_wire',
				'start_pos': pos_red.copy(),
				'end_pos': pos_red.copy(),
				'color': (246,31,0),
				'width': wires_width
			}

			GameLoop().get_menu_handler().get_current_menu().add_element(background_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(green_wire_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(blue_wire_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(red_wire_data)

			self.objectives_store['green_flag'] = False
			self.objectives_store['blue_flag'] = False
			self.objectives_store['red_flag'] = False

			self.objectives_store['green_accomplished'] = False
			self.objectives_store['blue_accomplished'] = False
			self.objectives_store['red_accomplished'] = False
		else:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_pos = Vector2(mouse_x, mouse_y)
			if GameLoop().get_control_handler().is_activated('clicked'):
				acceptance = 60
				green_end = Vector2(760, 640)
				blue_end = Vector2(760, 170)
				red_end = Vector2(760, 400)

				# Gestion des flags
				mouse_free = not self.objectives_store['green_flag'] and not self.objectives_store['blue_flag'] and not self.objectives_store['red_flag']
				if mouse_pos.distance_to(pos_green) < acceptance and mouse_free and not self.objectives_store['green_accomplished']:
					self.objectives_store['green_flag'] = True
				elif mouse_pos.distance_to(pos_blue) < acceptance and mouse_free and not self.objectives_store['blue_accomplished']:
					self.objectives_store['blue_flag'] = True
				elif mouse_pos.distance_to(pos_red) < acceptance and mouse_free and not self.objectives_store['red_accomplished']:
					self.objectives_store['red_flag'] = True

				# Gestion de la réparation des câbles
				elif mouse_pos.distance_to(green_end) < acceptance and self.objectives_store['green_flag']:
					self.objectives_store['green_flag'] = False
					self.objectives_store['green_accomplished'] = True
				elif mouse_pos.distance_to(blue_end) < acceptance and self.objectives_store['blue_flag']:
					self.objectives_store['blue_flag'] = False
					self.objectives_store['blue_accomplished'] = True
				elif mouse_pos.distance_to(red_end) < acceptance and self.objectives_store['red_flag']:
					self.objectives_store['red_flag'] = False
					self.objectives_store['red_accomplished'] = True

				# Si on clique au milieu de nulle part, on échoue la mission
				elif self.objectives_store['green_flag'] or self.objectives_store['blue_flag'] or self.objectives_store['red_flag']:
					self.objectives_store['green_flag'] = False
					self.objectives_store['blue_flag'] = False
					self.objectives_store['red_flag'] = False
					if not self.objectives_store['green_accomplished']:
						GameLoop().get_menu_handler().get_current_menu().get_element_by_id('green_wire').get_end_pos().copy(pos_green)
					if not self.objectives_store['blue_accomplished']:
						GameLoop().get_menu_handler().get_current_menu().get_element_by_id('blue_wire').get_end_pos().copy(pos_blue)
					if not self.objectives_store['red_accomplished']:
						GameLoop().get_menu_handler().get_current_menu().get_element_by_id('red_wire').get_end_pos().copy(pos_red)
					

			# Gestion de l'affichage
			if self.objectives_store['green_flag']:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('green_wire').get_end_pos().set_all(mouse_x, mouse_y)
			elif self.objectives_store['blue_flag']:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('blue_wire').get_end_pos().set_all(mouse_x, mouse_y)
			elif self.objectives_store['red_flag']:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('red_wire').get_end_pos().set_all(mouse_x, mouse_y)

			if self.objectives_store['green_accomplished'] and self.objectives_store['blue_accomplished'] and self.objectives_store['red_accomplished']:
				GameLoop().get_control_handler().enable_all_actions()
				GameLoop().get_mission_handler().get_current_mission().move_displayed_description('in_game')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('background')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('green_wire')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('blue_wire')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('red_wire')
				GameLoop().get_menu_handler().set_current_menu('in_game')
				del self.objectives_store['bombes_manipulation_2_initialized']
				return 1
		return 0

	def bombes_manipulation_3(self):
		return self.use_interaction('hugh_alexander')

	def bombes_manipulation_4(self):
		dialog_data = {
			'messages': [
				'Great, thanks to you, the Bombe works again!',
				'I saw Alan while you were repairing the Bombe, he would like to see you.',
				'See you soon!'
			]
		}
		return self.use_create_dialog('decrypt_enigma_4_dialog', dialog_data)



	# --- DÉCRYPTAGE AVEC ENIGMA ---

	def decrypt_enigma_0(self):
		dialog_data = {
			'messages': [
				'Now the time has come! I have a serious mission for you, let me explain what you will have to accomplish.',
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
		border_width = 250

		words = [
			'XGRTYPLM', 'WQAZNCVB', 'POIUYTRE', 'LKJHGFDS', 'MNBVCXZQ',
			'ASDFGHJK', 'ZXCVBNML', 'QWERTYUI', 'WETTER', 'PLMOKNIJ',
			'UHYGTFRE', 'EDCXSWZA', 'LOKIMJNH', 'RTYUIOPQ', 'GHJKLZXC',
			'VBNMASDF', 'YTREWQPO', 'QAZXSWED', 'MLPOKIUJ', 'NHBVGTFD'
		] 
 
		if 'decrypt_enigma_2_initialized' not in self.objectives_store:
			self.objectives_store['decrypt_enigma_2_initialized'] = True
			GameLoop().get_control_handler().disable_all_actions()
			GameLoop().get_control_handler().enable_actions(['enter'])
			GameLoop().get_mission_handler().get_current_mission().move_displayed_description('mission')
			GameLoop().get_menu_handler().set_current_menu('mission')

			enigma_bg_data = {
				'type': 'UIElement',
				'id': 'enigma_bg',
				'image': 'enigma',
				'image_height': SCREEN_HEIGHT,
				'color': 'transparent'
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

			border_data = {
				'type': 'UIElement',
				'id': 'border',
				'width': border_width,
				'height': 50,
				'x': 'center',
				'y': 250,
				'border_length': 2,
				'border_color': (255, 255, 255),
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
				'label': 'DFSU MKLE BJAP BCAHJ',
				'color': 'transparent',
				'text_align': 'left',
				'text_color': (255, 255, 255)
			}

			probable_word_data = {
				'type': 'UIElement',
				'id': 'probable_word',
				'width': 'auto',
				'height': 'auto',
				'x': 'center',
				'y': 500,
				'font_size': 40,
				'font_family': 'monofonto',
				'label': 'Probable word: WETTER',
				'color': 'transparent',
				'text_color': (255, 255, 255)
			} 

			current_word_data = {
				'type': 'UIElement',
				'id': 'current_word',
				'width': 'auto',
				'height': 'auto',
				'x': 'center',
				'y': 550,
				'font_size': 40,
				'font_family': 'monofonto',
				'label': 'Current word: ' + words[0],
				'text_color': (255, 255, 255)
			}

			self.objectives_store['words_index'] = 0

			GameLoop().get_menu_handler().get_current_menu().add_element(enigma_bg_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(light_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(border_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(encrypted_message_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(probable_word_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(current_word_data)

		else:
			element = GameLoop().get_menu_handler().get_current_menu().get_element_by_id('encrypted_message')
			for event in GameLoop().get_control_handler().get_pygame_events():
				if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):

					if event.key == pygame.K_LEFT:
						if self.objectives_store['words_index'] > -len(words) + 1:
							self.objectives_store['words_index'] -= 1
					else:
						if self.objectives_store['words_index'] < 11:
							self.objectives_store['words_index'] += 1

					element.get_position().set_x((SCREEN_WIDTH - border_width) / 2 + 3 + 20 * self.objectives_store['words_index'])
					GameLoop().get_menu_handler().get_current_menu().get_element_by_id('current_word').set_label('Current word: ' + words[-self.objectives_store['words_index']])

			if self.objectives_store['words_index'] == -8:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('light').set_color((255,) * 4)
				if GameLoop().get_control_handler().is_activated('enter'):
					GameLoop().get_control_handler().enable_all_actions()
					GameLoop().get_mission_handler().get_current_mission().move_displayed_description('in_game')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('enigma_bg')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('light')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('border')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('encrypted_message')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('probable_word')
					GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('current_word')
					GameLoop().get_menu_handler().set_current_menu('in_game')
					del self.objectives_store['decrypt_enigma_2_initialized']
					return 1
			else:
				GameLoop().get_menu_handler().get_current_menu().get_element_by_id('light').set_color((0,) * 3)

		return 0

	def decrypt_enigma_3(self):
		return self.use_interaction('alan_turing')

	def decrypt_enigma_4(self):
		dialog_data = {
			'messages': [
				'Well done! I see you are an expert.',
				'Denniston told me he wanted to talk to you about something...'
			]
		}
		return self.use_create_dialog('decrypt_enigma_4_dialog', dialog_data)



	# --- DENNISTON DONNE ACCÈS LE BLOCK H AU JOUEUR ---

	def act3_upgrade_0(self):
		dialog_data = {
			'messages': [
				'After all that you have done for this country in here, I must thank you.',
				'Moreover, from what I have heard, you are really talented. Now, I\'ll grant you access to Block H, some of the best cryptanalysts are waiting for you in it.'
			]
		}
		return self.use_create_dialog('act3_upgrade_0_dialog', dialog_data)



	# --- INSÉRER LES PUNCHED CARDS DANS COLOSSUS ---

	def insert_colossus_0(self):
		dialog_data = {
			'messages': [
				'Hello, we\'ve been told someone new was going to join us, I\'m Thomas Flowers, but you can call me Tommy.'
				'basically, our job here consists in cracking german high commands comunications, the ones Hitler sends to his generals.'
				'We don\'t know what the machine looks like, we code-named it Tunny, but we\'ll manage. You know Alan right ? He helps us for that part'
				'By the way, we are preparing some tests and we need to use Colossus, it\'s a digital computer I made',
				'Could you insert the punch cards that you see on this table in Colossus please? The team would be very thankful.'
			]
		}
		return self.use_create_dialog('insert_colossus_0_dialog', dialog_data)

	def insert_colossus_1(self):
		return self.use_wait_for_item('colossus_punched_cards')

	def insert_colossus_2(self):
		if self.use_interaction('colossus') == 1 and Player().get_focus().get_inventory() is not None and Player().get_focus().get_inventory().get_name() == 'colossus_punched_cards':
			Player().get_focus().purge_inventory()
			return 1
		else:
			return 0

	def insert_colossus_3(self):
		return self.use_interaction('tommy_flowers')

	def insert_colossus_4(self):
		dialog_data = {
			'messages': [
				'Well done! I see you are an expert.',
				'Denniston told me he wanted to talk to you about something...'
			]
		}
		return self.use_create_dialog('insert_colossus_4_dialog', dialog_data)



	# --- DERNIÈRE MISSION DU JEU => GÉNÉRIQUE DE FIN ---

	def final_0(self):
		if Player().get_level() < 10:
			Player().set_level(10)
		dialog_data = {
			'messages': [
				'A lot of years have passed since you\'ve been there. Now war is almost over.',
				'Still, I need you for a last mission, you will have to destroy all the machines to erase all traces of this place and its activcities.',
				'Destroy Enigma, the Bombe and Colossus, and come back to me when you are done.'
			]
		}
		return self.use_create_dialog('final_0_dialog', dialog_data)

	def final_1(self):
		return self.use_interaction('enigma')

	def final_2(self):
		Player().get_map().search_by_name('enigma').kill()
		return 1

	def final_3(self):
		return self.use_interaction('bombe')

	def final_4(self):
		Player().get_map().search_by_name('bombe').kill()
		return 1

	def final_5(self):
		return self.use_interaction('colossus')

	def final_6(self):
		Player().get_map().search_by_name('colossus').kill()
		return 1

	def final_7(self):
		return self.use_interaction('alastair_denniston')

	def final_8(self):
		dialog_data = {
			'messages': [
				'Your job here is now over, keep in mind that under no circumstances you may talk about this.',
				'Your family, your friends, no one has to know. You must act like you\'ve never met all these people before'
				'All of them, strangers.'
				'None of this existed, Enigma was never broken, and there\'s no such thing as a Bombe or Colossus'
				'You can stay here more time if you want, you just have to know that this is in the public interest that you keep your mouth shut',
				'You really don\'t want to break the contract.',
				'Thank you for your services, have a nice life'
			]
		}
		return self.use_create_dialog('final_8_dialog', dialog_data)

	def final_9(self):
		initial_y = 800
		if 'final_9_initialized' not in self.objectives_store:
			self.objectives_store['final_9_initialized'] = True

			GameLoop().get_control_handler().disable_all_actions()
			GameLoop().get_menu_handler().set_current_menu('mission')
			GameLoop().get_sound_mixer().play_music('Cosmic - Lish Grooves')

			background_data = {
				'type': 'UIElement',
				'id': 'background',
				'color': (0, 0, 0, 255)
			}

			title_data = {
				'type': 'UIElement',
				'id': 'title',
				'class': 'credits_writing',
				'label': 'The End',
				'font_size': 80,
				'y': 50
			}

			thanks_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Thank you for playing'
			}

			project_manager_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Project Manager - Alexis LAROSE'
			}

			editor_in_chief_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Editor-In-Chief - Diego GIMENEZ'
			}

			ui_designer_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'UI Designer - Dimitri NERRAND'
			}

			inventory_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Inventory System Designer - Maël KEN'
			}

			sound_engineer_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Sound Engineer - Diego GIMENEZ'
			}

			artistic_director_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Artistic Director - Maël KEN'
			}

			artistic_assistant_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Artistic Assistant - Dimitri NERRAND'
			}

			mathematical_expert_data = {
				'type': 'UIElement',
				'class': 'credits_writing',
				'label': 'Mathematical Expert - Alexis LAROSE'
			}

			self.objectives_store['final_9_elements'] = []

			GameLoop().get_menu_handler().get_current_menu().add_element(background_data)
			GameLoop().get_menu_handler().get_current_menu().add_element(title_data)

			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(thanks_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(project_manager_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(editor_in_chief_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(ui_designer_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(inventory_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(sound_engineer_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(artistic_director_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(artistic_assistant_data))
			self.objectives_store['final_9_elements'].append(GameLoop().get_menu_handler().get_current_menu().add_element(mathematical_expert_data))

		else:
			elapsed_time = TimeHandler().add_chrono_tag('final_9')

			if elapsed_time > 17:
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('background')
				GameLoop().get_menu_handler().get_current_menu().delete_element_by_id('title')
				TimeHandler().remove_chrono_tag('final_9')
				GameLoop().get_control_handler().enable_all_actions()
				GameLoop().get_menu_handler().set_current_menu('in_game')
				GameLoop().get_sound_mixer().play_music_prev()
				return 1

			for idx, element in enumerate(self.objectives_store['final_9_elements']):
				if element.get_position().get_y() <= 5 and elapsed_time > 0:
					GameLoop().get_menu_handler().get_current_menu().delete_element(element)
				element.get_position().set_y(initial_y + idx * 60 - elapsed_time * 80)

		return 0



	# --- MISSIONS DE L'ÉPILOGUE ---

	def epilogue_joan_clarke_0(self):
		dialog_data = {
			'messages': [
				'Hello, I\'ve never relly had the time to chat with you',
				'I am Joan Clarke, I recently became the deputy manager of this hut. I used to decrypt encrypted messages from the nazis by using the bamburismus method.',
				'It is a method that consists in finding the most probable word in the encrypted message, and then decrypt the message by using the word as a key. But I am sure you already know that.',
				'I developed it with Alan Turing, who is a very good friend of mine. I am sure you know him too. It is so sad that he left Bletchley Park...',
				'He really appreciated you for the work that you have done and for your sympathy'
			]
		}
		return self.use_create_dialog('epilogue_joan_clarke_0_dialog', dialog_data)

	def epilogue_bill_tutte_0(self):
		dialog_data = {
			'messages': [
				'Hey, my name is William Tutte, but every body calls me Bill here.',
				'What did I do here you say? I am a mathematician, and I deduced the structure of the Tunny cipher, which is, I must say, very complex.',
				'How does it work ? Oh, well, it somehow uses XOR and different kind of wheels, it was a pain to deduce !'
				'I did it by using the Colossus machine, which was designed by Tommy Flowers, you have already worked with him I think.',
				'I am sure you know that the Colossus machine is the world\'s first programmable, electronic, digital computer !',
				'You know, I am very proud of my work here, and I am sure you are too. I hope we will see you around soon.'
			]
		}
		return self.use_create_dialog('epilogue_bill_tutte_0_dialog', dialog_data)



	def do(self, mission_name: str, index: int):
		objective_method = getattr(self, mission_name + '_' + str(index), None)
		return objective_method()
