from src.classes import GameLoop


class Mission:
	def __init__(self, mission_data: dict, name: str):
		self.name = name
		self.description = mission_data['description']
		self.required_level = mission_data['required_level']
		self.rewards = mission_data['rewards']  # TODO: implémenter des récompenses plus complexes une fois que l'inventaire sera fait
		self.objectives = mission_data['objectives']
		self.objective_index = 0
		self.indicator = 0
		self.displayed_description = None

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	def get_objective_description(self):
		return self.objectives[self.objective_index][1]

	def get_required_level(self):
		return self.required_level

	def get_rewards(self):
		return self.rewards

	def display_objective_description(self):
		if self.displayed_description is not None:
			return  # La description est déjà affichée

		data = {
			'type': 'UIElement',
			'label': self.get_objective_description(),
			'x': 'center',
			'y': 20,
			'width': 'auto',
			'height': 'auto',
			'text_color': (255,) * 3,
			'color': (0, 0, 0, 80)
		}

		self.displayed_description = GameLoop().get_menu_handler().get_menu('in_game').add_element(data)

	def delete_objective_description(self):
		GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.displayed_description)
		self.displayed_description = None

	def update(self):
		if self.indicator == 0:
			self.indicator = self.objectives[self.objective_index][0]()
			self.display_objective_description()
		elif self.indicator == 1:
			self.objective_index += 1
			self.display_objective_description()
			self.inidcator = 0
			if self.objective_index == len(self.objectives):
				self.delete_objective_description()
				return 1  # mission_réussie
		elif self.indicator == -1:
			self.indicator = 0
			self.delete_objective_description()
			return -1  # mission échouée
		return 0  # en cours
