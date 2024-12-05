from src.classes import GameLoop, TimeHandler

# Cet effet fait disparaître le pnj pendant 3 secondes si le joueur s'approche trop près
# Une fois le pnj réapparu au bout des 3 secondes, il ne peut plus redisparaître
def npc_side_effect_test(self):
	time = TimeHandler().add_chrono_tag('first_side_effect')
	effect_made = self.side_effect_data('data_test')
 
	if not effect_made:
		TimeHandler().remove_chrono_tag('first_side_effect')
		if (self.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom() and not effect_made:
			self.set_z_index(-1)
			self.side_effect_data('data_test', True)

	elif time > 3:
		self.set_z_index(1)
		TimeHandler().remove_chrono_tag('first_side_effect')


side_effects = {
	"npc_side_effect_test": npc_side_effect_test
}