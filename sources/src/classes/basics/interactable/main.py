from src.classes import ControlHandler
from src.utils import interactions


def default_interaction(player):
    return

class Interactable:
	def __init__(self, interaction: str = ''):
		if interaction == '':
			self.interaction = default_interaction
		else:
			self.interaction = interactions.get(interaction)

	def must_interact(self, self_position, player_position):
		if not ControlHandler().is_activated('interacted'):
			return False
		elif self_position.distance_to(player_position) <= 60:
			return True
