from src.classes import GameLoop, TimeHandler, LogHandler

# Cet effet fait disparaître le pnj pendant 3 secondes si le joueur s'approche trop près
# Une fois le pnj réapparu au bout des 3 secondes, il ne peut plus redisparaître
def npc_side_effect_test(self):
	if GameLoop().get_player().get_focus() == self:
		return  # On ne veut pas que cet effet s'applique si on est le focus du Player

	effect_made = self.side_effect_data('npc_side_effect_test_effect_made')
	cleared = self.side_effect_data('npc_side_effect_test_cleared')
	if not cleared:
		time = TimeHandler().add_chrono_tag('first_side_effect')

	if not effect_made:
		TimeHandler().remove_chrono_tag('first_side_effect')
		if (self.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom() and not effect_made:
			self.set_z_index(-1)
			LogHandler().add(f'{self.get_name()} * switch Z index to -1')
			self.side_effect_data('npc_side_effect_test_effect_made', True)

	elif not cleared and time > 3:
		LogHandler().add(f'{self.get_name()} * switch to the previous Z index')
		self.set_z_index_prev()
		TimeHandler().remove_chrono_tag('first_side_effect')
		self.side_effect_data('npc_side_effect_test_cleared', True)


side_effects = {
	"npc_side_effect_test": npc_side_effect_test
}