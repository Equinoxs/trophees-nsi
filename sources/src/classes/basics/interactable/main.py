from src.classes import ControlHandler

class Interactable:
	def __init__(self, interaction = 'default'):
		self.interaction = interaction

	def handle_interaction(self, closest_vector):
		if ControlHandler().is_activated('interacted') and closest_vector.get_norm() <= 50:
			self.interaction(self)
			ControlHandler().finish_event('interacted')
