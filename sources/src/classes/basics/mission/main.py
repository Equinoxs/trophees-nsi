from src.classes import LogHandler


class Mission:
	def __init__(self, mission_data: dict, name: str):
		self.name = name
		self.description = mission_data['description']
		self.required_level = mission_data['required_level']
		self.rewards = mission_data['rewards']  # TODO: implémenter des récompenses plus complexes une fois que l'inventaire sera fait
		self.objectives = mission_data['objectives']
		self.objective_index = 0
		self.indicator = 0

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	def get_required_level(self):
		return self.required_level

	def get_rewards(self):
		return self.rewards

	def start(self):
		return

	def update(self):
		if self.indicator == 0:
			self.indicator = self.objectives[self.objective_index]()
		elif self.indicator == 1:
			self.objective_index += 1
			self.inidcator = 0
			if self.objective_index == len(self.objectives):
				return 1  # mission_réussie
		elif self.indicator == -1:
			self.indicator = 0
			return -1  # mission échouée
		return 0  # en cours
