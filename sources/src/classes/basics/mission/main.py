class Mission:
	def __init__(self, mission_data):
		self.description = mission_data['description']
		self.required_level = mission_data['required_level']
		self.rewards = mission_data['rewards']  # TODO: implémenter des récompenses plus complexes une fois que l'inventaire sera fait
		self.objectives = mission_data['objectives']
		self.objective_index = 0
		self.do_again = True

	def get_description(self):
		return self.description

	def get_required_level(self):
		return self.required_level

	def get_rewards(self):
		return self.rewards

	def start(self):
		return

	def update(self):
		if self.do_again:
			self.do_again = self.objectives[self.objective_index]()
		else:
			self.objective_index += 1
		if self.objective_index + 1 == len(self.objectives):
			return False
		return True
