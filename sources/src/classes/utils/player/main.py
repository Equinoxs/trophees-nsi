class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map = None, npc_name = None):
		if not hasattr(self, '_initialized'):
			self._initialized = True
			self.map = map
			self.focus = self.map.search_by_name(npc_name)
			if self.focus is None:
				raise ValueError(f'NPC {npc_name} not found in map {self.map.map_name}')
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

	def change_focus(self, npc_name):
		self.focus = self.map.search_by_name(npc_name)
		if self.focus is None:
			raise ValueError(f'NPC {npc_name} not found in map {self.map.map_name}')

	def update(self):
		self.map.update()
		self.focus.update_player()
