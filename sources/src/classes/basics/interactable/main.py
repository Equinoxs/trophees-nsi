from src.classes import ControlHandler, Interactions

class Interactable:
	def __init__(self, interaction: str):
		self.interaction = interaction

	def handle_interaction(self, closest_vector):
		if ControlHandler().is_activated('interacted') and closest_vector.get_norm() <= 50:
			if callable(self.interaction):
				self.interaction(self)
			elif type(self.interaction) == str:
				Interactions().do(self.interaction, self)
			else:
				return
			ControlHandler().consume_event('interacted')
