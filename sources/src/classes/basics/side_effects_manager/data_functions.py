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


def visit_player(self):
	distance = self.get_position().distance_to(GameLoop().get_player().get_focus().get_position())
	out = self.side_effect_data('visit_player_out')
	if distance < 80:
		if out:
			self.play_sound('okay')
		self.side_effect_data('visit_player_out', False)
		TimeHandler().remove_chrono_tag('visit_player')
		self.set_following_pattern(False)
		self.set_objective(GameLoop().get_player().get_focus().get_position())
		self.move_npc_to_objective()
		if distance < 30:
			self.stop_moving()
	else:
		if not out:
			self.side_effect_data('visit_player_out', True)
			self.set_following_pattern(True)
			self.set_objective(None)


side_effects = {
	"npc_side_effect_test": npc_side_effect_test,
	"visit_player": visit_player
}