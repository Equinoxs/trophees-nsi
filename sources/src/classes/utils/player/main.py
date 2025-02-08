from src.classes import GameLoop, Vector2


class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map = None, data_player: dict = None, map_name: str = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.map_name = map_name
			self.map = map
			self.accomplished_missions = data_player['accomplished_missions']
			self.focus = self.map.search_by_name(data_player['current_npc_name'])
			self.focus.set_is_player(True)
			if self.focus is None:
				raise ValueError(f'NPC {data_player["current_npc_name"]} not found in map {self.map.map_name}')

	def get_map(self):
		return self.map

	def get_map_name(self):
		return self.map_name

	def change_map(self, map_name: str):
		GameLoop().get_menu_handler().set_current_menu('loading', True)
		self.map_name = map_name
		self.focus = self.map.remove(self.focus)
		GameLoop().get_sound_mixer().free_all_channels()
		self.map.load_elements_from(map_name)
		potential_player = self.map.search_by_name(self.focus.get_name())
		if potential_player is not None:
			self.map.remove(potential_player)
		self.map.add(self.focus)
		GameLoop().get_camera().initialize()
		GameLoop().get_menu_handler().set_current_menu('in_game')

	def get_focus(self):
		return self.focus

	def get_level(self):
		return int(self.focus.get_level())

	def set_level(self, level: int):
		self.focus.set_level(level)
		self.map.throw_event('player_level_change')

	def get_accomplished_missions(self):
		return self.accomplished_missions

	def add_accomplished_mission(self, mission):
		self.accomplished_missions.append(mission.get_name())
		self.set_level(self.get_level() + mission.get_rewards())

	def change_focus(self, npc_name):
		self.focus.set_is_player(False)
		self.focus = self.map.search_by_name(npc_name)
		self.focus.set_is_player(True)
		if self.focus is None:
			raise ValueError(f'NPC {npc_name} not found in map {self.map.map_name}')

	def teleport_to(self, point: Vector2 | str):
		if isinstance(point, Vector2):
			self.focus.get_position().copy(point)
		elif type(point) == str:
			searched_object = self.map.search_by_name(point)
			if searched_object is not None:
				self.focus.get_position().copy(searched_object.get_position().copy())

	def update(self):
		self.map.update()
