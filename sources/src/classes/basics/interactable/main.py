from src.classes import ControlHandler, Interactions, Vector2, Player, MenuHandler, Missions

class Interactable:
	def __init__(self, interaction: str):
		self.interaction = interaction
		self.interaction_marker = None
		self.interaction_available = True
		if self.interaction is None:
			self.interaction_available = False

	def is_interaction_available(self):
		return self.interaction_available

	def set_interaction_available(self, available: bool):
		self.interaction_available = available
		if not available:
			MenuHandler().remove_marker(self.interaction_marker)
			self.interaction_marker = None

	def handle_interaction(self, closest_vector):
		if self.is_interaction_available() and ControlHandler().is_activated('interacted') and closest_vector.get_norm() <= 50:
			if type(self.interaction) == str and 'start_' in self.interaction and Missions().is_mission(self.interaction.split('start_')[-1]):
				self.set_interaction_available(False)

			if callable(self.interaction):
				self.interaction(self)
			elif type(self.interaction) == str:
				Interactions().do(self.interaction, self)
			else:
				return
			ControlHandler().consume_event('interacted')

	def update(self, closest_vector: Vector2):
		self.handle_interaction(closest_vector)

		if closest_vector.get_norm() <= 50:
			if self.interaction_marker is None and self.is_interaction_available():
				data = {
					'label': ControlHandler().get_key_letter('interacted'),
					'color': (20, 20, 20, 200),
					'text_color': (255,) * 3,
					'border_radius': 50,
					'border_length': 1,
					'border_color': (200,) * 3,
					'position': Player().get_focus().get_position(),
					'width': 'auto',
					'height': 'auto'
				}
				self.interaction_marker = MenuHandler().add_marker(data)
		elif self.interaction_marker is not None:
			MenuHandler().remove_marker(self.interaction_marker)
			self.interaction_marker = None
