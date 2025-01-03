class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map = None, data_player: dict = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.map = map
			self.accomplished_missions = data_player['accomplished_missions']
			self.focus = self.map.search_by_name(data_player['current_npc_name'])
			self.focus.set_is_player(True)
			if self.focus is None:
				raise ValueError(f'NPC {data_player["current_npc_name"]} not found in map {self.map.map_name}')

	def get_map(self):
		return self.map

	def change_map(self, map_name: str):
		self.focus = self.map.remove(self.focus)
		self.map.load_elements_from(map_name)
		self.map.add(self.focus)

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

	def update(self):
		self.map.update()
