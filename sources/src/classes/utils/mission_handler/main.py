from src.classes import Mission, Player


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

	def initialize_missions(self):
		for name, data in self.missions_data.items():
			self.missions[name] = Mission(data)

	def start_mission(self, mission_name: str):
		self.missions[mission_name].start()

	def update(self):
		if self.current_mission is not None:
			if not self.current_mission.update():
				Player().add_accomplished_mission(self.current_mission)
				self.current_mission = None  # La mission est terminée
