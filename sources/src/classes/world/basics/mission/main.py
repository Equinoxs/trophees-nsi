from src.classes import GameLoop, Missions


class Mission:
	def __init__(self, mission_data: dict, name: str):
		self.name = name
		self.description = mission_data['description']
		self.required_level = mission_data.get('required_level', 1)
		self.rewards = mission_data.get('rewards', 1)
		self.objectives_len = Missions().get_objectives_len(name)
		self.objective_index = 0
		self.indicator = 0
		self.displayed_description = None

	def abort(self):
		self.objective_index = 0
		self.indicator = 0
		self.delete_objective_description()
		Missions().del_ui_elements()
		Missions().reset_store()

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	def get_objective_description(self):
		return Missions().get_description(self.name, self.objective_index)

	def get_required_level(self):
		return self.required_level

	def get_rewards(self):
		return self.rewards

	def display_objective_description(self, force: bool = False):
		if self.get_objective_description() is None:
			self.delete_objective_description()
			return

		if self.displayed_description is not None and not force:
			return  # La description est déjà affichée

		data = {
			'type': 'UIElement',
			'label': self.get_objective_description(),
			'x': 'center',
			'y': 20,
			'width': 'auto',
			'height': 'auto',
			'border_radius': 20,
			'border_length': 1,
			'border_color': (255,) * 3,
			'text_color': (255,) * 3,
			'color': (0, 0, 0, 80)
		}

		self.delete_objective_description()
		self.displayed_description = GameLoop().get_menu_handler().get_menu('in_game').add_element(data)

	def delete_objective_description(self):
		if self.displayed_description is not None:
			GameLoop().get_menu_handler().get_menu('in_game').delete_element(self.displayed_description)
			self.displayed_description = None

	def update(self):
		if self.indicator == 0:
			self.indicator = Missions().do(self.name, self.objective_index)
			self.display_objective_description()

		elif self.indicator == 1:
			self.objective_index += 1
			self.display_objective_description(force=True)
			self.indicator = 0

			if self.objective_index == self.objectives_len:
				self.delete_objective_description()
				return 1  # mission_réussie

		elif self.indicator == -1:
			self.indicator = 0
			self.delete_objective_description()
			self.objective_index = 0
			return -1  # mission échouée

		return 0  # en cours
