#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import Mission, Player, LogHandler, GameLoop, TimeHandler, DEBUG

class MissionHandler:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, missions_data = []):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.missions_data = missions_data
			self.missions = {}
			self.initialize_missions()
			self.current_mission = None
			self.mission_description_displayed = None
			self.mission_popup = None

	def get_current_mission(self):
		return self.current_mission

	def get_mission(self, mission_name: str) -> Mission | None:
		return self.missions.get(mission_name, None)

	def get_current_mission_name(self):
		for name, mission in self.missions.items():
			if mission == self.current_mission:
				return name
		return None

	def mission_ongoing(self):
		return self.current_mission is not None

	def initialize_missions(self):
		for name, data in self.missions_data.items():
			self.missions[name] = Mission(data, name)

	def abort_mission(self):
		if self.current_mission is not None:
			self.current_mission.abort()
			self.current_mission = None
			self.delete_description_displayed()
			Player().get_map().set_allow_map_change(True)
			GameLoop().get_control_handler().enable_all_actions()
			GameLoop().get_menu_handler().set_current_menu('loading', True)
			GameLoop().get_data_handler().load_save(force=True, reload=True)
			GameLoop().get_data_handler().set_save_allowed(True)
			GameLoop().get_menu_handler().set_last_menu()

	def start_mission(self, mission_name: str):
		if mission_name in self.missions and self.current_mission is None and mission_name not in Player().get_accomplished_missions():
			self.current_mission = self.missions[mission_name]
			GameLoop().get_data_handler().set_save_allowed(False)
			LogHandler().add(f'{Player().get_focus().get_name()} * start mission {self.current_mission.get_name()}')

	def display_description_of_current_mission(self):
		if self.mission_description_displayed is not None:
			return

		description_data = {
			'type': 'UIElement',
			'x': -20,
			'y': -15,
			'color': (0, 0, 0, 200),
			'text_color': (255,) * 3,
			'width': 'auto',
			'height': 'auto',
			'border_radius': 20,
			'label': 'mission started : ' + self.current_mission.get_description()
		}

		self.mission_description_displayed = GameLoop().get_menu_handler().get_menu('in_game').add_element(description_data)

	def delete_description_displayed(self):
		GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.mission_description_displayed)
		self.mission_description_displayed = None

	def update(self):
		if self.current_mission is not None:
			indicator = self.current_mission.update()
			if DEBUG and GameLoop().get_control_handler().is_activated('pass_mission'):
				self.current_mission.abort()
				indicator = 1

			if indicator == 1:
				LogHandler().add(f'{Player().get_focus().get_name()} * accomplish mission {self.current_mission.get_name()}')
				Player().add_accomplished_mission(self.current_mission)
				self.delete_description_displayed()
				GameLoop().throw_event({ 'mission' : self.get_current_mission_name() })
				self.current_mission.reset()
				self.current_mission = None  # La mission est terminée

				if self.mission_popup is not None:
					GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.mission_popup)

				data = {
					'type': 'UIElement',
					'class': 'mission_popup',
					'label': 'MISSION PASSED'
				}
				self.mission_popup = GameLoop().get_menu_handler().get_menu('in_game').add_element(data)
				Player().get_map().set_allow_map_change(True)
				GameLoop().get_control_handler().enable_all_actions()
				GameLoop().get_data_handler().set_save_allowed(True)
				GameLoop().get_data_handler().save()
				GameLoop().get_sound_mixer().play_sfx('level_up')

			elif indicator == -1:
				GameLoop().get_menu_handler().set_current_menu('loading', True)
				GameLoop().get_data_handler().reload_game()
				GameLoop().get_data_handler().set_save_allowed(True)
				GameLoop().get_menu_handler().set_current_menu('in_game')
				GameLoop().get_sound_mixer().play_sfx('game_over')
				LogHandler().add(f'{Player().get_focus().get_name()} * fail mission {self.current_mission.get_name()}')
				self.current_mission = None  # La mission est échouée
				self.delete_description_displayed()

				if self.mission_popup is not None:
					GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.mission_popup)

				data = {
					'type': 'UIElement',
					'class': 'mission_popup',
					'label': 'MISSION FAILED'
				}
				self.mission_popup = GameLoop().get_menu_handler().get_menu('in_game').add_element(data)
				Player().get_map().set_allow_map_change(True)
				GameLoop().get_control_handler().enable_all_actions()


			elif indicator == 0:
				self.display_description_of_current_mission()

		if self.mission_popup is not None and TimeHandler().add_chrono_tag('mission_popup') >= 2:
			GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.mission_popup)
			TimeHandler().remove_chrono_tag('mission_popup')
			self.mission_popup = None
