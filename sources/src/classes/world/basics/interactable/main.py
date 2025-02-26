from src.classes import ControlHandler, Interactions, Vector2, Player, MenuHandler, Missions, MissionHandler

class Interactable:
	def __init__(self, interaction: str, mission: str):
		self.interaction = interaction
		self.interaction_marker = None
		self.interaction_available = True
		if self.interaction is None:
			self.interaction_available = False

		self.mission = mission
		self.mission_marker = None

		if not hasattr(self, 'mission_marker_x_offset'):
			self.mission_marker_x_offset = 0
		if not hasattr(self, 'mission_marker_y_offset'):
			self.mission_marker_y_offset = 0

	def get_mission(self):
		return self.mission

	def set_mission_name(self, mission_name: str):
		self.mission = mission_name

	def is_mission_available(self):
		return Missions().is_mission(self.mission) and not MissionHandler().mission_ongoing() and Player().get_focus().get_level() >= MissionHandler().get_mission(self.mission).get_required_level() and not self.mission in Player().get_accomplished_missions()

	def set_mission(self, mission: str):
		if not Missions().is_mission(mission):
			return

		self.mission = mission

		mission_marker_data = {
			'image': 'mission_indicator',
			'image_height': 50,
			'position': self.get_position(),
			'width': 'auto',
			'height': 'auto',
			'x_offset': self.mission_marker_x_offset,
			'y_offset': self.mission_marker_y_offset,
			'special': True
		}

		self.mission_marker = MenuHandler().add_marker(mission_marker_data)

	def is_interaction_available(self):
		return self.interaction_available

	def set_interaction_available(self, available: bool):
		self.interaction_available = available
		if not available and self.interaction_marker is not None:
			MenuHandler().remove_marker(self.interaction_marker)
			self.interaction_marker = None

	def handle_interaction(self, closest_vector: Vector2) -> bool:
		if (self.is_interaction_available() or Missions().is_mission(self.mission)) and ControlHandler().is_activated('interacted') and closest_vector.get_norm() <= 50:

			if Missions().is_mission(self.mission) and not MissionHandler().mission_ongoing():
				self.set_interaction_available(False)
				MissionHandler().start_mission(self.mission)
				return True

			if callable(self.interaction):
				self.interaction(self)
			elif type(self.interaction) == str:
				Interactions().do(self.interaction, self)
			else:
				return False
			ControlHandler().consume_event('interacted')
			return True

	def catch_event(self, event):
		if type(event) == dict and 'mission' in event and event['mission'] == self.mission:
			self.mission = None
			if self.mission_marker is not None:
				MenuHandler().remove_marker(self.mission_marker)
				self.mission_marker = None

	def update(self, closest_vector: Vector2):
		self.handle_interaction(closest_vector)

		if self.mission_marker is not None and not self.is_mission_available():
			MenuHandler().remove_marker(self.mission_marker)
			self.mission_marker = None

		if self.mission is not None and self.mission in Player().get_accomplished_missions():
			self.mission = None
		if self.mission_marker is None and self.is_mission_available():
			self.set_mission(self.mission)

		if closest_vector.get_norm() <= 50:
			if self.interaction_marker is None and (self.is_interaction_available() or (Missions().is_mission(self.mission) and not MissionHandler().mission_ongoing())):
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

	def __del__(self):
		if hasattr(self, 'interaction_marker') and self.interaction_marker is not None:
			MenuHandler().remove_marker(self.interaction_marker)
		if self.mission_marker is not None:
			MenuHandler().remove_marker(self.mission_marker)
