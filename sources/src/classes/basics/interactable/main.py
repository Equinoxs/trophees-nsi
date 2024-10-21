from typing import Callable
from .....main import control_handler


class Interactable:
	def __init__(self, interaction: Callable = None):
		if interaction is None:
			interaction = self.default_interaction
		self.interaction = interaction

	def default_interaction(self):
		return

	def must_interact(self, self_position, player_position):
		if not control_handler.is_activated('interacted'):
			return False
		elif self_position.distance_to(player_position) <= 2:
			return True
