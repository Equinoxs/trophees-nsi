from typing import Callable


class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map = None, npc_name = None):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.map = map
			self.focus = self.map.search_by_name(npc_name)

	def get_map(self):
		return self.map

	def change_map(self, map):
		self.map = map
  
	def get_focus(self):
		return self.focus

	def change_focus(self, npc_name):
		self.focus = self.map.search_by_name(npc_name)

	def update(self):
		self.map.update()
		self.focus.update_player()
