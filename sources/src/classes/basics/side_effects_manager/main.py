from src.classes import DataHandler

class SideEffectsManager:
	def __init__(self, side_effects):
		self.side_effects = side_effects
		self.side_effects_data = {}

	def side_effect_data(self, key: str, val = None):
		if val is not None or key not in self.side_effects_data:
			self.side_effects_data[key] = val
		return self.side_effects_data[key]

	def add_side_effect(self, side_effect_name: str):
		self.side_effects.append(DataHandler().get_side_effect(side_effect_name))

	def remove_side_effect(self, side_effect_name: str):
		side_effect = DataHandler().get_side_effect(side_effect_name)
		self.side_effects.remove(side_effect)

	def apply_side_effects(self):
		for side_effect in self.side_effects:
			side_effect(self)
