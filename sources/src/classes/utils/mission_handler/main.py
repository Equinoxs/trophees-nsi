from src.classes import Mission, Player, LogHandler


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
			self.missions[name] = Mission(data, name)

	def start_mission(self, mission_name: str):
		if mission_name in self.missions and self.current_mission is None and mission_name not in Player().get_accomplished_missions():
			self.current_mission = self.missions[mission_name]
			self.current_mission.start()
			LogHandler().add(f'{Player().get_focus().get_name()} * start mission {self.current_mission.get_name()}')

	def update(self):
		if self.current_mission is not None:
			indicator = self.current_mission.update()
			if indicator == 1:
				LogHandler().add(f'{Player().get_focus().get_name()} * accomplish mission {self.current_mission.get_name()}')
				Player().add_accomplished_mission(self.current_mission)
				self.current_mission = None  # La mission est terminée
			elif indicator == -1:
				LogHandler().add(f'{Player().get_focus().get_name()} * fail mission {self.current_mission.get_name()}')
				self.current_mission = None  # La mission est échouée
			elif indicator == 0:
				return  # la missions continue, le state n'a pas besoin d'être changé