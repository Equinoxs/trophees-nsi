class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map = None, data_player = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.map = map
			self.level = data_player['level']
			self.accomplished_missions = data_player['accomplished_missions']
			self.focus = self.map.search_by_name(data_player['current_npc_name'])
			self.focus.set_is_player(True)
			if self.focus is None:
				raise ValueError(f'NPC {data_player["current_npc_name"]} not found in map {self.map.map_name}')  # Python <3.12 compat
			else:
				width, height = self.focus.get_image().get_size()
				self.focus.get_position().set_all(self.focus.get_position().get_x() - width // 2, self.focus.get_position().get_y() - height)

	def get_map(self):
		return self.map

	def change_map(self, map_name: str):
		self.focus = self.map.remove(self.focus)
		self.map.load_elements_from(map_name)
		self.map.add(self.focus)

	def get_focus(self):
		return self.focus

	def get_level(self):
		return self.level

	def get_accomplished_missions(self):
		return self.accomplished_missions

	def add_accomplished_mission(self, mission_name: str):
		self.accomplished_missions.append(mission_name)

	def change_focus(self, npc_name):
		self.focus.set_is_player(False)
		self.focus = self.map.search_by_name(npc_name)
		self.focus.set_is_player(True)
		if self.focus is None:
			raise ValueError(f'NPC {npc_name} not found in map {self.map.map_name}')

	def update(self):
		self.map.update()
