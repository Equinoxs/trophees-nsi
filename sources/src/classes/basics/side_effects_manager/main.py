from src.classes import SideEffects

class SideEffectsManager:
	def __init__(self, side_effects):
		self.side_effects = set(side_effects)
		self.side_effects_data = {}

	def side_effect_data(self, key: str, val = None):
		if val is not None or key not in self.side_effects_data:
			self.side_effects_data[key] = val
		return self.side_effects_data[key]

	def add_side_effect(self, side_effect_name: str):
		self.side_effects.add(side_effect_name)

	def remove_side_effect(self, side_effect_name: str):
		self.side_effects.discard(side_effect_name)

	def apply_side_effects(self):
		for side_effect_name in self.side_effects:
			SideEffects().do(side_effect_name, self)

	def update(self):
		self.apply_side_effects()
