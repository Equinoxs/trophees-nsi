from src.classes import SaveHandler, Map


class Player:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, map_name = None, npc_name = None):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			self.focus = self.map.search_by_name(npc_name)
			self.map = None
			self.initialize_map(map_name)
		
	def initialize_map(self, map_name):
		saved_data = SaveHandler().load_save()
		self.map = Map(saved_data['maps'][saved_data["player"]["current_map_name"]]['elements']), self.saved_data['player']['current_npc_name']

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
