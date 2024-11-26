from src.classes import ControlHandler, Player
from src.utils import interactions


def default_interaction(player):
    return

class Interactable:
	def __init__(self, interaction: str = ''):
		if interaction == '':
			self.interaction = default_interaction
		else:
			self.interaction = interactions.get(interaction)

	def handle_interaction(self, closest_vector):
		if ControlHandler().is_activated('interacted') and closest_vector.get_norm() <= 50:
			self.interaction(Player())
